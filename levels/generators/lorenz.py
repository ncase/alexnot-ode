"""Lorenz: x' = sigma * (y - x), y' = rho * x - xz - y, z' = xy - beta * z. Writes levels/timeseries/lorenz.json.

The classic chaotic butterfly! Three variables, seven terms, and two of those terms have no parameter at all.
"""
import numpy as np

from common import make_demo, plot_level, write_level

NOISE_FRACTION: float = 0.10
SEED: int = 0
VARIABLE_NAMES: list[str] = ['x', 'y', 'z']

# Specifically chosen to differ, and all chaotic. Short end times, since it moves fast & each demo only gets 50 samples
DEMO_SETTINGS: list[dict] = [
    {'sigma': 10.0, 'rho': 28.0, 'beta': 8 / 3, 'start': [-8.0, 8.0, 27.0], 'end_time': 2.0},
    {'sigma': 14.0, 'rho': 35.0, 'beta': 2.0, 'start': [5.0, 10.0, 20.0], 'end_time': 2.0},
    {'sigma': 8.0, 'rho': 40.0, 'beta': 3.5, 'start': [10.0, -5.0, 35.0], 'end_time': 2.0},
]


def make_lorenz_demo(sigma: float, rho: float, beta: float, start: list[float], end_time: float, noise_fraction: float, rng: np.random.Generator) -> dict:
    return make_demo(
        f"x' = {sigma}(y - x), y' = {rho}x - xz - y, z' = xy - {beta:.3f}z",
        lambda time, state: [
            sigma * (state[1] - state[0]),
            rho * state[0] - state[0] * state[2] - state[1],
            state[0] * state[1] - beta * state[2],
        ],
        start, end_time, noise_fraction, rng,
    )


def build_demos(noise_fraction: float, seed: int) -> list[dict]:
    rng: np.random.Generator = np.random.default_rng(seed)
    return [make_lorenz_demo(**settings, noise_fraction=noise_fraction, rng=rng) for settings in DEMO_SETTINGS]


if __name__ == '__main__':
    demos: list[dict] = build_demos(NOISE_FRACTION, SEED)
    write_level('lorenz', VARIABLE_NAMES, demos)
    plot_level('lorenz', VARIABLE_NAMES, demos, NOISE_FRACTION)
