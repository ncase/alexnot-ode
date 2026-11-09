# AlexNot-ODE

> ⚠️ **This is fully vibe-coded slop.** A toy side-experiment, written almost entirely by an LLM. Don't trust it without checking.

A tiny spin-off of [AlexNot](https://github.com/ncase/alexnot): the same "search for the simplest program that fits the data" idea,
but for finding differential equations (ODEs) from sparse, noisy time series, instead of solving ARC puzzles.
Results are in [`FINAL_WRITEUP.md`](FINAL_WRITEUP.md).

## Run it locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Make the noisy copies of each level (levels/timeseries/fan/, not in git)
.venv/bin/python levels/generators/generate_fan.py

# Find the equations for one or more levels (or leave the names off for all of them).
# Prints each winner, and saves a full trace to levels/results/
.venv/bin/python solver/run_level.py sir lotka_volterra
```

Levels: `exponential`, `newton`, `lotka_volterra`, `sir`, `drag`, `spring`, `logistic`, `bass`, `lorenz`, and the real
lynx & hare data (`lynx_hare`, in `data/`).

## License

CC0 (see `LICENSE`). The lynx & hare data is Hudson's Bay Company pelt counts (sources at the top of `data/lynx_hare.csv`).
