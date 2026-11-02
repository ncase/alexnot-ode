"""The real lynx & hare data, at the settings that recover Lotka-Volterra's structure. Saves a trace next to the main settings' one.

Usage: python solver/trace_lynx_sparks.py
"""
import time

import programs
from programs import TIMESERIES_PATH, Level, ScoredProgram, load_level
from run_level import RESULTS_PATH, describe_program, make_trace
from search import RoundLog, search_population

# Weights simplicity more heavily than the main solver's 40 / 0.1 / 0.5
ACCURACY: float = 25.0
TOKEN: float = 1.0
PARAMETER: float = 0.5
OUTPUT_NAME: str = 'lynx_hare_25_1_0.5'

if __name__ == '__main__':
    programs.SCORE_COEFF_ACCURACY, programs.SCORE_COEFF_TOKEN, programs.SCORE_COEFF_PARAMETER = ACCURACY, TOKEN, PARAMETER
    level: Level = load_level(TIMESERIES_PATH / 'lynx_hare.json')
    round_logs: list[RoundLog] = []
    start_time: float = time.perf_counter()
    population: list[ScoredProgram] = search_population(level, round_logs)
    seconds: float = time.perf_counter() - start_time
    (RESULTS_PATH / f'{OUTPUT_NAME}.md').write_text(make_trace(OUTPUT_NAME, population, round_logs, seconds))
    winner: ScoredProgram = min(population, key=lambda program: program.score)
    print(f'\n=== {OUTPUT_NAME}: {seconds:.2f} seconds, {len(population)} programs, {len(round_logs)} rounds')
    print(describe_program(winner), end='', flush=True)
