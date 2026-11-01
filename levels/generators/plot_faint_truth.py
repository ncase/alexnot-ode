"""Logistic at 20% noise, with the truth almost invisible: would even a human fail to see the equation?"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import logistic
from common import COLORS, GRID, INK, MUTED, PLOTS_PATH, SURFACE

NOISE_FRACTION: float = 0.20
SEED: int = 0  # Same data as levels/timeseries/fan/logistic_noise20_seed00.json
TRUTH_OPACITY: float = 0.12  # Almost invisible, so your eye reads the dots first

demos: list[dict] = logistic.build_demos(NOISE_FRACTION, SEED)
figure, axes = plt.subplots(1, len(demos), figsize=(4.4 * len(demos), 3.8), facecolor=SURFACE, constrained_layout=True)
for axis, demo in zip(axes, demos):
    axis.plot(demo['dense_times'], demo['dense_states'][:, 0], color=COLORS[0], linewidth=2, alpha=TRUTH_OPACITY, zorder=2)
    axis.scatter(demo['times'], demo['states'][:, 0], s=26, color=COLORS[0], edgecolors=SURFACE, linewidths=0.8, zorder=3)
    axis.set_title(demo['equation'], loc='left', fontsize=10.5, color=INK)
    axis.set_facecolor(SURFACE)
    axis.grid(axis='y', color=GRID, linewidth=0.8)
    axis.set_axisbelow(True)
    axis.tick_params(colors=MUTED, labelsize=9, length=0)
    for side in axis.spines.values():
        side.set_visible(False)
    axis.set_xlabel('time', fontsize=9, color=MUTED)
figure.suptitle(f'logistic: {len(demos[0]["times"])} samples per demo, {NOISE_FRACTION:.0%} noise, truth nearly invisible', x=0.01, ha='left', fontsize=13, color=INK)
figure.savefig(PLOTS_PATH / 'logistic_20_percent_faint_truth.png', dpi=130, facecolor=SURFACE)
plt.close(figure)
