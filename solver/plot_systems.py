"""Graph every test system: ground truth vs what the program gets to see. Saves to levels/plots/systems.png."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from systems import SYSTEMS, System, load_lynx_hare, noisy_samples, simulate

OUTPUT_PATH: Path = Path(__file__).parent.parent / 'levels' / 'plots' / 'systems.png'
BUTTERFLY_PATH: Path = Path(__file__).parent.parent / 'levels' / 'plots' / 'lorenz_butterfly.png'

# One fixed color per variable: x, y, z
COLORS: list[str] = ['#2a78d6', '#eb6834', '#1baf7a']
SURFACE: str = '#fcfcfb'
INK: str = '#3d3d3a'
MUTED: str = '#8a8a84'
GRID: str = '#e8e7e2'

# Dense enough that the truth looks like a smooth line, even for Lorenz
DENSE_SAMPLE_COUNT: int = 6000
# Past this many samples, dots need to shrink or they'd blot out the truth
CROWDED_SAMPLE_COUNT: int = 200
PLOT_SEED: int = 1
# Faint, so your eye reads the dots first, and can see how sparse the data really is
LINE_OPACITY: float = 0.15


def style_axis(axis: plt.Axes, title: str, time_label: str) -> None:
    axis.set_title(title, loc='left', fontsize=10.5, color=INK, pad=22)
    axis.set_facecolor(SURFACE)
    axis.grid(axis='y', color=GRID, linewidth=0.8)
    axis.set_axisbelow(True)
    axis.tick_params(colors=MUTED, labelsize=9, length=0)
    for side in axis.spines.values():
        side.set_visible(False)
    axis.set_xlabel(time_label, fontsize=9, color=MUTED)
    # Above the plot, so the legend can never cover the data
    legend = axis.legend(frameon=False, fontsize=9, labelcolor=INK, ncols=3, loc='lower left', bbox_to_anchor=(0, 1), borderaxespad=0.1, handlelength=1.2)
    # The legend's lines stay solid, or you couldn't tell which color's which
    for legend_line in legend.get_lines():
        legend_line.set_alpha(1)


figure, axes = plt.subplots(4, 2, figsize=(11, 13), facecolor=SURFACE, constrained_layout=True)

# The synthetic systems, with a line for the truth & dots for the noisy samples
for axis, system in zip(axes.flat, SYSTEMS):
    dense_times, dense_states = simulate(system, DENSE_SAMPLE_COUNT)
    times, states = noisy_samples(system, PLOT_SEED)
    is_crowded: bool = system.sample_count > CROWDED_SAMPLE_COUNT
    for column, (name, meaning) in enumerate(zip(system.variable_names, system.variable_meanings)):
        label: str = name if name == meaning else f'{name} = {meaning}'
        axis.plot(dense_times, dense_states[:, column], color=COLORS[column], linewidth=1 if is_crowded else 2, alpha=LINE_OPACITY, zorder=2, label=label)
        axis.scatter(times, states[:, column], s=4 if is_crowded else 26, color=COLORS[column], edgecolors=SURFACE, linewidths=0 if is_crowded else 0.8, zorder=3)
    title: str = f'{system.name}  ({system.sample_count} samples, {system.noise_fraction:.0%} noise)\n{system.equation}'
    style_axis(axis, title, 'time')

# The real data. There's no known truth to draw, so the line only connects the dots
lynx_hare_axis: plt.Axes = axes.flat[len(SYSTEMS)]
years, pelts = load_lynx_hare()
for column, name in enumerate(['x = hare', 'y = lynx']):
    lynx_hare_axis.plot(years, pelts[:, column], color=COLORS[column], linewidth=1, alpha=LINE_OPACITY, zorder=2, label=name)
    lynx_hare_axis.scatter(years, pelts[:, column], s=26, color=COLORS[column], edgecolors=SURFACE, linewidths=0.8, zorder=3)
style_axis(lynx_hare_axis, f'Real lynx & hare  ({len(years)} yearly samples)\nThousands of pelts (no known truth, lines just connect the dots)', 'year')
lynx_hare_axis.set_xticks(np.arange(1900, 1921, 5))

figure.suptitle('Lines = ground truth, dots = what the program gets to see', x=0.01, ha='left', fontsize=13, color=INK)
OUTPUT_PATH.parent.mkdir(exist_ok=True)
figure.savefig(OUTPUT_PATH, dpi=130, facecolor=SURFACE)
print(f'Saved {OUTPUT_PATH}')

# Lorenz's x & y overlap over time, so also show the famous butterfly in 3D. (Matplotlib has this built in!)
lorenz: System = next(system for system in SYSTEMS if system.name == 'Lorenz')
_, lorenz_states = simulate(lorenz, DENSE_SAMPLE_COUNT)
butterfly_figure: plt.Figure = plt.figure(figsize=(7, 6), facecolor=SURFACE)
butterfly_axis = butterfly_figure.add_subplot(projection='3d', facecolor=SURFACE)
butterfly_axis.plot(lorenz_states[:, 0], lorenz_states[:, 1], lorenz_states[:, 2], color=COLORS[0], linewidth=0.5)
butterfly_axis.set_xlabel('x', color=MUTED)
butterfly_axis.set_ylabel('y', color=MUTED)
butterfly_axis.set_zlabel('z', color=MUTED)
butterfly_axis.tick_params(colors=MUTED, labelsize=8)
butterfly_axis.set_title('Lorenz: ground truth, 30 time units', loc='left', fontsize=11, color=INK)
butterfly_figure.savefig(BUTTERFLY_PATH, dpi=130, facecolor=SURFACE)
print(f'Saved {BUTTERFLY_PATH}')
