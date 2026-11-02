"""Run the search on named levels (or every level), print each winner, and save a reasoning trace to levels/results/.

Usage: python solver/run_level.py [exponential logistic]
"""
from pathlib import Path
import sys
import time

from programs import TIMESERIES_PATH, Level, ScoredProgram, load_level
from search import RoundLog, search_population

RESULTS_PATH: Path = Path(__file__).parent.parent / 'levels' / 'results'
RUNNER_UP_COUNT: int = 4


def describe_program(program: ScoredProgram) -> str:
    """A program's score & its three parts (lower's better), its text, then its fitted parameters on each demo."""
    text: str = f'-- score: {program.score:.2f} (accuracy {program.accuracy_score:.2f}, token simplicity {program.token_score:.2f}, parameter simplicity {program.parameter_score:.2f}) --\n'
    text += (program.source if program.source else '(blank program)') + '\n'
    if program.params[0]:
        for demo_index, demo_params in enumerate(program.params):
            text += f'  Demo {demo_index}: ' + ', '.join(f'{name} = {value:.3f}' for name, value in demo_params.items()) + '\n'
    return text


def make_trace(level_name: str, population: list[ScoredProgram], round_logs: list[RoundLog], seconds: float) -> str:
    """The winner & runner-ups up top, then every round's parents below."""
    ranked: list[ScoredProgram] = sorted(population, key=lambda program: program.score)
    trace: str = f'# {level_name}\n\nSolved in {seconds:.2f} seconds. {len(population)} programs considered, over {len(round_logs)} rounds.\n\n'
    trace += f'## Winner\n\n{describe_program(ranked[0])}\n'
    trace += f'## Runner-ups\n\n' + '\n'.join(describe_program(program) for program in ranked[1:RUNNER_UP_COUNT + 1]) + '\n'
    trace += '# The Search\n\n'
    for round_number, round_log in enumerate(round_logs):
        proposed: int = sum(round_log.new_proposals_by_monkey.values())
        out_of_time: str = ' (OUT OF TIME)' if round_log.scored_count < proposed else ''
        trace += f'## Round {round_number} | {round_log.seconds:.2f}s | best score: {round_log.best_score:.2f}\n\n'
        trace += f'+{proposed} new programs ({round_log.scored_count} actually scored){out_of_time}\n'
        trace += ''.join(f'* {monkey_name}: +{count}\n' for monkey_name, count in round_log.new_proposals_by_monkey.items())
        trace += f'\n### {len(round_log.parents)} parents for the next round\n\n'
        trace += '\n'.join(describe_program(parent) for parent in round_log.parents) + '\n'
    return trace


if __name__ == '__main__':
    level_names: list[str] = sys.argv[1:] or sorted(path.stem for path in TIMESERIES_PATH.glob('*.json'))
    RESULTS_PATH.mkdir(exist_ok=True)
    for level_name in level_names:
        level: Level = load_level(TIMESERIES_PATH / f'{level_name}.json')
        round_logs: list[RoundLog] = []
        start_time: float = time.perf_counter()
        population: list[ScoredProgram] = search_population(level, round_logs)
        seconds: float = time.perf_counter() - start_time
        (RESULTS_PATH / f'{level_name}.md').write_text(make_trace(level_name, population, round_logs, seconds))
        winner: ScoredProgram = min(population, key=lambda program: program.score)
        print(f'\n=== {level_name}: {seconds:.2f} seconds, {len(population)} programs, {len(round_logs)} rounds')
        print(describe_program(winner), end='')
