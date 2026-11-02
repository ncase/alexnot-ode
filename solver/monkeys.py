"""Monkeys: each one looks at the parents, and proposes new programs. The scorer decides what's actually good."""
import itertools
import operator
import re
from typing import Callable

import numpy as np

from programs import Demo, LINE_PATTERN, Level, PARAMETER_PATTERN, Proposal, ScoredProgram, flip_sign, split_line, trapezoid_step

Monkey = Callable[[list[ScoredProgram], Level], list[Proposal]]

# Two numbers are close if they have the same sign, and max(a/b, b/a) < 1 + this. The scorer has the final say
# Being more generous isn't free: more proposals to score means more runs hit the time limits
CLOSE_FRACTION: float = 0.5
# What counts as "near zero" depends on how big a parameter's term is, so try a few cutoffs. Adding & deleting terms both use these
NEAR_ZERO_CUTOFFS: list[float] = [0.001, 0.01, 0.1]
# Only for the add-term monkeys' fit, never the scorer's. Picked on SIR at 1% noise only, from 0.01 up to 0.08
RIDGE_PENALTY: float = 0.05
RELATIONS: dict[str, Callable[[float, float], float]] = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def _is_close(first: float, second: float) -> bool:
    return first * second > 0 and max(abs(first), abs(second)) < (1 + CLOSE_FRACTION) * min(abs(first), abs(second))


def _linear_term_names(variable_names: list[str]) -> list[str]:
    """A constant ('') & each variable."""
    return [''] + [f'data.{name}' for name in variable_names]


def _quadratic_term_names(variable_names: list[str]) -> list[str]:
    """A constant, each variable & each product of two variables, including a variable with itself."""
    return _linear_term_names(variable_names) + [f'data.{first} * data.{second}' for first, second in itertools.combinations_with_replacement(variable_names, 2)]


def _term_values(term: str, demo: Demo) -> np.ndarray:
    """A term's value at each of a demo's data points."""
    values: np.ndarray = np.ones(len(demo.times))
    for factor in term.split(' * ') if term else []:
        values = values * demo.states[:, demo.variable_names.index(factor.removeprefix('data.'))]
    return values


def _add_lines(parent: ScoredProgram, new_lines: list[tuple[str, str]]) -> Proposal:
    """Add (variable, term) lines to a program. Their values are just placeholders: the scorer fits every parameter."""
    lines: list[str] = parent.source.splitlines()
    new_names: list[str] = [f'new{index}' for index in range(len(new_lines))]
    for name, (variable, term) in zip(new_names, new_lines):
        lines.append(f'diff.{variable} += params.{name}' + (f' * {term}' if term else ''))
    params: list[dict[str, float]] = [{**parent_params, **{name: 1.0 for name in new_names}} for parent_params in parent.params]
    return Proposal('\n'.join(lines), params)


def _existing_terms(parent: ScoredProgram) -> set[tuple[str, str]]:
    """The exact (variable, term) pairs a program already has."""
    return {(split_line(line)[0], split_line(line)[2]) for line in parent.source.splitlines()}


def _propose_big_terms(parents: list[ScoredProgram], level: Level, terms: list[str]) -> list[Proposal]:
    """Like SINDy: on each demo, fit all the terms to the residual of every equation. Then, for each cutoff, propose adding the terms above it on just that demo."""
    proposals: list[Proposal] = []
    for parent in parents:
        existing: set[tuple[str, str]] = _existing_terms(parent)
        for demo, residuals in zip(level.demos, parent.residuals):
            term_columns: np.ndarray = np.column_stack([trapezoid_step(_term_values(term, demo), demo.times) for term in terms])
            residual_columns: np.ndarray = np.column_stack([residuals[variable] for variable in level.variable_names])
            # Ridge regression, so nearly-redundant terms share the credit instead of fighting with huge opposite coefficients. Shaped (term, variable)
            coefficients: np.ndarray = np.linalg.solve(term_columns.T @ term_columns + RIDGE_PENALTY * np.eye(len(terms)), term_columns.T @ residual_columns)
            for cutoff in NEAR_ZERO_CUTOFFS:
                # Only size counts here, not sign: the fit flips any negative parameters to `-=` later on.
                # A term the parent already has gets no second line, since the scorer refits the one it's got
                new_lines: list[tuple[str, str]] = [
                    (variable, term)
                    for column, variable in enumerate(level.variable_names)
                    for row, term in enumerate(terms)
                    if abs(coefficients[row, column]) >= cutoff and (variable, term) not in existing
                ]
                if new_lines:
                    proposals.append(_add_lines(parent, new_lines))
    return proposals


def add_linear_terms(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    return _propose_big_terms(parents, level, _linear_term_names(level.variable_names))


def add_quadratic_terms(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    return _propose_big_terms(parents, level, _quadratic_term_names(level.variable_names))


def add_single_terms(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    """Ignoring the data's values, propose adding each possible term to each equation, one at a time. Only += is needed, since the fit picks the sign."""
    proposals: list[Proposal] = []
    for parent in parents:
        existing: set[tuple[str, str]] = _existing_terms(parent)
        for variable, term in itertools.product(level.variable_names, _quadratic_term_names(level.variable_names)):
            if (variable, term) not in existing:
                proposals.append(_add_lines(parent, [(variable, term)]))
    return proposals


def delete_interaction_terms(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    """For each line, propose removing each thing it multiplies together, one at a time: a parameter, a relation, or a data term."""
    proposals: list[Proposal] = []
    for parent in parents:
        lines: list[str] = parent.source.splitlines()
        for index, line in enumerate(lines):
            variable, sign, coefficient, term = LINE_PATTERN.fullmatch(line).groups()
            things: list[str] = ([coefficient] if coefficient else []) + (term.split(' * ') if term else [])
            # A line with just one thing would have nothing left. That's delete_lines' job
            if len(things) < 2:
                continue
            for removed in range(len(things)):
                new_line: str = f'diff.{variable} {sign}= ' + ' * '.join(things[:removed] + things[removed + 1:])
                source: str = '\n'.join(lines[:index] + [new_line] + lines[index + 1:])
                # Drop any parameter that nothing uses anymore
                kept_names: set[str] = set(PARAMETER_PATTERN.findall(source))
                params: list[dict[str, float]] = [{name: value for name, value in demo_params.items() if name in kept_names} for demo_params in parent.params]
                proposals.append(Proposal(source, params))
    return proposals


def delete_lines(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    """Propose removing each line, one at a time. If a line wasn't pulling its weight, the scorer will reward this."""
    proposals: list[Proposal] = []
    for parent in parents:
        lines: list[str] = parent.source.splitlines()
        for index in range(len(lines)):
            kept_lines: list[str] = lines[:index] + lines[index + 1:]
            source: str = '\n'.join(kept_lines)
            # Drop any parameter that nothing uses anymore
            kept_names: set[str] = set(PARAMETER_PATTERN.findall(source))
            params: list[dict[str, float]] = [{name: value for name, value in demo_params.items() if name in kept_names} for demo_params in parent.params]
            proposals.append(Proposal(source, params))
    return proposals


def delete_near_zeros(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    """Like SINDy's thresholding: on each demo, for each cutoff, propose removing every line whose parameter is near zero on just that demo, all at once."""
    proposals: list[Proposal] = []
    for parent in parents:
        lines: list[str] = parent.source.splitlines()
        for demo_params, cutoff in itertools.product(parent.params, NEAR_ZERO_CUTOFFS):
            near_zero: set[str] = {name for name, value in demo_params.items() if abs(value) < cutoff}
            # A relation's other parameter might still matter, so only delete lines with one parameter
            kept_lines: list[str] = [line for line in lines if not (len(PARAMETER_PATTERN.findall(line)) == 1 and PARAMETER_PATTERN.findall(line)[0] in near_zero)]
            if len(kept_lines) == len(lines):
                continue
            source: str = '\n'.join(kept_lines)
            kept_names: set[str] = set(PARAMETER_PATTERN.findall(source))
            params: list[dict[str, float]] = [{name: value for name, value in all_params.items() if name in kept_names} for all_params in parent.params]
            proposals.append(Proposal(source, params))
    return proposals


def _relation_is_close(target: str, first: str, second: str, symbol: str, sign: int, all_params: list[dict[str, float]]) -> bool:
    """Is target ≈ sign * (first (symbol) second), on EVERY demo? A coincidence on one demo shouldn't count."""
    for demo_params in all_params:
        if not _is_close(demo_params[target], sign * RELATIONS[symbol](demo_params[first], demo_params[second])):
            return False
    return True


def relate_parameters(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    """When one parameter's close to the sum/difference/product of two others, propose replacing it with that expression."""
    proposals: list[Proposal] = []
    for parent in parents:
        for target in parent.params[0]:
            # Parameters already inside a relation can't be replaced, or we'd nest brackets
            target_pattern: re.Pattern = re.compile(rf'params\.{target}\b')
            if any(target_pattern.search(line) and len(PARAMETER_PATTERN.findall(line)) > 1 for line in parent.source.splitlines()):
                continue
            others: list[str] = [name for name in parent.params[0] if name != target]
            for (first, second), symbol in itertools.product(itertools.permutations(others, 2), RELATIONS):
                # a + b is the same as b + a, so only try one order of those
                if symbol in '+*' and first > second:
                    continue
                # A sign of -1 means target ≈ -(a + b), which gets written by flipping the line to `-= (a + b)`.
                # No -1 for subtraction, since -(a - b) is just (b - a), which the other order already covers
                for sign in [1] if symbol == '-' else [1, -1]:
                    if _relation_is_close(target, first, second, symbol, sign, parent.params):
                        lines: list[str] = [flip_sign(line) if sign == -1 and target_pattern.search(line) else line for line in parent.source.splitlines()]
                        source: str = target_pattern.sub(f'(params.{first} {symbol} params.{second})', '\n'.join(lines))
                        params: list[dict[str, float]] = [{name: value for name, value in demo_params.items() if name != target} for demo_params in parent.params]
                        proposals.append(Proposal(source, params))
    return proposals


def tie_parameters(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    """When two parameters are close in size on EVERY demo, propose making them one parameter. If their signs are opposite on every demo, the replaced one's lines flip between += and -=."""
    proposals: list[Proposal] = []
    for parent in parents:
        lines: list[str] = parent.source.splitlines()
        for kept, replaced in itertools.combinations(parent.params[0], 2):
            if not all(_is_close(abs(demo_params[kept]), abs(demo_params[replaced])) for demo_params in parent.params):
                continue
            # Same sign on some demos and opposite on others can't be one parameter
            same_signs: bool = all(demo_params[kept] * demo_params[replaced] > 0 for demo_params in parent.params)
            opposite_signs: bool = all(demo_params[kept] * demo_params[replaced] < 0 for demo_params in parent.params)
            if not same_signs and not opposite_signs:
                continue
            replaced_pattern: re.Pattern = re.compile(rf'params\.{replaced}\b')
            lines_using_it: list[str] = [line for line in lines if replaced_pattern.search(line)]
            # Tying two parts of one relation gives junk like (a - a)
            if any(kept in PARAMETER_PATTERN.findall(line) for line in lines_using_it):
                continue
            # Flipping a whole line can't flip just one part of a relation
            if opposite_signs and any(len(PARAMETER_PATTERN.findall(line)) > 1 for line in lines_using_it):
                continue
            new_lines: list[str] = [flip_sign(line) if opposite_signs and replaced_pattern.search(line) else line for line in lines]
            source: str = replaced_pattern.sub(f'params.{kept}', '\n'.join(new_lines))
            params: list[dict[str, float]] = [{name: value for name, value in demo_params.items() if name != replaced} for demo_params in parent.params]
            proposals.append(Proposal(source, params))
    return proposals


def snap_to_one(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    """When a parameter's close to 1 on EVERY demo, propose removing it, so `params.a * data.y` becomes `data.y`."""
    proposals: list[Proposal] = []
    for parent in parents:
        for name in parent.params[0]:
            lines_using_it: list[str] = [line for line in parent.source.splitlines() if name in PARAMETER_PATTERN.findall(line)]
            # A plain constant has nothing left once its parameter's gone, and a relation's parameter can't be pulled out on its own
            if any(' * ' not in line or len(PARAMETER_PATTERN.findall(line)) > 1 for line in lines_using_it):
                continue
            # The sign tidy-up already turned all-negative parameters positive, so this covers -1 too
            if all(_is_close(demo_params[name], 1.0) for demo_params in parent.params):
                source: str = re.sub(rf'params\.{name} \* ', '', parent.source)
                params: list[dict[str, float]] = [{key: value for key, value in demo_params.items() if key != name} for demo_params in parent.params]
                proposals.append(Proposal(source, params))
    return proposals


MONKEYS: list[Monkey] = [add_linear_terms, add_quadratic_terms, add_single_terms, delete_interaction_terms, delete_lines, delete_near_zeros, relate_parameters, snap_to_one, tie_parameters]
