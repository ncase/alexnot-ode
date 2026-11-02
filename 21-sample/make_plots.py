"""Plots of the levels that did well with 21 samples at 20% noise, on the same data as data/. Writes to 21-sample/plots/.

Usage: PYTHONPATH=levels/generators python 21-sample/make_plots.py
"""
from pathlib import Path

import common
import exponential
import lotka_volterra
import newton
import sir
from common import plot_level

NOISE_FRACTION: float = 0.20
SEED: int = 0  # Same data as data/*_noise20_seed00.json

common.DEFAULT_SAMPLE_COUNT = 21
# Keeps these apart from the main 50-sample plots in levels/plots/
common.PLOTS_PATH = Path(__file__).parent / 'plots'

for level_name, module in [('exponential', exponential), ('newton', newton), ('lotka_volterra', lotka_volterra), ('sir', sir)]:
    plot_level(level_name, module.VARIABLE_NAMES, module.build_demos(NOISE_FRACTION, SEED), NOISE_FRACTION)
