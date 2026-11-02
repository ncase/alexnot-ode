"""The evolutionary loop: monkeys propose, the scorer selects. Starts from the blank program."""
from dataclasses import dataclass
import random
import time

from monkeys import MONKEYS
from programs import Level, Proposal, ScoredProgram, canonicalize, evaluate

EVO_MAX_GENERATIONS: int = 20
EVO_EARLY_STOP_COUNTDOWN: int = 3
PARENTS_TOP_K: int = 10
# Two programs whose scores differ by less than this are the same program, spelled differently
SAME_SCORE_TOLERANCE: float = 1e-5
# Time limits, in seconds. An unlucky slow level still gets an answer, from whatever got scored in time
TIME_LIMIT_PER_LEVEL: float = 30.0
TIME_LIMIT_PER_ROUND: float = 10.0


@dataclass
class RoundLog:
    """What happened in one round of evolution, for the reasoning trace."""
    seconds: float
    best_score: float
    new_proposals_by_monkey: dict[str, int]  # After skipping programs we've already tried
    scored_count: int  # Fewer than the proposals, if we ran out of time
    parents: list[ScoredProgram]  # The parents this round picked, for the next round


def select_parents(population: list[ScoredProgram]) -> list[ScoredProgram]:
    """The top programs overall, skipping different spellings of a better program."""
    parents: list[ScoredProgram] = []
    for program in sorted(population, key=lambda program: program.score):
        if len(parents) == PARENTS_TOP_K:
            break
        # We're going through scores in order, so the last parent we kept is always the closest one
        if not parents or program.score - parents[-1].score > SAME_SCORE_TOLERANCE:
            parents.append(program)
    return parents


def search(level: Level) -> ScoredProgram:
    """Returns the best-scoring program ever seen."""
    return min(search_population(level), key=lambda program: program.score)


def search_population(level: Level, round_logs: list[RoundLog] | None = None) -> list[ScoredProgram]:
    """Returns every program the search scored, not just the winner. Handy for asking "how close did the right answer get?".

    Optional round_logs: a list the caller owns, which gets one RoundLog per round.
    """
    level_start_time: float = time.perf_counter()
    # Fixed seed, so runs are repeatable (unless a time limit kicks in)
    shuffler: random.Random = random.Random(0)
    blank: ScoredProgram = evaluate(Proposal('', [{} for _ in level.demos]), level)
    population: list[ScoredProgram] = [blank]
    tried_sources: set[str] = {blank.source}
    best: ScoredProgram = blank
    parents: list[ScoredProgram] = [blank]
    countdown: int = EVO_EARLY_STOP_COUNTDOWN

    for _ in range(EVO_MAX_GENERATIONS):
        round_start_time: float = time.perf_counter()
        deadline: float = min(round_start_time + TIME_LIMIT_PER_ROUND, level_start_time + TIME_LIMIT_PER_LEVEL)

        # Skip anything we've already tried, or another monkey just proposed. This happens BEFORE scoring, since scoring's the slow part
        new_proposals: dict[str, Proposal] = {}
        new_proposals_by_monkey: dict[str, int] = {}
        for monkey in MONKEYS:
            new_proposals_by_monkey[monkey.__name__] = 0
            for proposal in monkey(parents, level):
                source_before_fit: str = canonicalize(proposal, level).source
                if source_before_fit not in tried_sources and source_before_fit not in new_proposals:
                    new_proposals[source_before_fit] = proposal
                    new_proposals_by_monkey[monkey.__name__] += 1

        # Random order, so running out of time doesn't always cut off the same monkey
        shuffled_sources: list[str] = list(new_proposals)
        shuffler.shuffle(shuffled_sources)

        children: list[ScoredProgram] = []
        scored_count: int = 0
        for source_before_fit in shuffled_sources:
            if time.perf_counter() > deadline:
                break
            scored_count += 1
            tried_sources.add(source_before_fit)
            # A crash just means this program's dropped
            try:
                child: ScoredProgram = evaluate(new_proposals[source_before_fit], level)
            except (ValueError, FloatingPointError, OverflowError):
                continue
            # Fitting can flip signs, which can turn this into a program we've already seen
            if child.source != source_before_fit and child.source in tried_sources:
                continue
            tried_sources.add(child.source)
            children.append(child)

        # Nothing new left to try
        if not children:
            break
        population.extend(children)
        parents = select_parents(population)

        generation_best: ScoredProgram = min(children, key=lambda program: program.score)
        improved: bool = generation_best.score < best.score
        if improved:
            best = generation_best
        if round_logs is not None:
            round_logs.append(RoundLog(time.perf_counter() - round_start_time, best.score, new_proposals_by_monkey, scored_count, parents))

        # Out of time for the whole level?
        if time.perf_counter() > level_start_time + TIME_LIMIT_PER_LEVEL:
            break
        if improved:
            countdown = EVO_EARLY_STOP_COUNTDOWN
        else:
            countdown -= 1
            if countdown == 0:
                break
    return population
