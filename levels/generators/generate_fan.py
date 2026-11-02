"""Write many noisy copies of each level to levels/timeseries/fan/, for fanning the scoring coefficients.

Usage: python levels/generators/generate_fan.py [--sample-count 20 --output-path levels/timeseries/fan_samples20]
"""
import argparse
from pathlib import Path

import bass
import common
import drag
import exponential
import logistic
import lorenz
import lotka_volterra
import newton
import sir
import spring
from common import TIMESERIES_PATH, write_level

# 1% is a sanity check: with almost perfect data, a level should definitely solve
NOISE_FRACTIONS: list[float] = [0.01, 0.05, 0.10, 0.20]
SEED_COUNT: int = 40

parser = argparse.ArgumentParser()
parser.add_argument('--sample-count', type=int, default=common.DEFAULT_SAMPLE_COUNT)
parser.add_argument('--output-path', type=Path, default=TIMESERIES_PATH / 'fan')
arguments = parser.parse_args()
# Samples per demo. The end times stay the same, so fewer samples means bigger gaps between them
common.DEFAULT_SAMPLE_COUNT = arguments.sample_count

for level_name, module in [('exponential', exponential), ('logistic', logistic), ('bass', bass), ('newton', newton), ('drag', drag), ('spring', spring), ('lotka_volterra', lotka_volterra), ('sir', sir), ('lorenz', lorenz)]:
    for noise_fraction in NOISE_FRACTIONS:
        for seed in range(SEED_COUNT):
            output_path = arguments.output_path / f'{level_name}_noise{noise_fraction * 100:02.0f}_seed{seed:02d}.json'
            write_level(level_name, module.VARIABLE_NAMES, module.build_demos(noise_fraction, seed), output_path)
