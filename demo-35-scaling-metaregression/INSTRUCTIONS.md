# Demo 35: Scaling Metaregression — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_meta.py` (or `make demo DEMO=35` from root) |
| Record results | 5 min | Fill reproducibility table below |
| **Total** | **~10 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic JSON.

---

## Step 0 — Environment Check

```bash
python3 --version          # must be 3.11 or newer
```

**Expected**: `Python 3.11.x` (or higher).

## Step 1 — Run the Tests

From this directory:

```bash
python3 -m pytest tests/ -v
```

**Expected**: `5 passed` (determinism, benchmark means, scale means, gap
dominance, results parity).

## Step 2 — Run the Meta-Analysis

```bash
python3 student/run_meta.py
```

**Expected**:

```text
benchmark A mean 0.650 (n=4)
benchmark B mean 0.345 (n=6)
bench gap 0.305
scale small mean 0.464 (n=5)
scale large mean 0.470 (n=5)
scale gap 0.006
lesson: benchmark explains more than scale.
```

This also writes `results/meta.json`.

## Step 3 — Break It (Exercise)

Change `r10` to `benchmark: A` in `fixtures/results.json` and re-run both
commands. Record: does the benchmark gap shrink? Does the scale gap move?
Why does relabelling one row shift the lesson?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=35
python3 tools/figures/build.py 35
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| Bench gap / Scale gap | ___ / ___ |
| Commit | Git SHA or `local` |
