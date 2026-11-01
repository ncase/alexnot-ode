"""Logistic level: x' = rate * x - (rate / capacity) * x^2. Writes levels/timeseries/logistic.json."""
import numpy as np

from common import make_demo, plot_level, write_level

NOISE_FRACTION: float = 0.10
SEED: int = 0
VARIABLE_NAMES: list[str] = ['x']

# Specifically chosen to differ, so nothing can tie or relate by accident. Each span shows the whole S-curve
DEMO_SETTINGS: list[dict[str, float]] = [
    {'rate': 0.8, 'capacity': 10.0, 'start': 0.5, 'end_time': 12.0},
    {'rate': 0.5, 'capacity': 30.0, 'start': 2.0, 'end_time': 18.0},
    {'rate': 1.2, 'capacity': 4.0, 'start': 0.2, 'end_time': 8.0},
]


def make_logistic_demo(rate: float, capacity: float, start: float, end_time: float, noise_fraction: float, rng: np.random.Generator) -> dict:
    squared_coefficient: float = rate / capacity
    return make_demo(
        f"x' = {rate}x - {squared_coefficient:.3g}x²",
        lambda time, state: [rate * state[0] - squared_coefficient * state[0]**2],
        [start], end_time, noise_fraction, rng,
    )


def build_demos(noise_fraction: float, seed: int) -> list[dict]:
    rng: np.random.Generator = np.random.default_rng(seed)
    return [make_logistic_demo(**settings, noise_fraction=noise_fraction, rng=rng) for settings in DEMO_SETTINGS]


if __name__ == '__main__':
    demos: list[dict] = build_demos(NOISE_FRACTION, SEED)
    write_level('logistic', VARIABLE_NAMES, demos)
    plot_level('logistic', VARIABLE_NAMES, demos, NOISE_FRACTION)
