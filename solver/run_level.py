"""Run the search on named levels, and print the winning program, so we can read it by eye.

Usage: python solver/run_level.py exponential logistic
"""
import sys
import time

from programs import TIMESERIES_PATH, Level, ScoredProgram, load_level
from search import search

for level_name in sys.argv[1:]:
    level: Level = load_level(TIMESERIES_PATH / f'{level_name}.json')
    start_time: float = time.perf_counter()
    winner: ScoredProgram = search(level)
    print(f'\n=== {level_name}: score {winner.score:.1f}, {time.perf_counter() - start_time:.3f} seconds')
    print(winner.source if winner.source else '(blank program)')
    for demo_index, demo_params in enumerate(winner.params):
        print(f'  Demo {demo_index}: ' + ', '.join(f'{name} = {value:.3f}' for name, value in demo_params.items()))
