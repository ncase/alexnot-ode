"""Damped spring: x' = y, y' = -stiffness * x - damping * y. Writes levels/timeseries/spring.json.

x is position and y is velocity. Measuring velocity directly is a cheat, but it's noisy like everything else.
"""
import numpy as np

from common import make_demo, plot_level, write_level

NOISE_FRACTION: float = 0.10
SEED: int = 0
VARIABLE_NAMES: list[str] = ['x', 'y']

# Specifically chosen to differ: a textbook spring, a loose one, and a stiff one.
# Each end time shows about 2 wobbles. Any more, and a coarser time step adds its own error, which extra terms overfit
DEMO_SETTINGS: list[dict] = [
    {'stiffness': 4.0, 'damping': 0.4, 'start': [1.0, 0.0], 'end_time': 8.0},
    {'stiffness': 1.5, 'damping': 0.25, 'start': [0.0, 2.0], 'end_time': 12.0},
    {'stiffness': 9.0, 'damping': 0.6, 'start': [2.0, -1.0], 'end_time': 4.0},
]


def make_spring_demo(stiffness: float, damping: float, start: list[float], end_time: float, noise_fraction: float, rng: np.random.Generator) -> dict:
    return make_demo(
        f"x' = y, y' = -{stiffness}x - {damping}y",
        lambda time, state: [state[1], -stiffness * state[0] - damping * state[1]],
        start, end_time, noise_fraction, rng,
    )


def build_demos(noise_fraction: float, seed: int) -> list[dict]:
    rng: np.random.Generator = np.random.default_rng(seed)
    return [make_spring_demo(**settings, noise_fraction=noise_fraction, rng=rng) for settings in DEMO_SETTINGS]


if __name__ == '__main__':
    demos: list[dict] = build_demos(NOISE_FRACTION, SEED)
    write_level('spring', VARIABLE_NAMES, demos)
    plot_level('spring', VARIABLE_NAMES, demos, NOISE_FRACTION)
