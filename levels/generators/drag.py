"""Falling with air drag: x' = gravity - drag * x². Writes levels/timeseries/drag.json.

x is falling speed. Drag's quadratic because going twice as fast means hitting twice as much air, twice as hard.
"""
import numpy as np

from common import make_demo, plot_level, write_level

NOISE_FRACTION: float = 0.10
SEED: int = 0
VARIABLE_NAMES: list[str] = ['x']

# Specifically chosen to differ: a skydiver speeding up, a parachute opening so the speed drops, and a probe falling on Mars.
# Each end time's picked so the speed gets close to terminal velocity, which is sqrt(gravity / drag).
# The parachute's time range is short because a coarser time step adds its own error, and extra terms overfit that
DEMO_SETTINGS: list[dict[str, float]] = [
    {'gravity': 9.8, 'drag': 0.004, 'start': 0.0, 'end_time': 15.0},
    {'gravity': 9.8, 'drag': 0.05, 'start': 50.0, 'end_time': 3.0},
    {'gravity': 3.7, 'drag': 0.02, 'start': 0.0, 'end_time': 12.0},
]


def make_drag_demo(gravity: float, drag: float, start: float, end_time: float, noise_fraction: float, rng: np.random.Generator) -> dict:
    return make_demo(
        f"x' = {gravity} - {drag}x², start {start:g}",
        lambda time, state: [gravity - drag * state[0]**2],
        [start], end_time, noise_fraction, rng,
    )


def build_demos(noise_fraction: float, seed: int) -> list[dict]:
    rng: np.random.Generator = np.random.default_rng(seed)
    return [make_drag_demo(**settings, noise_fraction=noise_fraction, rng=rng) for settings in DEMO_SETTINGS]


if __name__ == '__main__':
    demos: list[dict] = build_demos(NOISE_FRACTION, SEED)
    write_level('drag', VARIABLE_NAMES, demos)
    plot_level('drag', VARIABLE_NAMES, demos, NOISE_FRACTION)
