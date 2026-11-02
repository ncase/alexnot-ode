"""Is there ANY setting of the scoring coefficients where the real lynx & hare data gives Lotka-Volterra? Changes nothing in the main solver.

Careful: this picks settings on one dataset, already knowing the answer we want. A hit here is a spark, not proof.

Usage: python solver/grid_lynx.py
"""
from collections import Counter
import itertools
import multiprocessing

import programs
from programs import TIMESERIES_PATH, Level, ScoredProgram, load_level
from rank_intended import INTENDED_PROGRAMS, rank_of, score_directly, short_text
from search import search_population

ACCURACY_COEFFS: list[float] = [2.0, 3.0, 5.0, 7.5, 10.0, 15.0, 25.0, 40.0, 60.0]
TOKEN_COEFFS: list[float] = [0.0, 0.05, 0.1, 0.2, 0.5, 1.0]
PARAMETER_COEFFS: list[float] = [0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0]
PROGRESS_EVERY: int = 50

LEVEL: Level = load_level(TIMESERIES_PATH / 'lynx_hare.json')
LOTKA_VOLTERRA: str = next(iter(INTENDED_PROGRAMS['lotka_volterra']))
# The same structure, but with the predator death rate snapped to exactly 1. It fits to about 1.03, so that's fair
SNAPPED_LOTKA_VOLTERRA: str = 'diff.x += params.a * data.x\ndiff.x -= params.b * data.x * data.y\ndiff.y += params.c * data.x * data.y\ndiff.y -= data.y'
# Also with the two x * y rates tied into one. They fit to 0.030 & 0.029, so that's fair too
TIED_LOTKA_VOLTERRA: str = 'diff.x += params.a * data.x\ndiff.x -= params.b * data.x * data.y\ndiff.y += params.b * data.x * data.y\ndiff.y -= data.y'
FORM_NAMES: dict[str, str] = {LOTKA_VOLTERRA: 'free', SNAPPED_LOTKA_VOLTERRA: 'snapped', TIED_LOTKA_VOLTERRA: 'tied'}


def run_setting(setting: tuple[float, float, float]) -> tuple[tuple[float, float, float], str, dict[str, float], int | None, float]:
    """A setting's winner, its fitted numbers, LV's rank among what got tried, and how far LV is behind the winner if scored directly."""
    # Each worker changes its own copy of these, so nothing outside this script sees them
    programs.SCORE_COEFF_ACCURACY, programs.SCORE_COEFF_TOKEN, programs.SCORE_COEFF_PARAMETER = setting
    population: list[ScoredProgram] = search_population(LEVEL)
    winner: ScoredProgram = min(population, key=lambda program: program.score)
    return setting, winner.source, winner.params[0], rank_of(population, {LOTKA_VOLTERRA})[0], score_directly(LOTKA_VOLTERRA, LEVEL) - winner.score


if __name__ == '__main__':
    # Only the ratios between coefficients matter, so skip the repeats
    settings: dict[tuple[float, float], tuple[float, float, float]] = {}
    for accuracy_coeff, token_coeff, parameter_coeff in itertools.product(ACCURACY_COEFFS, TOKEN_COEFFS, PARAMETER_COEFFS):
        settings.setdefault((round(token_coeff / accuracy_coeff, 6), round(parameter_coeff / accuracy_coeff, 6)), (accuracy_coeff, token_coeff, parameter_coeff))
    print(f'{len(settings)} settings', flush=True)

    results = []
    with multiprocessing.Pool() as pool:
        for result in pool.imap_unordered(run_setting, list(settings.values())):
            results.append(result)
            if len(results) % PROGRESS_EVERY == 0:
                print(f'{len(results)} done, {sum(result[1] in FORM_NAMES for result in results)} hits so far', flush=True)

    solved = sorted((result for result in results if result[1] in FORM_NAMES), key=lambda result: result[0])
    print(f'\n{len(solved)} of {len(results)} settings make Lotka-Volterra win:')
    for setting, winner, winner_params, _, _ in solved:
        print(f'  accuracy {setting[0]:<4} token {setting[1]:<4} parameter {setting[2]:<4} {FORM_NAMES[winner]:8s}' + ' '.join(f'{name} = {value:.3f}' for name, value in winner_params.items()))

    # Would LV have beaten the winner, if only the search had tried it?
    print(f'\nSettings where LV beats the winner but the search missed it: {sum(result[4] < 0 for result in results)}')
    print('Most common winners:')
    for winner, count in Counter(result[1] for result in results).most_common(12):
        print(f'  {count:3d}x {short_text(winner)}')
    print('ALL DONE', flush=True)
