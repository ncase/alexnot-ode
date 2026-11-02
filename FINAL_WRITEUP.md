# AlexNot-ODE: Final Results

AlexNot-ODE finds ODEs from sparse, noisy data, using an evolutionary program search selected by compression.
It's a toy experiment, to show that an AlexNot-style architecture *can* generalize to real-world tasks.

Score, lower's better: `accuracy * log-error ratio + token * tokens + parameter * parameters`. Settings below are written as accuracy / token / parameter.
"Solved" means the winner is the exact intended program, or scores the same as it. Each noise level (1, 5, 10, 20%) has 20 seeds, so each level is out of 80.

## Main solver: 40 / 0.1 / 0.5, 50 samples per demo

**562/640 solved (88%) on 8 levels.** Solved out of 20, at 1 / 5 / 10 / 20% noise:

- Exponential: 20, 20, 20, 20 (80)
- Newton: 20, 20, 20, 20 (80)
- Lotka-Volterra: 20, 20, 20, 20 (80)
- SIR: 19, 19, 19, 17 (74)
- Drag: 20, 20, 19, 8 (67)
- Spring: 3, 20, 20, 20 (63)
- Logistic: 20, 20, 20, 0 (60)
- Bass: 20, 20, 18, 0 (58)

Traces for each level are in `levels/results/`, on 5% noise, seed 0. All 8 of those traces end on the intended program.

## Real lynx & hare data: 21 samples, 1 demo

- **Main settings fail:** the winner has all 4 Lotka-Volterra terms plus 5 extras, which is overfitting (`levels/results/lynx_hare.md`).
- **25 / 1 / 0.5 finds the structure:** the winner is `x += a*x | x -= b*x*y | y += b*x*y | y -= y`, and all of the top 6 programs are Lotka-Volterra-shaped. The version with 4 separate numbers comes #6, 2.38 points behind.
- **This is one result, not a success rate:** there's one dataset, and the search has a fixed seed.
- **This is a spark, not a validation:** the setting was picked on this same data. In a grid search, 56 of 298 settings won with a Lotka-Volterra shape.

## Synthetic levels at 25 / 1 / 0.5

**At 50 samples: 329/640.** So this setting does much worse than main at the same sample count.

**At 21 samples, as sparse as the real data: 411/640.** Solved out of 20, at 1 / 5 / 10 / 20% noise:

- Exponential: 20, 20, 20, 20 (80)
- Newton: 20, 20, 20, 19 (79)
- Lotka-Volterra: 2, 19, 20, 19 (60)
- Logistic: 20, 20, 17, 0 (57)
- Drag: 20, 20, 13, 0 (53)
- SIR: 0, 17, 18, 17 (52)
- Spring: 0, 2, 18, 10 (30)
- Bass: 0, 0, 0, 0 (0)

These levels have 3 demos, where the real data has 1. Main settings haven't had a full run at 21 samples, so this doesn't compare directly with 562.
Main settings at 20 samples got 266/640, but that run stopped each level at its first 0/20, so it's a lower bound.

## Lorenz: stretch level, 40 / 0.1 / 0.5, 50 samples

**Exact form in 4/80 (5%).** It can find the exact equation from noisy data, but not reliably. Lorenz isn't one of the 8 levels above.

- Exact form, at 1 / 5 / 10 / 20% noise: 0, 0, 3, 1
- Right 7 terms & nothing extra, with exact winners included, at 5 / 10 / 20% noise: 8, 9, 2. This wasn't counted at 1%.

## Where things are

- `levels/results/`: traces for the main settings. `lorenz.md` is from the same solver code, and wasn't rerun.
- `levels/plots/`, `plots/systems.png`: data plots, with lines at 0.15 opacity, so you can see how sparse the dots are.
- `21-sample/`: the 21-sample data, scripts & logs. `other_logs/` backs the other numbers here (`run_accuracy.log`'s `ACCURACY 40` block is the 562).
- `_old.md`: LLM-generated speculation. Don't cite it.

To rerun the 21-sample tests, from the root: `PYTHONPATH=solver python 21-sample/rank_no_stop.py --levels sir --coeffs 25 1 0.5 --fan-path 21-sample/data/other_levels`
