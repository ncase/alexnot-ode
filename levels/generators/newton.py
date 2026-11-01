"""Newton's law of cooling: x' = rate * (room - x) = rate * room - rate * x. Writes levels/timeseries/newton.json.

Heating & cooling are the same equation! The only difference is whether x starts above or below the room.
"""
import numpy as np

from common import make_demo, plot_level, write_level

NOISE_FRACTION: float = 0.10
SEED: int = 0
VARIABLE_NAMES: list[str] = ['x']

# Specifically chosen to differ: coffee cooling, something cooling in a fridge, and a cold drink warming up.
# Each end time's about 4.5 / rate, so all the demos get close to the set point
DEMO_SETTINGS: list[dict[str, float]] = [
    {'rate': 0.3, 'room': 20.0, 'start': 90.0, 'end_time': 15.0},
    {'rate': 0.15, 'room': 5.0, 'start': 60.0, 'end_time': 30.0},
    {'rate': 0.5, 'room': 22.0, 'start': 4.0, 'end_time': 9.0},
]


def make_newton_demo(rate: float, room: float, start: float, end_time: float, noise_fraction: float, rng: np.random.Generator) -> dict:
    return make_demo(
        f"x' = {rate}({room:g} - x), start {start:g}",
        lambda time, state: [rate * (room - state[0])],
        [start], end_time, noise_fraction, rng,
    )


def build_demos(noise_fraction: float, seed: int) -> list[dict]:
    rng: np.random.Generator = np.random.default_rng(seed)
    return [make_newton_demo(**settings, noise_fraction=noise_fraction, rng=rng) for settings in DEMO_SETTINGS]


if __name__ == '__main__':
    demos: list[dict] = build_demos(NOISE_FRACTION, SEED)
    write_level('newton', VARIABLE_NAMES, demos)
    plot_level('newton', VARIABLE_NAMES, demos, NOISE_FRACTION)
