"""Lotka-Volterra: x' = prey_growth * x - predation * xy, y' = predator_growth * xy - predator_death * y. Writes levels/timeseries/lotka_volterra.json.

x is prey and y is predators.
"""
import numpy as np

from common import make_demo, plot_level, write_level

NOISE_FRACTION: float = 0.10
SEED: int = 0
VARIABLE_NAMES: list[str] = ['x', 'y']

# Specifically chosen to differ, with no coefficients all near 1 or tied to each other.
# Each end time shows about 1.5 cycles, which last about 2 * pi / sqrt(prey_growth * predator_death).
# Any more, and a coarser time step adds its own error, which extra terms overfit
DEMO_SETTINGS: list[dict] = [
    {'prey_growth': 1.1, 'predation': 0.1, 'predator_growth': 0.075, 'predator_death': 1.5, 'start': [10.0, 5.0], 'end_time': 8.0},
    {'prey_growth': 0.6, 'predation': 0.05, 'predator_growth': 0.02, 'predator_death': 0.8, 'start': [20.0, 5.0], 'end_time': 12.0},
    {'prey_growth': 2.0, 'predation': 0.3, 'predator_growth': 0.1, 'predator_death': 0.7, 'start': [5.0, 2.0], 'end_time': 8.0},
]


def make_lotka_volterra_demo(
    prey_growth: float, predation: float, predator_growth: float, predator_death: float,
    start: list[float], end_time: float, noise_fraction: float, rng: np.random.Generator,
) -> dict:
    return make_demo(
        f"x' = {prey_growth}x - {predation}xy, y' = {predator_growth}xy - {predator_death}y",
        lambda time, state: [
            prey_growth * state[0] - predation * state[0] * state[1],
            predator_growth * state[0] * state[1] - predator_death * state[1],
        ],
        start, end_time, noise_fraction, rng,
    )


def build_demos(noise_fraction: float, seed: int) -> list[dict]:
    rng: np.random.Generator = np.random.default_rng(seed)
    return [make_lotka_volterra_demo(**settings, noise_fraction=noise_fraction, rng=rng) for settings in DEMO_SETTINGS]


if __name__ == '__main__':
    demos: list[dict] = build_demos(NOISE_FRACTION, SEED)
    write_level('lotka_volterra', VARIABLE_NAMES, demos)
    plot_level('lotka_volterra', VARIABLE_NAMES, demos, NOISE_FRACTION)
