"""Why does Spring do worse at 1% noise than at 5%? Compares the intended `x += y` against the loose `x += a * y`, and tests the step error as the cause.

This only scores those two programs directly, with no search. Takes a bit over a minute.

Usage: PYTHONPATH=levels/generators python solver/why_spring_low_noise.py
"""
import statistics

import numpy as np

import common
from programs import PARAMETER_PATTERN, Demo, Level, Proposal, evaluate, trapezoid_step
from rank_intended import INTENDED_PROGRAMS, LOOSE_SPRING, score_directly
import spring

INTENDED: str = next(iter(INTENDED_PROGRAMS['spring']))
SEEDS: range = range(20)
NOISE_FRACTIONS: list[float] = [0.0, 0.001, 0.005, 0.01, 0.02, 0.03, 0.05, 0.10, 0.20]


def make_level(noise_fraction: float, seed: int, sample_count: int = common.DEFAULT_SAMPLE_COUNT) -> Level:
    """Same noise as the fan's files, for the same noise fraction & seed."""
    common.DEFAULT_SAMPLE_COUNT = sample_count
    return Level(spring.VARIABLE_NAMES, [Demo(demo['times'], demo['states'], spring.VARIABLE_NAMES) for demo in spring.build_demos(noise_fraction, seed)])


def blank_start(source: str) -> Proposal:
    """A program with every parameter starting at 1, on all 3 demos. Fitting takes it from there."""
    names: list[str] = list(dict.fromkeys(PARAMETER_PATTERN.findall(source)))
    return Proposal(source, [{name: 1.0 for name in names} for _ in spring.DEMO_SETTINGS])


def remove_step_error(level: Level, seed: int) -> Level:
    """Same noisy data, minus the trapezoid's own error, which we can only measure because we know the truth here."""
    truth: Level = make_level(0.0, seed, len(level.demos[0].times))
    for demo, true_demo, settings in zip(level.demos, truth.demos, spring.DEMO_SETTINGS):
        true_slopes: dict[str, np.ndarray] = {'x': true_demo.data.y, 'y': -settings['stiffness'] * true_demo.data.x - settings['damping'] * true_demo.data.y}
        for name, slopes in true_slopes.items():
            demo.state_changes[name] = demo.state_changes[name] - (true_demo.state_changes[name] - trapezoid_step(slopes, true_demo.times))
            demo.blank_mean_squared_errors[name] = float(np.mean(demo.state_changes[name]**2))
    return level


if __name__ == '__main__':
    # 1. What `a` does the loose form fit on perfect data? Anything but 1 is the step error
    print('Best a on perfect data, by demo (50 samples):')
    perfect: Level = make_level(0.0, 0)
    for demo in perfect.demos:
        steps: np.ndarray = trapezoid_step(demo.data.y, demo.times)
        print(f'  a = {float(steps @ demo.state_changes["x"] / (steps @ steps)):.4f}')

    # 2. Scores alone, no search. Positive means the loose form beats the intended program
    print('\nLoose form\'s lead over intended, median over 20 seeds. Its 2 extra tokens & 1 parameter cost 0.70 of this already:')
    for noise_fraction in NOISE_FRACTIONS:
        leads: list[float] = []
        for seed in SEEDS:
            level: Level = make_level(noise_fraction, seed)
            leads.append(score_directly(INTENDED, level) - score_directly(LOOSE_SPRING, level))
        print(f'  noise {noise_fraction:5.1%}: {statistics.median(leads):+.2f}, loose ahead on {sum(lead > 0 for lead in leads):2d}/20')

    # 2b. Is the x equation's error near the floor? The floor's log ratio is log(MSE_FLOOR) = -6.91, and below it more accuracy earns nothing
    print('\nMedian accuracy cost on x alone, per program, then the loose lead without the step error & with more samples:')
    for noise_fraction in [0.001, 0.003, 0.005, 0.0075, 0.01, 0.0125, 0.015, 0.02, 0.03, 0.05]:
        intended_costs: list[float] = []
        loose_costs: list[float] = []
        no_step_error_leads: list[float] = []
        for seed in SEEDS:
            level = make_level(noise_fraction, seed)
            intended_costs.append(evaluate(blank_start(INTENDED), level).variable_costs['x'])
            loose_costs.append(evaluate(blank_start(LOOSE_SPRING), level).variable_costs['x'])
            cleaned: Level = remove_step_error(make_level(noise_fraction, seed), seed)
            no_step_error_leads.append(score_directly(INTENDED, cleaned) - score_directly(LOOSE_SPRING, cleaned))
        print(f'  noise {noise_fraction:6.2%}: intended {statistics.median(intended_costs):.3f}, loose {statistics.median(loose_costs):.3f}, '
              f'no step error: lead {statistics.median(no_step_error_leads):+.2f}, loose ahead on {sum(lead > 0 for lead in no_step_error_leads):2d}/20')

    print('\nAt 1% noise, by sample count (more samples = smaller time steps = less step error):')
    for sample_count in [50, 100, 200, 400]:
        leads = [score_directly(INTENDED, make_level(0.01, seed, sample_count)) - score_directly(LOOSE_SPRING, make_level(0.01, seed, sample_count)) for seed in SEEDS]
        print(f'  {sample_count:3d} samples: lead {statistics.median(leads):+.2f}, loose ahead on {sum(lead > 0 for lead in leads):2d}/20')
