"""Monkeys: each one looks at the parents, and proposes new programs. The scorer decides what's actually good."""
import itertools
import operator
import re
from typing import Callable

import numpy as np

from programs import Demo, Level, PARAMETER_PATTERN, Proposal, ScoredProgram, flip_sign, split_line, trapezoid_step

Monkey = Callable[[list[ScoredProgram], Level], list[Proposal]]

# "Close" only filters what gets proposed, so being generous is safe. The scorer has the final say
CLOSE_FRACTION: float = 0.2
RELATIONS: dict[str, Callable[[float, float], float]] = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def _linear_term_names(variable_names: list[str]) -> list[str]:
    """A constant ('') & each variable."""
    return [''] + [f'data.{name}' for name in variable_names]


def _quadratic_term_names(variable_names: list[str]) -> list[str]:
    """Each product of two variables, including a variable with itself."""
    return [f'data.{first} * data.{second}' for first, second in itertools.combinations_with_replacement(variable_names, 2)]


def _term_values(term: str, demo: Demo) -> np.ndarray:
    """A term's value at each of a demo's data points."""
    values: np.ndarray = np.ones(len(demo.times))
    for factor in term.split(' * ') if term else []:
        values = values * demo.states[:, demo.variable_names.index(factor.removeprefix('data.'))]
    return values


def _add_lines(parent: ScoredProgram, variable: str, new_terms: list[str], level: Level) -> Proposal:
    """Add terms to one equation. On each demo separately, start them at the values that best explain that demo's residual."""
    lines: list[str] = parent.source.splitlines()
    new_names: list[str] = [f'new{index}' for index in range(len(new_terms))]
    for name, term in zip(new_names, new_terms):
        lines.append(f'diff.{variable} += params.{name}' + (f' * {term}' if term else ''))

    params: list[dict[str, float]] = []
    for demo, parent_params, parent_residuals in zip(level.demos, parent.params, parent.residuals):
        columns: np.ndarray = np.column_stack([trapezoid_step(_term_values(term, demo), demo.times) for term in new_terms])
        coefficients: np.ndarray = np.linalg.lstsq(columns, parent_residuals[variable], rcond=None)[0]
        params.append({**parent_params, **dict(zip(new_names, map(float, coefficients)))})
    return Proposal('\n'.join(lines), params)


def add_terms(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    """Linear regression on the residual. Proposes each missing term alone, all the linear ones together, and all of them together."""
    linear_terms: list[str] = _linear_term_names(level.variable_names)
    all_terms: list[str] = linear_terms + _quadratic_term_names(level.variable_names)
    proposals: list[Proposal] = []
    for parent in parents:
        # What each equation already has
        existing: set[tuple[str, str]] = {(split_line(line)[0], split_line(line)[2]) for line in parent.source.splitlines()}
        for variable in level.variable_names:
            missing_all: list[str] = [term for term in all_terms if (variable, term) not in existing]
            missing_linear: list[str] = [term for term in linear_terms if (variable, term) not in existing]
            bundles: list[list[str]] = [[term] for term in missing_all] + [missing_linear, missing_all]
            for bundle in bundles:
                if bundle:
                    proposals.append(_add_lines(parent, variable, bundle, level))
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


def _relation_is_close(target: str, first: str, second: str, symbol: str, sign: int, all_params: list[dict[str, float]]) -> bool:
    """Is target ≈ sign * (first (symbol) second), on EVERY demo? A coincidence on one demo shouldn't count."""
    for demo_params in all_params:
        if symbol == '/' and demo_params[second] == 0:
            return False
        if abs(demo_params[target] - sign * RELATIONS[symbol](demo_params[first], demo_params[second])) > CLOSE_FRACTION * abs(demo_params[target]):
            return False
    return True


def relate_parameters(parents: list[ScoredProgram], level: Level) -> list[Proposal]:
    """When one parameter's close to the sum/difference/product/ratio of two others, propose replacing it with that expression."""
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
            if any(abs(abs(demo_params[kept]) - abs(demo_params[replaced])) > CLOSE_FRACTION * abs(demo_params[replaced]) for demo_params in parent.params):
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
            if all(abs(demo_params[name] - 1) <= CLOSE_FRACTION for demo_params in parent.params):
                source: str = re.sub(rf'params\.{name} \* ', '', parent.source)
                params: list[dict[str, float]] = [{key: value for key, value in demo_params.items() if key != name} for demo_params in parent.params]
                proposals.append(Proposal(source, params))
    return proposals


MONKEYS: list[Monkey] = [add_terms, delete_lines, relate_parameters, snap_to_one, tie_parameters]
