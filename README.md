# AlexNot-ODE

> **⚠️ This whole README was written by an LLM, not by Nicky. Nicky has not verified it in detail.** Its reasoning and its design choices are the LLM's unless stated otherwise. Don't treat them as human decisions, or as correct.

A much simpler cousin of [AlexNot](../AlexNot/), our ARC-AGI program induction solver. It evolves short programs that explain sparse, noisy time-series data as differential equations.

**Why it exists:** Universality points for the Nov 9 paper. We want to show that AlexNot's loop (monkeys propose, the scorer selects for compression) carries over from ARC grids to continuous science data, with new monkeys and no change to the loop.

**What it won't show:** that we beat SINDy. Every test system here is polynomial, degree 2 at most, so a SINDy library can represent all of them, and SINDy is faster. The paper will say so upfront.

**How we judge it:** there's no automated pass/fail. We manually inspect the winning program and check that it's the intended equation.

# Part 1: Spec

## The loop

Evolutionary search over programs, starting from the blank program, which predicts "nothing ever changes". Each round:

1. Give every parent program, its best-fit parameters, its predictions and its residuals to every monkey.
2. Each monkey proposes new programs.
3. Skip anything we've already tried.
4. Fit each new program's parameters, then score it.
5. Pick the next parents.
6. Stop after `EVO_MAX_GENERATIONS` rounds, or after `EVO_EARLY_STOP_COUNTDOWN` rounds without improvement.

**Time limits:** like AlexNot, `TIME_LIMIT_PER_LEVEL` and `TIME_LIMIT_PER_ROUND` cap the search, and it answers with whatever got scored in time. Each round scores its programs in random order, so running out of time doesn't always cut off the same monkey.

**Reasoning traces:** `solver/run_level.py` saves one to `levels/results/` for each level: the winner, 4 runner-ups, the solve time and program count, then every round's parents, with each score split into accuracy, token simplicity and parameter simplicity.

The winner is the best-scoring program ever seen. Proposing, scoring and throwing candidates away is cheap, so monkeys can be generous.

Reused from AlexNot's `search_transform.py`: remembering every tried program, dropping programs that crash (here, also any that produce NaN or infinity), and early stopping.

**Parents:** the top `PARENTS_TOP_K` programs by total score, skipping any whose score is within `SAME_SCORE_TOLERANCE` of the last parent kept, since that's just another spelling. We ablated AlexNot's per-variable island (the best program on each variable): on the 7 levels before SIR, across 20 seeds at each of 3 noise levels, it changed no result, so it's gone.

## Programs

A program is Python that gets `exec()`'d with no builtins. It receives `params` and `data`, and writes to `diff`, which starts at zero for every variable. Each term gets its own line, so evolution can edit lines independently.

```python
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y -= params.c * data.y
diff.y += params.d * data.x * data.y
```

- `diff` and `data` highlight the ODE nature of this. (`in` is a Python keyword, so `in.x` can't compile.)
- A line can have no parameter: `diff.x += data.y`.
- A parameter can appear on more than one line. That's how a tie works.
- `data.x` holds the whole time series as a numpy array, so one run computes every time point.
- Parameters get renamed `a, b, c...` in order of appearance, so the same program always has the same string.

## Parameters are separate from programs

Programs are structure, and parameters are fitted before scoring. So a structure is never judged by unlucky numbers, and monkeys never burn generations nudging decimals.

**Fitting:** nearly every program is linear in its parameters, so we nudge each parameter once to measure its effect, then solve for the best values directly with one linear least-squares solve. Only `a * b` and `a / b` relations need the slower `scipy.optimize.least_squares`, warm-started from the parent's parameters. It fits all equations together, because a tied parameter spans several equations. Each variable's residuals are divided by the blank program's root-mean-square error, so large variables can't dominate a tied fit.

**Signs:** the fit is unrestricted. After fitting, a negative parameter gets rewritten as a positive one, flipping `+=` and `-=` on every line that uses it. That way the final program reads naturally, and `+= -a` and `-= a` can't become duplicates. (We may revisit the details during implementation.)

## The trapezoid step

**ELI12:** to guess where you'll be after a trip, use the average of your speed at the start and at the end, instead of just your speed at the start.

**Details:** one helper, `trapezoid_step`, serves fitting, scoring and monkeys. For variable `x` and time step `k`, with `f` as the predicted `diff.x` at each data point:

```python
predicted_step[k] = (times[k+1] - times[k]) * (f[k] + f[k+1]) / 2
residual[k] = (data.x[k+1] - data.x[k]) - predicted_step[k]
```

- There's no chicken-and-egg problem. A parent's predictions already exist, and any candidate term can be computed directly from the data.
- The search needs no x-dot estimates. The blank program's residual is just the raw change between samples.
- It's linear in the parameters of most programs, which makes fitting a single solve. `relate_parameters` can break that (`params.a * params.b`), and those programs use `least_squares`.
- Why not Euler? See "Preliminary checks" below.

## Scoring

Lower is better. The blank program scores exactly 0.

```python
total_score = SCORE_COEFF_ACCURACY * (average over demos of (sum over variables of  log( max(MSE, MSE_FLOOR * blank_MSE) / blank_MSE )))
              + SCORE_COEFF_TOKEN * token_count
              + SCORE_COEFF_PARAMETER * parameter_count
```

- `MSE` is the mean squared `residual` for that variable. It's a mean, so accuracy doesn't grow with the number of data points.
- `blank_MSE` is the same quantity for the blank program.
- `token_count` counts regex words, so `diff.x += params.a * data.x` is 6 tokens.

**ELI12:** grade each program on how many times smaller it made the error, compared with predicting no change at all. Switching from rabbits to thousands of rabbits changes nothing, and halving the error always earns the same points. So we can read a token's price as "this term has to shrink the error by X%".

**Why the floor:** on noiseless data, the error can hit 0, and log(0) is infinite. The floor also stops tiny numerical improvements from earning points. It's set at 1e-3 because on perfect data, the intended programs' errors are the trapezoid step's own, up to about 1e-4 of the blank program's. With a floor of 1e-12, extra terms fit that error and beat the right answer on 6 of 8 levels. At 1e-3, all 8 solve. Noisy data stays far above it: the lowest error we measured from an intended program was 3.6e-2.

**Constants** (token and parameter picked by `solver/fan_scoring.py`, on exponential and logistic only; accuracy picked by Nicky from a fan on the 8 fan levels, so it's tuned on the same data it's tested on; they live as magic constants at the top of the file):

- `SCORE_COEFF_ACCURACY = 25`
- `SCORE_COEFF_TOKEN = 0.1`
- `SCORE_COEFF_PARAMETER = 0.5`
- `MSE_FLOOR = 1e-3`

## Levels

Like ARC, each level has several demos: 3 time series with specifically different coefficients and starts. `levels/generators/` writes them to `levels/timeseries/<level>.json`, and the solver only reads that JSON. One program must explain all 3 demos, with its parameters fitted separately per demo. Accuracy is averaged across demos, while tokens and parameters are counted once per program. An accidental tie or relation can't hold across all 3.

## Monkeys

Monkeys propose, and the scorer decides. Each monkey receives the parents, their fitted parameters, their predictions and their residuals, all in time order.

**`add_terms`:** the one residual monkey, running every round on every parent and variable. Its regression runs on each demo separately, but the scorer judges the program on all demos together.

- Candidates: a constant, each variable, and each product of two variables, including a variable with itself (`data.x * data.x`, which logistic growth needs).
- With three variables, that's 10 candidates per equation.
- It proposes every missing term on its own. There aren't many, and throwing candidates away is cheap, so there's no top-K limit.
- It also proposes every missing linear term + constant together, and every missing term together.
- We need both styles (see "Preliminary checks").

**`delete_lines`:** proposes removing each line, one at a time, like AlexNot's `compression.delete_lines`. This replaces "drop small parameters", because raw size is misleading: an essential `x*y` coefficient looks tiny when `x*y` is large.

**`snap_to_one`:** when a parameter is close to 1 in absolute value, proposes removing it, so `diff.x += params.a * data.y` becomes `diff.x += data.y`. The sign rewriting covers -1.

**`tie_parameters`:** when two parameters are close in absolute value on every demo, with the same signs or opposite signs on every demo, proposes making them one parameter, flipping the replaced one's lines if their signs are opposite. It refuses to tie two parts of one relation, like `a - a`, or to flip a line with a relation in it. We tried relaxing this to "close on any demo": it added about 35% more programs on Lotka-Volterra, lost a seed on 4 noise settings, and didn't help SIR. SIR needs this, because the flow out of Susceptible has to exactly match the flow into Infected:

```python
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
```

**`relate_parameters`:** when one parameter is close to the sum, difference, product or ratio of two others (or the negative of a sum, product or ratio) on every demo, proposes replacing it with that expression. That's one less parameter to pay for, at the price of a few more tokens. Bass needs this for `q - p`, and Michaelis-Menten needs it for `k₂ + k₃`:

```python
diff.x += params.a
diff.x += (params.b - params.a) * data.x
diff.x -= params.b * data.x * data.x
```

"Close" for `snap_to_one`, `tie_parameters` and `relate_parameters` means the same sign, with the bigger number under `1 + CLOSE_FRACTION` times the smaller one. `CLOSE_FRACTION = 0.2` is a starting guess. It only filters proposals, so being generous is safe. The scorer may still accept a coincidence, if the fit barely gets worse, so `relate_parameters` is the monkey to watch for false positives.

## Test data

Generated by integrating each system accurately, sampling it, and adding Gaussian noise scaled to each variable's standard deviation. Time steps may be uneven in real data, so nothing assumes even spacing.

**Defaults:** 50 samples and 3% noise, except 10% for the exponentials, which looked too smooth at 3%. A later "fan" sweeps noise and sample spacing for the paper. Each system gets a graph of ground truth against noisy samples, so we can see what the program sees.

Coefficients are common textbook-style values where they exist, chosen to avoid accidental ties or 1s, so `tie_parameters` and `snap_to_one` can't fire by coincidence.

**Watch the time step!** The trapezoid step has its own error, which is systematic, so extra terms can fit it and win. If it's a real share of the total error, *less* noise gives *worse* results. On one drag demo it was 81% of the error at 5% noise, and shorter time ranges fixed it. Check this for every new level.

1. **Exponential growth:** `x' = 0.3x`, start 1, time 0–10
2. **Exponential decay:** `x' = -0.5x`, start 10, time 0–10
3. **Logistic growth:** `x' = 0.8x - 0.08x²` (r = 0.8, K = 10), start 0.5, time 0–12
4. **Damped spring:** `x' = y`, `y' = -4x - 0.4y` (k = 4, c = 0.4, m = 1), start (1, 0), time 0–12
5. **Lotka-Volterra:** `x' = x - 0.1xy`, `y' = 0.075xy - 1.5y`, start (10, 5), time 0–13 (two cycles)
6. **SIR:** `x' = -βxy`, `y' = βxy - γy`, `z' = γy`. Three demos, (β, γ, start, end time): (0.5, 0.1, (0.99, 0.01, 0), 60), (0.3, 0.05, (0.95, 0.05, 0), 100), (0.8, 0.25, (0.98, 0.02, 0), 35)
7. **Lorenz (stretch):** σ = 10, ρ = 28, β = 8/3, start (1, 1, 1), time 0–30, 1,500 samples

**All variables are observed.** For the damped spring, that means velocity is measured directly. It's a cheat, and the paper will admit it. In general, `y' = a*x + b*y` has `a = -k/m` and `b = -c/m`.

**Real data (stretch):** the Hudson's Bay lynx and hare pelt counts, 1900–1920, in `data/lynx_hare.csv`. It has only 21 points. Other versions of this table exist (Gilpin's differs), so the paper should cite this one specifically. Real SIR data is skipped: the classic 1978 boarding-school flu data only records students in bed, so S and R are hidden.

**Stretch systems** (not built yet; coefficients to be picked when we get there; equations written from memory, so check them against the original papers before citing):

- **Bass diffusion (economics/marketing):** `x' = (p + qx)(1 - x) = p + (q - p)x - qx²`, where x is the fraction of people who've adopted a product. It's logistic growth plus a constant term (`p`, adoption from ads rather than from other people). That means it can take off from x = 0, where logistic growth stays stuck forever. It's the only system here that needs the constant term.
- **Goodwin growth cycle (economics):** `x' = (1/σ - α - β)x - (1/σ)xy`, `y' = ρxy - (α + γ)y`, where x is the employment rate and y is the workers' share of income. It has the same shape as Lotka-Volterra, so it adds a new field but no new challenge.
- **Michaelis-Menten, full form (biochemistry):** `s' = -k₁es + k₂c`, `e' = -k₁es + (k₂ + k₃)c`, `c' = k₁es - (k₂ + k₃)c`, `p' = k₃c`. A workout for `tie_parameters`, and the hardest system: 4 variables, 15 candidate terms, and conserved quantities like SIR. It comes after Lorenz.

## Setup

Own `.venv` with numpy, scipy and matplotlib. No system packages.

## Build order

1. ✅ This spec.
2. ✅ Generate the example systems with graphs (`solver/systems.py`, `solver/plot_systems.py`, `plots/systems.png`), and grab the lynx/hare data.
3. Make it solve the systems, simplest first: exponential ✅, logistic ✅, Bass ✅, Newton's law of cooling ✅ (`x' = k*room - k*x`), falling with air drag ✅ (`v' = g - k*v²`), damped spring ✅, Lotka-Volterra ✅ (all at 10% noise, run with `solver/run_level.py`; actual demo settings are in `levels/generators/`), SIR, then Lorenz. Stretch system after that: Michaelis-Menten. That's 10 levels. (Skipping Goodwin, since it has the same shape as Lotka-Volterra. Exponential growth & decay are one level, since their demos share one program.)
4. Run the noise and sparsity fan and the lynx/hare attempt, and make the paper figures.

## Known risks

- **Parents might be too greedy.** In the quick checks, single terms and the full set each won on different systems, but those ran as two separate searches. In the real population, a path that looks good early could push out the one that wins later. If so, raise `PARENTS_TOP_K`.
- **SIR is degenerate.** S+I+R is constant, so its 10 candidate terms only have rank 6, and many coefficient combinations fit equally well. The fit on the full set of terms is arbitrary until deletion narrows it down.
- **Score weights are barely tested.** `solver/fan_scoring.py` has only fanned them on exponential and logistic, which have too few terms to show much overfitting.

# Part 2: Paper notes

## Framing

- The claim is generality: the same loop solves ARC puzzles and recovers ODEs.
- SINDy's regression could fit inside AlexNot as a monkey, but AlexNot's loop can't fit inside SINDy.
- The fair caveat: the loop generalizes, but every new domain needs new monkeys. `add_terms` is very close to SINDy's regression.
- We're probably slower than SINDy. Absolute times should still be small, but we haven't measured them. The ratio could be well above 10×, since we fit many candidates.
- No head-to-head with SINDy. The paper just says SINDy can do all this faster, with a citation, because the point is that AlexNot generalizes and SINDy wouldn't the other way.
- For each equation, the paper shows the hardest noise and sparsity where it still works, with the full fan reported separately or in an addendum. "Still works" should mean across many seeds, not one lucky run. We'll pick the threshold once we see the fan.
- Lorenz gets a 3D butterfly plot (`plots/lorenz_butterfly.png`).

## How SINDy works

SINDy (Brunton, Proctor & Kutz, 2016) isn't evolutionary or brute force, and doesn't really search over programs. It assumes the true equation is a sparse weighted sum of terms from a fixed library. Then, usually via sequentially thresholded least squares, for each equation:

1. Estimate derivatives from the data.
2. Fit every library term at once.
3. Zero out the coefficients below a threshold.
4. Refit the survivors, and repeat until it settles.

PySINDy's `STLSQ` defaults to a threshold of 0.1 and at most 20 iterations, with column normalization off.

The library can include trigonometric terms as well as polynomials ("constant, polynomial, and trigonometric terms"). The authors also stress that it needs "the right coordinates and function basis".

## Comparison with SINDy

**Where our approach is stronger:**

- **Generality:** the loop doesn't require programs to be weighted sums of fixed terms, so it also runs on ARC's discrete, sequential programs. SINDy's core trick doesn't carry over to those.
- **Simplicity is scored directly:** tokens and parameters are priced in one score, rather than judged through a coefficient-size threshold.
- **Discovered structure:** monkeys can find ties and exact constants from a parent's fit. Constrained SINDy variants exist, but as far as we recall, the constraints are specified upfront. (From memory; check before citing.)
- **No derivative estimates:** the search uses trapezoid steps. Note that weak-form SINDy also avoids pointwise derivatives, so this isn't unique to us.

**Where SINDy is stronger:**

- **Speed:** a bare-bones numpy version of its core loop took 0.26 ms per run on Lotka-Volterra (30 samples, 6 candidate terms). That measures speed only, not whether it chose the right terms.
- **Simplicity of the method:** a few lines of linear algebra, rather than a population and several monkeys.
- **Maturity:** a decade of variants and a maintained library.
- **Expressiveness on our test set:** we can't express anything here that a SINDy library couldn't.

## SINDy speed

- Our bare-bones timing: 0.26 ms per run (see above).
- Ensemble-SINDy reports "only seconds" for a model plus coefficient and inclusion probabilities, compared with "several hours of CPU time" for Bayesian MCMC methods.
- ⚠️ Kumar & Sumitra (2026) report SINDy at 1.2 s and PySR at 24.6 s. We could only read a search snippet, so **check this before citing**.
- ⚠️ The Chaos benchmark paper reports PySR at a median of 1400 ± 60 s per system on one core. This is also from a snippet, with a different setup, so it isn't directly comparable.

## SINDy successes

**On real data:**

- **Lynx and hare:** Ensemble-SINDy recovered Lotka-Volterra from 21 yearly pelt counts (1900–1920), using a polynomial library up to third order. The paper reports coefficient uncertainty and inclusion probabilities, but no numeric error metric for this case.

**On simulations (not real measurements):**

- **Cylinder wake:** the original paper's vortex shedding example comes from a simulated 2D Navier–Stokes flow.
- ⚠️ **Plasma:** Alves & Fiuza recovered plasma equations from particle simulations, with about 1–4% coefficient error. Snippet only.

**Other reported applications (⚠️ from search snippets, unverified):**

- Reactive SINDy, for finding chemical reactions from concentration data.
- SINDy-PI, for rational dynamics like Michaelis-Menten enzyme kinetics.
- DF-SINDy, a derivative-free variant for noisy kinetics data.

## SINDy weaknesses

- It's noise-sensitive, because it relies on estimated derivatives. Smoothing helps, but adds its own bias and tuning.
- That has prompted weak-form and ensemble variants. Ensemble-SINDy reports handling more than twice the noise previously reported for PDE discovery.
- It can't find a term that's missing from its library.
- ⚠️ One comparison of five methods found PySR recovered the correct form on all nine dynamical systems it tested. Snippet only.

## How empirical are our test systems?

⚠️ Mostly from search snippets and secondary sources, plus some background from memory. Check before citing. Roughly from most to least empirically supported:

- **Damped spring and exponential decay:** solid physics in their proper range, like small stretches or radioactive decay. Exponential growth only holds until something runs out. (From memory.)
- **Michaelis-Menten:** built on lab measurements of invertase in 1913, and a modern refit of the original data found them surprisingly precise. The steady-state derivation came later (Briggs & Haldane, 1925).
- **Bass:** starts from a behavioral story, but it's mainly supported by fits to real sales. Reviews call it an "empirical generalization", with average p = 0.03 and q = 0.38 across studies. Those are pooled averages, though, and forecasts are sensitive to the p and q you pick.
- **Logistic:** fits Gause's lab Paramecium closely (about 97%, with hand-picked values), under steady food.
- **SIR:** Kermack & McKendrick's 1927 Bombay plague fit "conforms roughly". Bacaër argues the constant parameters are unrealistic, and that the epidemic was really seasonal.
- **Lotka-Volterra:** qualitative at best. Gause's predators wiped out their prey and then starved, and Huffaker's mites needed a complex environment to coexist. Real hare cycles depend on both food and predation.
- **Goodwin:** theory first. The cycle shape shows up in many datasets, but the numbers usually don't fit, and overall evidence is mixed.
- **Lorenz:** not empirical. It's a drastic simplification of convection. The same equations do describe an idealized single-mode laser and a purpose-built waterwheel.

**For the paper:** recovering Lotka-Volterra from lynx/hare would show that it's a good compressed description of that data, not that it's the true mechanism.

## Preliminary checks

⚠️ These came from throwaway scripts: one parent, per-equation greedy search, untuned weights. They shaped the spec, but they aren't paper results, and the real system needs re-running.

**Euler vs trapezoid.** Worst coefficient error on Lotka-Volterra (α = 1.1, β = 0.4, γ = 0.4, δ = 0.1), fitting only the correct terms, at 3% noise, median of 100 seeds:

- **20 samples:** Euler 40%, average slope 35%, trapezoid 19%
- **30 samples:** Euler 26%, average slope 17%, trapezoid 8%
- **50 samples:** Euler 13%, average slope 7%, trapezoid 4%

Noiseless runs were almost identical, so at this noise level, time-step error matters far more than noise.

**Single terms vs the full set.** Exact recovery at 3% noise, out of 20 seeds, with the coefficients in this spec:

- **Lotka-Volterra, 50 samples:** one term at a time got 3/20, all terms then delete got 19/20.
- **SIR, 50 samples:** one term at a time got 20/20, all terms then delete got 2/20.
- **Keeping whichever scored better, per equation:** Lotka-Volterra got 19/20, SIR got 20/20.

**How many samples?** Exact recovery, keeping whichever scored better:

- **Exponential and logistic:** 20/20 at 20, 30 and 50 samples.
- **Damped spring:** 4/20 at 20 samples, 18/20 at 30, 20/20 at 50.
- **Lotka-Volterra:** 0/20 at 20 samples, 1/20 at 30, 19/20 at 50. At 30 samples, the true equation only scored best in 6/20 seeds, so better search can't fix that.
- **SIR:** 14/20 at 20 samples, 20/20 at 30 and 50.
- **Lorenz, over 30 time units:** 0/20 at 500 samples. At 1,500 samples, each style alone got 20/20.

## Sources

- [Brunton, Proctor & Kutz 2016, original SINDy paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4839439)
- [Fasel et al. 2022, Ensemble-SINDy](https://pmc.ncbi.nlm.nih.gov/articles/PMC9006119/)
- [PySINDy STLSQ docs](https://pysindy.readthedocs.io/en/latest/generated/pysindy.optimizers.STLSQ.html)
- [Toolkit for equation discovery in high-noise regimes](https://arxiv.org/pdf/2111.04870)
- [Weak SINDy and test functions (Fourier Weak SINDy)](https://arxiv.org/pdf/2604.20141)
- ⚠️ [Kumar & Sumitra 2026, runtime comparison](https://arxiv.org/pdf/2609.01102)
- ⚠️ [Chaos as an interpretable benchmark, PySR timing](https://arxiv.org/pdf/2110.05266)
- ⚠️ [Comparison of five methods on dynamical systems](https://arxiv.org/pdf/2508.20257v2)
- ⚠️ [Alves & Fiuza, sparse regression on plasma simulations](https://arxiv.org/pdf/2004.08424v1)
- ⚠️ [PySINDy paper, citing Reactive SINDy](https://joss.theoj.org/papers/10.21105/joss.02104.pdf)
- ⚠️ [DF-SINDy abstract, AIChE 2023](https://proceedings.aiche.org/conferences/aiche-annual-meeting/2023/proceeding/paper/199f-learning-kinetic-models-data-using-derivative-free-sparse-identification-method-and-domain)

**Empirical support for the test systems (⚠️ all secondary or snippet-level):**

- [Mahajan, Muller & Bass 1995, Bass as an empirical generalization](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.14.3.G79)
- [Massiani & Gohs, sensitivity to Bass p and q](https://iris.unive.it/bitstream/10278/3664720/2/bassCoefficients%20v3%20%2829%20mars%202015%29%20xArca.pdf)
- [Citing study reporting Sultan, Farley & Lehmann's averages](https://ideas.repec.org/p/ems/eureri/1012.html)
- [García Molina & Herrera Medina 2010, Goodwin evidence, summarizing Harvie 2000](https://revistas.unal.edu.co/index.php/ceconomia/article/view/18570)
- [Veneziani et al., mixed Goodwin evidence](https://mpra.ub.uni-muenchen.de/30444/1/MPRA_paper_30444.pdf)
- [Huffaker's mite experiment](https://en.wikipedia.org/wiki/Huffaker%27s_mite_experiment)
- [Beals & Gross, Lotka-Volterra teaching module](https://lgross.utk.edu/bioed/bealsmodules/predator-prey.html)
- [Krebs et al. 2018, the snowshoe hare cycle](https://zendy.io/title/10.1111/1365-2656.12720)
- [gauseR vignette, Gause's data](https://cran.r-project.org/web/packages/gauseR/vignettes/gauseR_examples.html)
- [Sulsky handout, Kermack & McKendrick's plague fit](https://math.unm.edu/%7Esulsky/mathcamp/ApplyData.pdf)
- [Bacaër 2012, the Bombay plague critique](https://www.documentation.ird.fr/hor/fdi:010054339)
- [Johnson & Goody, Michaelis-Menten translation and refit](https://pmc.ncbi.nlm.nih.gov/articles/PMC3381512)
- [Lorenz system overview](https://wikiwand.com/en/articles/Lorenz_system)

**Data sources:**

- [Stan case study, lynx/hare data](https://mc-stan.org/learn-stan/case-studies/lotka-volterra-predator-prey.html)
- [Odum-attributed lynx/hare table](https://gist.github.com/mages/1f0f0d5bbe50af81cc19)
- [Lecture note on Gilpin's version of the data](https://ndsu.edu/pubweb/~novozhil/Teaching/484%20Data/14.pdf)
- [Boarding-school data repository (not used)](https://awesome.ecosyste.ms/projects/github.com%2Fbenmaier%2Fboarding_school_sir)
