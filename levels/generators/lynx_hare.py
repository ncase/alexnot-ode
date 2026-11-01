"""The real data: Hudson's Bay hare & lynx pelts, 1900-1920. Writes levels/timeseries/lynx_hare.json.

One demo only, and no added noise, since real data brings its own. x is hares and y is lynx, both in thousands of pelts.
"""
from pathlib import Path

import numpy as np

from common import plot_level, write_level

CSV_PATH: Path = Path(__file__).parent.parent.parent / 'data' / 'lynx_hare.csv'
VARIABLE_NAMES: list[str] = ['x', 'y']
# The file starts with 3 comment lines, then the column names
HEADER_LINES: int = 4


if __name__ == '__main__':
    rows: np.ndarray = np.loadtxt(CSV_PATH, delimiter=',', skiprows=HEADER_LINES)
    times: np.ndarray = rows[:, 0] - rows[0, 0]
    states: np.ndarray = rows[:, 1:]
    # There's no ground truth here, so the graph's lines just connect the dots
    demo: dict = {'equation': 'x = hares, y = lynx (thousands of pelts, years since 1900)', 'times': times, 'states': states, 'dense_times': times, 'dense_states': states}
    write_level('lynx_hare', VARIABLE_NAMES, [demo])
    plot_level('lynx_hare', VARIABLE_NAMES, [demo], None)
