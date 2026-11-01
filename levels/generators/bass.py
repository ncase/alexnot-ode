"""Bass level: x' = (ads + word_of_mouth * x)(1 - x) = ads + (word_of_mouth - ads)x - word_of_mouth * x². Writes levels/timeseries/bass.json.

x is the fraction of people who've adopted, so it starts at 0, where logistic growth would stay stuck forever.
"""
import numpy as np

from common import make_demo, plot_level, write_level

NOISE_FRACTION: float = 0.10
SEED: int = 0
VARIABLE_NAMES: list[str] = ['x']

# The baseline's the average from Mahajan, Muller & Bass 1995. The others keep word of mouth there, and change the ads:
# very weak ads make word of mouth's early acceleration obvious, and strong ads make the ads themselves obvious.
# All the end times are picked so the demo shows the whole curve, up to saturation
DEMO_SETTINGS: list[dict[str, float]] = [
    {'ads': 0.03, 'word_of_mouth': 0.38, 'end_time': 19.5},
    {'ads': 0.003, 'word_of_mouth': 0.38, 'end_time': 25.0},
    {'ads': 0.3, 'word_of_mouth': 0.38, 'end_time': 11.8},
]


def make_bass_demo(ads: float, word_of_mouth: float, end_time: float, noise_fraction: float, rng: np.random.Generator) -> dict:
    return make_demo(
        f"x' = ({ads} + {word_of_mouth}x)(1 - x)",
        lambda time, state: [(ads + word_of_mouth * state[0]) * (1 - state[0])],
        [0.0], end_time, noise_fraction, rng,
    )


def build_demos(noise_fraction: float, seed: int) -> list[dict]:
    rng: np.random.Generator = np.random.default_rng(seed)
    return [make_bass_demo(**settings, noise_fraction=noise_fraction, rng=rng) for settings in DEMO_SETTINGS]


if __name__ == '__main__':
    demos: list[dict] = build_demos(NOISE_FRACTION, SEED)
    write_level('bass', VARIABLE_NAMES, demos)
    plot_level('bass', VARIABLE_NAMES, demos, NOISE_FRACTION)
