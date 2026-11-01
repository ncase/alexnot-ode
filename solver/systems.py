"""The test systems: ground-truth ODEs, noisy samples of them, and the real lynx/hare data."""
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np
from scipy.integrate import solve_ivp

# Default test data settings. (Later, the fan will sweep these)
DEFAULT_SAMPLE_COUNT: int = 50
DEFAULT_NOISE_FRACTION: float = 0.03

LYNX_HARE_PATH: Path = Path(__file__).parent.parent / 'data' / 'lynx_hare.csv'


@dataclass
class System:
    name: str
    equation: str  # Human-readable ground truth, for us to compare the winning program against
    variable_names: list[str]  # The names programs see, as in `data.x`
    variable_meanings: list[str]
    derivative: Callable[[float, np.ndarray], list[float]]
    start: list[float]
    end_time: float
    sample_count: int = DEFAULT_SAMPLE_COUNT
    noise_fraction: float = DEFAULT_NOISE_FRACTION


# Coefficients are textbook-style where possible, and avoid accidental ties or 1s,
# so the tie & snap monkeys can't fire by coincidence
SYSTEMS: list[System] = [
    System(
        name='Exponential growth',
        equation="x' = 0.3x",
        variable_names=['x'],
        variable_meanings=['amount'],
        derivative=lambda time, state: [0.3 * state[0]],
        start=[1.0],
        end_time=10.0,
        noise_fraction=0.10,
    ),
    System(
        name='Exponential decay',
        equation="x' = -0.5x",
        variable_names=['x'],
        variable_meanings=['amount'],
        derivative=lambda time, state: [-0.5 * state[0]],
        start=[10.0],
        end_time=10.0,
        noise_fraction=0.10,
    ),
    System(
        name='Logistic growth',
        equation="x' = 0.8x - 0.08x²",
        variable_names=['x'],
        variable_meanings=['population'],
        derivative=lambda time, state: [0.8 * state[0] - 0.08 * state[0]**2],
        start=[0.5],
        end_time=12.0,
    ),
    # We cheat & observe velocity directly. The paper will admit this!
    System(
        name='Damped spring',
        equation="x' = y,  y' = -4x - 0.4y",
        variable_names=['x', 'y'],
        variable_meanings=['position', 'velocity'],
        derivative=lambda time, state: [state[1], -4 * state[0] - 0.4 * state[1]],
        start=[1.0, 0.0],
        end_time=12.0,
    ),
    System(
        name='Lotka-Volterra',
        equation="x' = x - 0.1xy,  y' = 0.075xy - 1.5y",
        variable_names=['x', 'y'],
        variable_meanings=['rabbits', 'foxes'],
        derivative=lambda time, state: [
            state[0] - 0.1 * state[0] * state[1],
            0.075 * state[0] * state[1] - 1.5 * state[1],
        ],
        start=[10.0, 5.0],
        end_time=13.0,
    ),
    System(
        name='SIR',
        equation="x' = -0.5xy,  y' = 0.5xy - 0.1y,  z' = 0.1y",
        variable_names=['x', 'y', 'z'],
        variable_meanings=['susceptible', 'infected', 'recovered'],
        derivative=lambda time, state: [
            -0.5 * state[0] * state[1],
            0.5 * state[0] * state[1] - 0.1 * state[1],
            0.1 * state[1],
        ],
        start=[0.99, 0.01, 0.0],
        end_time=60.0,
    ),
    # Way more samples than the others: chaos is fast, and it failed badly at 500 in our quick check
    System(
        name='Lorenz',
        equation="x' = 10y - 10x,  y' = 28x - xz - y,  z' = xy - (8/3)z",
        variable_names=['x', 'y', 'z'],
        variable_meanings=['x', 'y', 'z'],
        derivative=lambda time, state: [
            10 * (state[1] - state[0]),
            state[0] * (28 - state[2]) - state[1],
            state[0] * state[1] - (8 / 3) * state[2],
        ],
        start=[1.0, 1.0, 1.0],
        end_time=30.0,
        sample_count=1500,
    ),
]


def simulate(system: System, sample_count: int) -> tuple[np.ndarray, np.ndarray]:
    """Integrate the true ODE very accurately. Returns times, and states shaped (time, variable)."""
    times: np.ndarray = np.linspace(0, system.end_time, sample_count)
    solution = solve_ivp(system.derivative, (0, system.end_time), system.start, t_eval=times, rtol=1e-10, atol=1e-12)
    return times, solution.y.T


def add_noise(states: np.ndarray, noise_fraction: float, rng: np.random.Generator) -> np.ndarray:
    """Add Gaussian noise, scaled to each variable's own standard deviation."""
    return states + rng.normal(0, 1, states.shape) * noise_fraction * states.std(axis=0)


def noisy_samples(system: System, seed: int) -> tuple[np.ndarray, np.ndarray]:
    """What a program gets to see: sparse, noisy samples of the truth."""
    times, states = simulate(system, system.sample_count)
    return times, add_noise(states, system.noise_fraction, np.random.default_rng(seed))


def load_lynx_hare() -> tuple[np.ndarray, np.ndarray]:
    """Real data! Returns years, and states shaped (time, variable), with x = hare & y = lynx (thousands of pelts)."""
    table: np.ndarray = np.loadtxt(LYNX_HARE_PATH, delimiter=',', comments='#', skiprows=4)
    return table[:, 0], table[:, 1:]
