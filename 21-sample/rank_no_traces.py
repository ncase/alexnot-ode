"""When the intended program doesn't win, how close was it? Ranks it among everything the search scored, on the fan's seeds.

"Intended" is checked mechanically: an exact match on the canonical program string, with no LLM or human judging.
The rank only counts programs the search actually tried, so on every loss we also score the intended program directly:
if it beats the winner, that's a search problem. If it doesn't, that's a scoring problem, for now, even if the winner might be a valid answer.
If it exactly ties the winner, the winner's just another spelling of the same equation. That's a synonym, which counts as solved.
Every winner that isn't the intended program gets printed, so a human can judge it.

Goes up through noise levels in order, and stops at the first one where no seed solves. Then updates levels/results/ for the levels it tested.

Usage: python solver/rank_intended.py [--levels bass spring] [--fan-path some/folder] [--coeffs 25 0.1 0.5] [--close-fraction 0.5] [--parents 10]
Needs levels/timeseries/fan/ to exist. (Run levels/generators/generate_fan.py)
"""
import argparse
import multiprocessing
from pathlib import Path
import statistics

import monkeys
import programs
from programs import PARAMETER_PATTERN, TIMESERIES_PATH, Level, Proposal, ScoredProgram, evaluate, load_level
from run_level import run_and_save
import search
from search import SAME_SCORE_TOLERANCE, search_population

NOISE_LABELS: list[str] = ['01', '05', '10', '20']
SEEDS: range = range(20)

# Only this file & the fans know the answers. The search itself never sees these
INTENDED_PROGRAMS: dict[str, set[str]] = {
    'exponential': {'diff.x += params.a * data.x'},
    'logistic': {'diff.x += params.a * data.x\ndiff.x -= params.b * data.x * data.x'},
    # Three spellings of one equation, depending on which parameter the relation replaced
    'bass': {
        'diff.x += params.a\ndiff.x += (params.b - params.a) * data.x\ndiff.x -= params.b * data.x * data.x',
        'diff.x += (params.a - params.b)\ndiff.x += params.b * data.x\ndiff.x -= params.a * data.x * data.x',
        'diff.x += params.a\ndiff.x += params.b * data.x\ndiff.x -= (params.a + params.b) * data.x * data.x',
    },
    'newton': {'diff.x += params.a\ndiff.x -= params.b * data.x'},
    'drag': {'diff.x += params.a\ndiff.x -= params.b * data.x * data.x'},
    'spring': {'diff.x += data.y\ndiff.y -= params.a * data.x\ndiff.y -= params.b * data.y'},
    'lotka_volterra': {'diff.x += params.a * data.x\ndiff.x -= params.b * data.x * data.y\ndiff.y += params.c * data.x * data.y\ndiff.y -= params.d * data.y'},
    'sir': {'diff.x -= params.a * data.x * data.y\ndiff.y += params.a * data.x * data.y\ndiff.y -= params.b * data.y\ndiff.z += params.b * data.y'},
}
# The spring with `x' = a * y`: the same structure, with one extra number that fits to about 1
LOOSE_SPRING: str = 'diff.x += params.a * data.y\ndiff.y -= params.b * data.x\ndiff.y -= params.c * data.y'
# SIR without its ties: the same structure, with 4 separate rates instead of 2
LOOSE_SIR: str = 'diff.x -= params.a * data.x * data.y\ndiff.y += params.b * data.x * data.y\ndiff.y -= params.c * data.y\ndiff.z += params.d * data.y'
LOOSE_PROGRAMS: dict[str, str] = {'spring': LOOSE_SPRING, 'sir': LOOSE_SIR}


def rank_of(population: list[ScoredProgram], intended: set[str]) -> tuple[int | None, float | None, str]:
    """The intended program's rank (1 = won), how many points behind the winner it was, and the winner. Spellings of one equation share a rank."""
    ranked: list[ScoredProgram] = sorted(population, key=lambda program: program.score)
    for index, program in enumerate(ranked):
        if program.source in intended:
            return index + 1, program.score - ranked[0].score, ranked[0].source
    return None, None, ranked[0].source


def score_directly(source: str, level: Level) -> float:
    """Fit & score a program, whether or not the search ever got there. Its parameters are all volume knobs, so any starting values will do."""
    names: list[str] = list(dict.fromkeys(PARAMETER_PATTERN.findall(source)))
    return evaluate(Proposal(source, [{name: 1.0 for name in names} for _ in level.demos]), level).score


def diagnose(population: list[ScoredProgram], intended: set[str], level: Level) -> tuple[str, float]:
    """The verdict, and how many points the intended program's score is above the winner's (negative means it beat the winner).

    'solved', 'synonym' (the winner's a different spelling, with the same score), 'search problem' (the intended program beats the winner, but wasn't found),
    or 'scoring problem' (the winner really does score better).
    """
    winner: ScoredProgram = min(population, key=lambda program: program.score)
    intended_score: float = min(score_directly(source, level) for source in intended)
    gap: float = intended_score - winner.score
    if winner.source in intended:
        return 'solved', gap
    if abs(gap) <= SAME_SCORE_TOLERANCE:
        return 'synonym', gap
    return ('search problem' if gap < 0 else 'scoring problem'), gap


def short_text(source: str) -> str:
    """A program on one line, without the noise."""
    return source.replace('diff.', '').replace('params.', '').replace('data.', '').replace('\n', ' | ') or '(blank program)'


def run_job(job: tuple[str, str, int, Path, tuple[float, float, float], float, int]) -> tuple[int | None, float | None, str, int | None, str, float]:
    level_name, noise_label, seed, fan_path, coeffs, close_fraction, parents_top_k = job
    programs.SCORE_COEFF_ACCURACY, programs.SCORE_COEFF_TOKEN, programs.SCORE_COEFF_PARAMETER = coeffs
    monkeys.CLOSE_FRACTION = close_fraction
    search.PARENTS_TOP_K = parents_top_k
    level: Level = load_level(fan_path / f'{level_name}_noise{noise_label}_seed{seed:02d}.json')
    population: list[ScoredProgram] = search_population(level)
    rank, margin, winner = rank_of(population, INTENDED_PROGRAMS[level_name])
    # Also rank the looser form, counting either as right
    loose_rank: int | None = rank_of(population, INTENDED_PROGRAMS[level_name] | {LOOSE_PROGRAMS[level_name]})[0] if level_name in LOOSE_PROGRAMS else None
    return rank, margin, winner, loose_rank, *diagnose(population, INTENDED_PROGRAMS[level_name], level)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--levels', nargs='+', default=list(INTENDED_PROGRAMS))
    parser.add_argument('--fan-path', type=Path, default=TIMESERIES_PATH / 'fan')
    parser.add_argument('--coeffs', nargs=3, type=float, default=[programs.SCORE_COEFF_ACCURACY, programs.SCORE_COEFF_TOKEN, programs.SCORE_COEFF_PARAMETER])
    parser.add_argument('--close-fraction', type=float, default=monkeys.CLOSE_FRACTION)
    parser.add_argument('--parents', type=int, default=search.PARENTS_TOP_K)
    arguments = parser.parse_args()

    with multiprocessing.Pool() as pool:
        for level_name in arguments.levels:
            for noise_label in NOISE_LABELS:
                jobs = [(level_name, noise_label, seed, arguments.fan_path, tuple(arguments.coeffs), arguments.close_fraction, arguments.parents) for seed in SEEDS]
                results = pool.map(run_job, jobs)
                ranks: list[int | None] = [result[0] for result in results]
                margins: list[float] = [result[1] for result in results if result[0] is not None and result[0] > 1]
                verdicts: list[str] = [result[4] for result in results]
                counts: dict[str, int] = {
                    '#1': ranks.count(1), '#2': ranks.count(2), '#3': ranks.count(3),
                    '#4-10': sum(rank is not None and 4 <= rank <= 10 for rank in ranks),
                    '#11+': sum(rank is not None and rank > 10 for rank in ranks),
                    'never tried': ranks.count(None),
                }
                margin_text: str = f'  behind by median {statistics.median(margins):.1f}, worst {max(margins):.1f}' if margins else ''
                solved_count: int = verdicts.count('solved') + verdicts.count('synonym')
                line: str = f"{level_name:15s} {noise_label}%: solved {solved_count:2d}/{len(SEEDS)} (synonyms {verdicts.count('synonym')}), search problem {verdicts.count('search problem')}, scoring problem {verdicts.count('scoring problem')}  | " + ' '.join(f'{label}:{count}' for label, count in counts.items()) + margin_text
                if level_name in LOOSE_PROGRAMS:
                    line += f"  (top 1 with loose form too: {sum(result[3] == 1 for result in results)})"
                print(line, flush=True)
                # The winners that aren't the intended program, most common first. Some of these might be valid answers!
                false_winners: dict[tuple[str, str], list[float]] = {}
                for result in results:
                    if result[4] != 'solved':
                        false_winners.setdefault((result[4], result[2]), []).append(result[5])
                for (verdict, winner), gaps in sorted(false_winners.items(), key=lambda item: -len(item[1])):
                    print(f"    false winner {len(gaps):2d}x, {verdict}, intended is {statistics.median(gaps):+.2f} from it: {short_text(winner)}", flush=True)
                # If this noise level never solves, more noise isn't going to help
                if solved_count == 0:
                    print(f'{level_name:15s} stopping: nothing solved at {noise_label}%', flush=True)
                    break

