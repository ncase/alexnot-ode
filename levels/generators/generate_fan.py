"""Write many noisy copies of each level to levels/timeseries/fan/, for fanning the scoring coefficients."""
import bass
import drag
import exponential
import logistic
import lotka_volterra
import newton
import sir
import spring
from common import TIMESERIES_PATH, write_level

NOISE_FRACTIONS: list[float] = [0.05, 0.10, 0.20]
SEED_COUNT: int = 40

for level_name, module in [('exponential', exponential), ('logistic', logistic), ('bass', bass), ('newton', newton), ('drag', drag), ('spring', spring), ('lotka_volterra', lotka_volterra), ('sir', sir)]:
    for noise_fraction in NOISE_FRACTIONS:
        for seed in range(SEED_COUNT):
            output_path = TIMESERIES_PATH / 'fan' / f'{level_name}_noise{noise_fraction * 100:02.0f}_seed{seed:02d}.json'
            write_level(level_name, module.VARIABLE_NAMES, module.build_demos(noise_fraction, seed), output_path)
