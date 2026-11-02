"""Mechanically fan the scoring coefficients: how often does each setting recover the right structural form?

Seeds 0-19 are for choosing a setting, and seeds 20-39 are held out, to check we didn't just tune to noise.
Needs levels/timeseries/fan/ to exist. (Run levels/generators/generate_fan.py)
"""
import itertools
import multiprocessing

import programs
from programs import TIMESERIES_PATH, Level, load_level, split_line
from search import search

ACCURACY_COEFFS: list[float] = [5.0, 7.5, 12.5, 25.0, 37.5, 50.0]
TOKEN_COEFFS: list[float] = [0.0, 0.1, 0.25, 0.5, 1.0]
PARAMETER_COEFFS: list[float] = [0.0, 0.5, 1.0, 2.0, 4.0]
NOISE_LABELS: list[str] = ['05', '10', '20']
TUNING_SEEDS: range = range(20)
HOLDOUT_SEEDS: range = range(20, 40)
ROWS_TO_PRINT: int = 25

# Only this fan knows the answers. The search itself never sees these
RIGHT_PROGRAMS: dict[str, str] = {
    'exponential': 'diff.x += params.a * data.x',
    'logistic': 'diff.x += params.a * data.x\ndiff.x -= params.b * data.x * data.x',
}

levels: dict[tuple[str, str, int], Level] = {}


def load_levels() -> None:
    """Runs once in each worker process."""
    for level_name, noise_label, seed in itertools.product(RIGHT_PROGRAMS, NOISE_LABELS, itertools.chain(TUNING_SEEDS, HOLDOUT_SEEDS)):
        levels[level_name, noise_label, seed] = load_level(TIMESERIES_PATH / 'fan' / f'{level_name}_noise{noise_label}_seed{seed:02d}.json')


def term_set(source: str) -> set[tuple[str, str]]:
    """Which terms a program has, on which variables, ignoring signs & parameter names."""
    return {(split_line(line)[0], split_line(line)[2]) for line in source.splitlines()}


def run_setting(setting: tuple[float, float, float]) -> tuple[tuple[float, float, float], dict[tuple[str, str], tuple[int, int, int]]]:
    """For each level & noise: how many right on tuning seeds, how many right on held-out seeds, and how many overfit (all seeds)."""
    # The scorer reads these constants at call time
    programs.SCORE_COEFF_ACCURACY, programs.SCORE_COEFF_TOKEN, programs.SCORE_COEFF_PARAMETER = setting
    cells: dict[tuple[str, str], tuple[int, int, int]] = {}
    for level_name, noise_label in itertools.product(RIGHT_PROGRAMS, NOISE_LABELS):
        right_source: str = RIGHT_PROGRAMS[level_name]
        right_terms: set[tuple[str, str]] = term_set(right_source)
        winners: dict[int, str] = {
            seed: search(levels[level_name, noise_label, seed]).source for seed in itertools.chain(TUNING_SEEDS, HOLDOUT_SEEDS)
        }
        right_tuning: int = sum(winners[seed] == right_source for seed in TUNING_SEEDS)
        right_holdout: int = sum(winners[seed] == right_source for seed in HOLDOUT_SEEDS)
        # Overfit = every right term, plus extras
        overfit: int = sum(term_set(source) > right_terms for source in winners.values())
        cells[level_name, noise_label] = (right_tuning, right_holdout, overfit)
    return setting, cells


if __name__ == '__main__':
    # Only the ratios between coefficients matter, since doubling all three picks the same winner. So skip the repeats
    settings: dict[tuple[float, float], tuple[float, float, float]] = {}
    for accuracy_coeff, token_coeff, parameter_coeff in itertools.product(ACCURACY_COEFFS, TOKEN_COEFFS, PARAMETER_COEFFS):
        settings.setdefault((round(token_coeff / accuracy_coeff, 6), round(parameter_coeff / accuracy_coeff, 6)), (accuracy_coeff, token_coeff, parameter_coeff))

    with multiprocessing.Pool(initializer=load_levels) as pool:
        results = pool.map(run_setting, list(settings.values()))

    def total_right(cells: dict[tuple[str, str], tuple[int, int, int]]) -> int:
        return sum(right_tuning for right_tuning, _, _ in cells.values())

    print(f'{len(settings)} settings. Each cell: right on tuning seeds/right on held-out seeds, out of {len(TUNING_SEEDS)} each, then overfit out of {len(TUNING_SEEDS) + len(HOLDOUT_SEEDS)}\n')
    for setting, cells in sorted(results, key=lambda result: -total_right(result[1]))[:ROWS_TO_PRINT]:
        row: str = '  '.join(f'{level_name[:3]}{noise_label}: {tuning:2d}/{holdout:2d} o{overfit:<2d}' for (level_name, noise_label), (tuning, holdout, overfit) in cells.items())
        print(f'{total_right(cells):3d}  accuracy {setting[0]:<4} token {setting[1]:<4} parameter {setting[2]:<3}  {row}')
