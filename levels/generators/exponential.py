"""Exponential level: x' = rate * x. Writes levels/timeseries/exponential.json."""
import numpy as np

from common import make_demo, plot_level, write_level

NOISE_FRACTION: float = 0.10
SEED: int = 0
VARIABLE_NAMES: list[str] = ['x']

# Specifically chosen to differ, so nothing can tie or relate by accident. One decays, so a single program must fit both directions
DEMO_SETTINGS: list[dict[str, float]] = [
    {'rate': 0.3, 'start': 1.0, 'end_time': 10.0},
    {'rate': -0.5, 'start': 10.0, 'end_time': 10.0},
    {'rate': 0.15, 'start': 3.0, 'end_time': 15.0},
]


def make_exponential_demo(rate: float, start: float, end_time: float, noise_fraction: float, rng: np.random.Generator) -> dict:
    return make_demo(f"x' = {rate}x", lambda time, state: [rate * state[0]], [start], end_time, noise_fraction, rng)


def build_demos(noise_fraction: float, seed: int) -> list[dict]:
    rng: np.random.Generator = np.random.default_rng(seed)
    return [make_exponential_demo(**settings, noise_fraction=noise_fraction, rng=rng) for settings in DEMO_SETTINGS]


if __name__ == '__main__':
    demos: list[dict] = build_demos(NOISE_FRACTION, SEED)
    write_level('exponential', VARIABLE_NAMES, demos)
    plot_level('exponential', VARIABLE_NAMES, demos, NOISE_FRACTION)
