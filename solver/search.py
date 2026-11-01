"""The evolutionary loop: monkeys propose, the scorer selects. Starts from the blank program."""
from monkeys import MONKEYS
from programs import Level, Proposal, ScoredProgram, canonicalize, evaluate

EVO_MAX_GENERATIONS: int = 20
EVO_EARLY_STOP_COUNTDOWN: int = 3
PARENTS_TOP_K: int = 5


def select_parents(population: list[ScoredProgram], level: Level) -> list[ScoredProgram]:
    """The top programs overall, plus the best program on each variable. (Like AlexNot's parent islands)"""
    parents: dict[str, ScoredProgram] = {program.source: program for program in sorted(population, key=lambda program: program.score)[:PARENTS_TOP_K]}
    for name in level.variable_names:
        best_on_variable: ScoredProgram = min(population, key=lambda program: program.variable_costs[name])
        parents[best_on_variable.source] = best_on_variable
    return list(parents.values())


def search(level: Level) -> ScoredProgram:
    """Returns the best-scoring program ever seen."""
    blank: ScoredProgram = evaluate(Proposal('', [{} for _ in level.demos]), level)
    population: list[ScoredProgram] = [blank]
    tried_sources: set[str] = {blank.source}
    best: ScoredProgram = blank
    parents: list[ScoredProgram] = [blank]
    countdown: int = EVO_EARLY_STOP_COUNTDOWN

    for _ in range(EVO_MAX_GENERATIONS):
        children: list[ScoredProgram] = []
        for monkey in MONKEYS:
            for proposal in monkey(parents, level):
                # Skip anything we've already tried
                source_before_fit: str = canonicalize(proposal, level).source
                if source_before_fit in tried_sources:
                    continue
                tried_sources.add(source_before_fit)
                # A crash just means this program's dropped
                try:
                    child: ScoredProgram = evaluate(proposal, level)
                except (ValueError, ZeroDivisionError, FloatingPointError, OverflowError):
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
        parents = select_parents(population, level)

        generation_best: ScoredProgram = min(children, key=lambda program: program.score)
        if generation_best.score < best.score:
            best = generation_best
            countdown = EVO_EARLY_STOP_COUNTDOWN
        else:
            countdown -= 1
            if countdown == 0:
                break
    return best
