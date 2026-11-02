"""Programs: running them, fitting their parameters, and scoring them.

A level has several demos. One program has to explain all of them, but gets its own fitted parameters on each demo.
"""
from dataclasses import dataclass, field
import functools
import json
from pathlib import Path
import re
from types import CodeType, SimpleNamespace

import numpy as np
from scipy.optimize import least_squares

# Scoring magic constants. Accuracy's averaged across demos, so more demos doesn't outweigh the program's own cost.
# Tokens & parameters are counted once: it's one program, with the same knobs on every demo. We never penalize a parameter's size.
# Token & parameter weights were picked by solver/fan_scoring.py, on exponential & logistic only.
# Accuracy was the best total across all 8 fan levels, of 5, 7.5, 12.5, 25, 37.5 & 50. Lower loses the simple levels, higher loses SIR
SCORE_COEFF_ACCURACY: float = 37.5
SCORE_COEFF_TOKEN: float = 0.1
SCORE_COEFF_PARAMETER: float = 0.5
# The trapezoid step has its own tiny error, up to about 1e-4 of the blank program's. Below this floor, more accuracy earns nothing,
# otherwise extra terms win on perfect data, just by fitting that error. Noise keeps real errors far above this (3.6e-2 at the lowest)
MSE_FLOOR: float = 1e-3

TIMESERIES_PATH: Path = Path(__file__).parent.parent / 'levels' / 'timeseries'

# Every program line looks like `diff.x += params.a * data.x`, or `diff.x += (params.b - params.a) * data.x` with a relation,
# or `diff.x += data.y` with no parameter at all
LINE_PATTERN: re.Pattern = re.compile(r'diff\.(\w+) ([+-])= (?:(params\.\w+|\(params\.\w+ [-+*/] params\.\w+\))(?: \* )?)?(.*)')
PARAMETER_PATTERN: re.Pattern = re.compile(r'params\.(\w+)')
NONLINEAR_RELATION_PATTERN: re.Pattern = re.compile(r'params\.\w+ [*/] params\.\w+')


def trapezoid_step(values: np.ndarray, times: np.ndarray) -> np.ndarray:
    """How far a variable moves over each time step, if `values` is its slope at each data point."""
    return (times[1:] - times[:-1]) * (values[:-1] + values[1:]) / 2


@dataclass
class Demo:
    times: np.ndarray
    states: np.ndarray  # Shaped (time, variable)
    variable_names: list[str]
    state_changes: dict[str, np.ndarray] = field(init=False)  # How far each variable really moved, over each time step
    blank_mean_squared_errors: dict[str, float] = field(init=False)
    data: SimpleNamespace = field(init=False)  # What programs read from. Shared by every run, since programs only write to diff

    def __post_init__(self) -> None:
        self.state_changes = {name: np.diff(self.states[:, column]) for column, name in enumerate(self.variable_names)}
        # The blank program predicts no change, so its error is just the raw change between samples
        self.blank_mean_squared_errors = {name: float(np.mean(changes**2)) for name, changes in self.state_changes.items()}
        self.data = SimpleNamespace(**{name: self.states[:, column] for column, name in enumerate(self.variable_names)})


@dataclass
class Level:
    variable_names: list[str]
    demos: list[Demo]


def load_level(path: Path) -> Level:
    raw_level: dict = json.loads(path.read_text())
    names: list[str] = raw_level['variable_names']
    demos: list[Demo] = [Demo(np.array(demo['times']), np.array(demo['states']), names) for demo in raw_level['demos']]
    return Level(names, demos)


@dataclass
class Proposal:
    source: str
    params: list[dict[str, float]]  # Starting values for the fit, one dict per demo


@dataclass
class ScoredProgram:
    source: str
    params: list[dict[str, float]]  # Best-fit values, one dict per demo
    score: float
    variable_costs: dict[str, float]  # Accuracy cost on each variable, averaged over demos
    predictions: list[dict[str, np.ndarray]]  # One per demo: the program's diff at each data point
    residuals: list[dict[str, np.ndarray]]  # One per demo: real step minus predicted step, for each time step
    # The score's three parts, added up. For the reasoning trace
    accuracy_score: float
    token_score: float
    parameter_score: float


def split_line(line: str) -> tuple[str, str, str]:
    """Split a program line into its variable, its sign, and its term (`data.x`, or '' for a plain constant)."""
    variable, sign, _, term = LINE_PATTERN.fullmatch(line).groups()
    return variable, sign, term or ''


def canonicalize(proposal: Proposal, level: Level) -> Proposal:
    """Sort the lines & rename parameters a, b, c..., so the same program always has the same string."""
    def sort_key(line: str) -> tuple[int, str]:
        variable, _, term = split_line(line)
        return level.variable_names.index(variable), term

    lines: list[str] = sorted(proposal.source.splitlines(), key=sort_key)
    # Dicts keep insertion order, so this lists parameters in order of appearance, without repeats
    old_names: list[str] = list(dict.fromkeys(PARAMETER_PATTERN.findall('\n'.join(lines))))
    new_names: dict[str, str] = {old: chr(ord('a') + index) if index < 26 else f'p{index}' for index, old in enumerate(old_names)}
    source: str = PARAMETER_PATTERN.sub(lambda match: f'params.{new_names[match.group(1)]}', '\n'.join(lines))
    return Proposal(source, [{new_names[old]: demo_params[old] for old in old_names} for demo_params in proposal.params])


def flip_sign(line: str) -> str:
    return line.replace('+=', '-=') if '+=' in line else line.replace('-=', '+=')


def make_parameters_positive(proposal: Proposal) -> Proposal:
    """Rewrite a parameter that's negative on EVERY demo as a positive one, by flipping += and -= where it's used.

    A parameter with mixed signs is always written with +=, since growth & decay can be the same program!
    (Otherwise `+= a` and `-= a` would be two spellings of one program, once you negate its numbers)
    """
    lines: list[str] = proposal.source.splitlines()
    params: list[dict[str, float]] = [dict(demo_params) for demo_params in proposal.params]
    for name in proposal.params[0]:
        # Flipping a whole line can't flip just one part of a relation, so parameters in relations stay as they are
        if any(name in PARAMETER_PATTERN.findall(line) and len(PARAMETER_PATTERN.findall(line)) > 1 for line in lines):
            continue
        all_negative: bool = all(demo_params[name] < 0 for demo_params in proposal.params)
        mixed_signs: bool = not all_negative and any(demo_params[name] < 0 for demo_params in proposal.params)
        written_with_minus: bool = any('-=' in line and name in PARAMETER_PATTERN.findall(line) for line in lines)
        if all_negative or (mixed_signs and written_with_minus):
            for demo_params in params:
                demo_params[name] = -demo_params[name]
            lines = [flip_sign(line) if name in PARAMETER_PATTERN.findall(line) else line for line in lines]
    return Proposal('\n'.join(lines), params)


@functools.lru_cache(maxsize=None)
def compile_program(source: str) -> CodeType:
    """Fitting runs a program dozens of times, so only turn its text into bytecode once."""
    return compile(source, '<program>', 'exec')


def run_program(source: str, params: dict[str, float], demo: Demo) -> dict[str, np.ndarray]:
    """Run a program on one demo's whole time series at once, and return its diff at each data point."""
    diff: SimpleNamespace = SimpleNamespace(**{name: np.zeros(len(demo.times)) for name in demo.variable_names})
    exec(compile_program(source), {'__builtins__': {}, 'params': SimpleNamespace(**params), 'data': demo.data, 'diff': diff})
    return vars(diff)


def get_residuals(predictions: dict[str, np.ndarray], demo: Demo) -> dict[str, np.ndarray]:
    return {name: demo.state_changes[name] - trapezoid_step(predictions[name], demo.times) for name in demo.variable_names}


def fit_parameters(source: str, start_params: dict[str, float], demo: Demo) -> dict[str, float]:
    """Fit one demo's parameters, across all its equations at once, since a tied parameter can span several."""
    if not start_params:
        return start_params
    names: list[str] = list(start_params)

    def weighted_residuals(values: np.ndarray) -> np.ndarray:
        residuals: dict[str, np.ndarray] = get_residuals(run_program(source, dict(zip(names, values)), demo), demo)
        # Divide by the blank program's error, so big variables can't dominate
        return np.concatenate([residuals[name] / np.sqrt(demo.blank_mean_squared_errors[name]) for name in demo.variable_names])

    start: np.ndarray = np.array([start_params[name] for name in names])
    # A relation like a * b or a / b means crawling towards the answer, the slow way
    if NONLINEAR_RELATION_PATTERN.search(source):
        fit = least_squares(weighted_residuals, start)
        return dict(zip(names, map(float, fit.x)))

    # Otherwise, each parameter's just a volume knob on its terms, so the errors change in a perfectly straight line.
    # That means we can nudge each knob once to see what it does, then solve for the best settings directly!
    at_start: np.ndarray = weighted_residuals(start)
    knob_effects: np.ndarray = np.column_stack([weighted_residuals(start + nudge) - at_start for nudge in np.eye(len(names))])
    best_change: np.ndarray = np.linalg.lstsq(knob_effects, -at_start, rcond=None)[0]
    return dict(zip(names, map(float, start + best_change)))


def score_program(proposal: Proposal, level: Level) -> ScoredProgram:
    """Lower is better, and the blank program scores exactly 0. See the README for the reasoning."""
    predictions: list[dict[str, np.ndarray]] = []
    all_residuals: list[dict[str, np.ndarray]] = []
    variable_costs: dict[str, float] = {name: 0.0 for name in level.variable_names}
    # All demos get scored together
    for demo, demo_params in zip(level.demos, proposal.params):
        demo_predictions: dict[str, np.ndarray] = run_program(proposal.source, demo_params, demo)
        demo_residuals: dict[str, np.ndarray] = get_residuals(demo_predictions, demo)
        predictions.append(demo_predictions)
        all_residuals.append(demo_residuals)
        for name, values in demo_residuals.items():
            error: float = float(np.mean(values**2))
            # NaN or infinity counts as a crash, so the search drops this program
            if not np.isfinite(error):
                raise ValueError('Program predicted a non-finite value')
            blank_error: float = demo.blank_mean_squared_errors[name]
            variable_costs[name] += np.log(max(error, MSE_FLOOR * blank_error) / blank_error) / len(level.demos)

    accuracy_score: float = float(SCORE_COEFF_ACCURACY * sum(variable_costs.values()))
    token_score: float = SCORE_COEFF_TOKEN * len(re.findall(r'\w+', proposal.source))
    parameter_score: float = SCORE_COEFF_PARAMETER * len(proposal.params[0])
    score: float = accuracy_score + token_score + parameter_score
    return ScoredProgram(proposal.source, proposal.params, score, variable_costs, predictions, all_residuals, accuracy_score, token_score, parameter_score)


def evaluate(proposal: Proposal, level: Level) -> ScoredProgram:
    """The whole pipeline for one proposal: fit on each demo, tidy up, then score on all demos."""
    tidy: Proposal = canonicalize(proposal, level)
    fitted_params: list[dict[str, float]] = [fit_parameters(tidy.source, demo_params, demo) for demo_params, demo in zip(tidy.params, level.demos)]
    return score_program(canonicalize(make_parameters_positive(Proposal(tidy.source, fitted_params)), level), level)
