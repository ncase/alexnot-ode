"""Which scoring coefficients make the search find Lotka-Volterra on the REAL lynx & hare data?

Careful: this tunes settings on the same single dataset they're judged on, against an answer we already know.
So look at how MUCH of the grid solves it, and check any winning setting on the synthetic levels. (solver/rank_intended.py --coeffs)

Usage: python solver/fan_lynx.py
"""
from collections import Counter
import itertools
import multiprocessing

from fan_scoring import ACCURACY_COEFFS, PARAMETER_COEFFS, TOKEN_COEFFS
import programs
from programs import TIMESERIES_PATH, Level, ScoredProgram, load_level
from rank_intended import INTENDED_PROGRAMS, rank_of
from search import search_population

LOTKA_VOLTERRA: set[str] = INTENDED_PROGRAMS['lotka_volterra']
# The same structure, but the search snapped the predator death rate to exactly 1
SNAPPED_LOTKA_VOLTERRA: str = 'diff.x += params.a * data.x\ndiff.x -= params.b * data.x * data.y\ndiff.y += params.c * data.x * data.y\ndiff.y -= data.y'
LEVEL: Level = load_level(TIMESERIES_PATH / 'lynx_hare.json')


def run_setting(setting: tuple[float, float, float]) -> tuple[tuple[float, float, float], int | None, float | None, str, dict[str, float]]:
    programs.SCORE_COEFF_ACCURACY, programs.SCORE_COEFF_TOKEN, programs.SCORE_COEFF_PARAMETER = setting
    population: list[ScoredProgram] = search_population(LEVEL)
    # The winner's fitted numbers, so we can see if they look sensible
    winner_params: dict[str, float] = min(population, key=lambda program: program.score).params[0]
    return (setting, *rank_of(population, LOTKA_VOLTERRA), winner_params)


if __name__ == '__main__':
    print('Current setting:')
    setting, rank, margin, winner, _ = run_setting((programs.SCORE_COEFF_ACCURACY, programs.SCORE_COEFF_TOKEN, programs.SCORE_COEFF_PARAMETER))
    print(f'  Lotka-Volterra rank {rank}, behind by {margin}\n  winner: {winner.replace(chr(10), " | ")}\n')

    # Only the ratios between coefficients matter, so skip the repeats
    settings: dict[tuple[float, float], tuple[float, float, float]] = {}
    for accuracy_coeff, token_coeff, parameter_coeff in itertools.product(ACCURACY_COEFFS, TOKEN_COEFFS, PARAMETER_COEFFS):
        settings.setdefault((round(token_coeff / accuracy_coeff, 6), round(parameter_coeff / accuracy_coeff, 6)), (accuracy_coeff, token_coeff, parameter_coeff))

    with multiprocessing.Pool() as pool:
        results = pool.map(run_setting, list(settings.values()))

    solved = [result for result in results if result[3] in LOTKA_VOLTERRA or result[3] == SNAPPED_LOTKA_VOLTERRA]
    print(f'{len(solved)} of {len(results)} settings make Lotka-Volterra win, counting a death rate snapped to 1:')
    for setting, _, _, winner, winner_params in solved:
        form: str = 'free' if winner in LOTKA_VOLTERRA else 'snapped'
        print(f'  accuracy {setting[0]:<4} token {setting[1]:<4} parameter {setting[2]:<3} {form:8s}' + ' '.join(f'{name} = {value:.3f}' for name, value in winner_params.items()))

    rank_counts: Counter = Counter('never tried' if rank is None else '#1' if rank == 1 else '#2-3' if rank <= 3 else '#4-10' if rank <= 10 else '#11+' for _, rank, _, _, _ in results)
    print(f'\nLotka-Volterra ranks across all settings: {dict(rank_counts)}')
    print('\nMost common winners:')
    for winner, count in Counter(result[3] for result in results).most_common(8):
        print(f'  {count:3d}x {winner.replace(chr(10), " | ") or "(blank program)"}')
