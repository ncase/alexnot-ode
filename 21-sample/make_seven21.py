"""The other 7 levels with 21 samples per demo, for all 4 noise levels & 20 seeds. Writes only to the scratchpad."""
from pathlib import Path

import bass
import common
import drag
import exponential
import logistic
import newton
import sir
import spring
from common import write_level

OUTPUT_PATH: Path = Path(__file__).parent / 'seven21'
NOISE_FRACTIONS: list[float] = [0.01, 0.05, 0.10, 0.20]
SEED_COUNT: int = 20

common.DEFAULT_SAMPLE_COUNT = 21

for level_name, module in [('exponential', exponential), ('logistic', logistic), ('bass', bass), ('newton', newton), ('drag', drag), ('spring', spring), ('sir', sir)]:
    for noise_fraction in NOISE_FRACTIONS:
        for seed in range(SEED_COUNT):
            output_path: Path = OUTPUT_PATH / f'{level_name}_noise{noise_fraction * 100:02.0f}_seed{seed:02d}.json'
            write_level(level_name, module.VARIABLE_NAMES, module.build_demos(noise_fraction, seed), output_path)
