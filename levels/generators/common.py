"""Shared helpers for the level generators: simulate a demo, then save it as JSON. (And a graph, for us humans)"""
import json
from pathlib import Path
from typing import Callable

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

DEFAULT_SAMPLE_COUNT: int = 50
TIMESERIES_PATH: Path = Path(__file__).parent.parent / 'timeseries'
PLOTS_PATH: Path = Path(__file__).parent.parent / 'plots'

# One fixed color per variable: x, y, z
COLORS: list[str] = ['#2a78d6', '#eb6834', '#1baf7a']
SURFACE: str = '#fcfcfb'
INK: str = '#3d3d3a'
MUTED: str = '#8a8a84'
GRID: str = '#e8e7e2'
# Dense enough that the truth looks like a smooth line
DENSE_SAMPLE_COUNT: int = 2000


def make_demo(
    equation: str,
    derivative: Callable[[float, np.ndarray], list[float]],
    start: list[float],
    end_time: float,
    noise_fraction: float,
    rng: np.random.Generator,
    sample_count: int = DEFAULT_SAMPLE_COUNT,
) -> dict:
    """Integrate the true ODE very accurately, sample it, and add noise scaled to each variable's standard deviation."""
    def simulate(count: int) -> tuple[np.ndarray, np.ndarray]:
        times: np.ndarray = np.linspace(0, end_time, count)
        return times, solve_ivp(derivative, (0, end_time), start, t_eval=times, rtol=1e-10, atol=1e-12).y.T

    times, states = simulate(sample_count)
    noisy_states: np.ndarray = states + rng.normal(0, 1, states.shape) * noise_fraction * states.std(axis=0)
    dense_times, dense_states = simulate(DENSE_SAMPLE_COUNT)
    return {'equation': equation, 'times': times, 'states': noisy_states, 'dense_times': dense_times, 'dense_states': dense_states}


def write_level(name: str, variable_names: list[str], demos: list[dict], output_path: Path | None = None) -> None:
    """Save only what the solver's allowed to see: the sparse, noisy samples. The truth stays out of the JSON."""
    level: dict = {
        'variable_names': variable_names,
        'demos': [{'times': demo['times'].tolist(), 'states': demo['states'].tolist()} for demo in demos],
    }
    path: Path = output_path or TIMESERIES_PATH / f'{name}.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(level))


def plot_level(name: str, variable_names: list[str], demos: list[dict], noise_fraction: float) -> None:
    """Graph each demo: lines are the ground truth, dots are what the program gets to see."""
    figure, axes = plt.subplots(1, len(demos), figsize=(4.4 * len(demos), 3.8), facecolor=SURFACE, constrained_layout=True)
    for axis, demo in zip(axes, demos):
        for column, variable in enumerate(variable_names):
            axis.plot(demo['dense_times'], demo['dense_states'][:, column], color=COLORS[column], linewidth=2, zorder=2, label=variable)
            axis.scatter(demo['times'], demo['states'][:, column], s=26, color=COLORS[column], edgecolors=SURFACE, linewidths=0.8, zorder=3)
        axis.set_title(demo['equation'], loc='left', fontsize=10.5, color=INK, pad=20)
        axis.set_facecolor(SURFACE)
        axis.grid(axis='y', color=GRID, linewidth=0.8)
        axis.set_axisbelow(True)
        axis.tick_params(colors=MUTED, labelsize=9, length=0)
        for side in axis.spines.values():
            side.set_visible(False)
        axis.set_xlabel('time', fontsize=9, color=MUTED)
        # Above the plot, so the legend can never cover the data
        axis.legend(frameon=False, fontsize=9, labelcolor=INK, ncols=3, loc='lower left', bbox_to_anchor=(0, 1), borderaxespad=0.1, handlelength=1.2)
    figure.suptitle(f'{name}: {len(demo["times"])} samples per demo, {noise_fraction:.0%} noise', x=0.01, ha='left', fontsize=13, color=INK)
    PLOTS_PATH.mkdir(parents=True, exist_ok=True)
    figure.savefig(PLOTS_PATH / f'{name}.png', dpi=130, facecolor=SURFACE)
    plt.close(figure)
