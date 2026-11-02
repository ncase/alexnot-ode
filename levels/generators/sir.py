"""SIR epidemic: x' = -infection * xy, y' = infection * xy - recovery * y, z' = recovery * y. Writes levels/timeseries/sir.json.

x is susceptible, y is infected and z is recovered, each as a fraction of everyone, so they always add up to 1 (before noise).
"""
import numpy as np

from common import make_demo, plot_level, write_level

NOISE_FRACTION: float = 0.10
SEED: int = 0
VARIABLE_NAMES: list[str] = ['x', 'y', 'z']

# Specifically chosen to differ, with no rates near 1 or tied to each other.
# Each end time shows one whole epidemic, from first cases to nearly over
DEMO_SETTINGS: list[dict] = [
    {'infection': 0.5, 'recovery': 0.1, 'start': [0.99, 0.01, 0.0], 'end_time': 60.0},
    {'infection': 0.3, 'recovery': 0.05, 'start': [0.95, 0.05, 0.0], 'end_time': 100.0},
    {'infection': 0.8, 'recovery': 0.25, 'start': [0.98, 0.02, 0.0], 'end_time': 35.0},
]


def make_sir_demo(infection: float, recovery: float, start: list[float], end_time: float, noise_fraction: float, rng: np.random.Generator) -> dict:
    return make_demo(
        f"x' = -{infection}xy, y' = {infection}xy - {recovery}y, z' = {recovery}y",
        lambda time, state: [
            -infection * state[0] * state[1],
            infection * state[0] * state[1] - recovery * state[1],
            recovery * state[1],
        ],
        start, end_time, noise_fraction, rng,
    )


def build_demos(noise_fraction: float, seed: int) -> list[dict]:
    rng: np.random.Generator = np.random.default_rng(seed)
    return [make_sir_demo(**settings, noise_fraction=noise_fraction, rng=rng) for settings in DEMO_SETTINGS]


if __name__ == '__main__':
    demos: list[dict] = build_demos(NOISE_FRACTION, SEED)
    write_level('sir', VARIABLE_NAMES, demos)
    plot_level('sir', VARIABLE_NAMES, demos, NOISE_FRACTION)
