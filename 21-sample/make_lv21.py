"""Synthetic LV with 21 samples per demo, like the real data: once with all 3 demos, and once per single demo. Writes only to the scratchpad."""
from pathlib import Path

import common
import lotka_volterra
from common import write_level

OUTPUT_PATH: Path = Path(__file__).parent / 'lv21'
NOISE_FRACTIONS: list[float] = [0.01, 0.05, 0.10, 0.20]
SEED_COUNT: int = 20

common.DEFAULT_SAMPLE_COUNT = 21

for noise_fraction in NOISE_FRACTIONS:
    for seed in range(SEED_COUNT):
        file_name: str = f'lotka_volterra_noise{noise_fraction * 100:02.0f}_seed{seed:02d}.json'
        demos: list[dict] = lotka_volterra.build_demos(noise_fraction, seed)
        write_level('lotka_volterra', lotka_volterra.VARIABLE_NAMES, demos, OUTPUT_PATH / 'three_demos' / file_name)
        # Real LV only has one demo, so each demo also gets a turn alone
        for index, demo in enumerate(demos):
            write_level('lotka_volterra', lotka_volterra.VARIABLE_NAMES, [demo], OUTPUT_PATH / f'demo{index}_only' / file_name)
