# Demo 16: Infection Spread — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_spread.py` |
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

**Expected**: `5 passed` (determinism, uncontained 6/6, chain containment 2/6,
chain R0, results parity).

## Step 2 — Run the Spread

```bash
python3 student/run_spread.py
```

**Expected**:

```text
p 0.9  seed 16
topo   r0    infected  contained
chain  1.50  6/6       2/6
star   1.50  6/6       -
mesh   2.70  6/6       -
tree   1.50  6/6       -
lesson: uncontained spread reaches 6/6 everywhere; blocking 4 chain edges holds the chain at 2/6.
```

This also writes `results/spread.json`.

## Step 3 — Break It (Exercise)

Remove one edge from `chain_blocked_edges` in `fixtures/graphs.json` (keep 3 of
4) and re-run both commands. Record: how many nodes does the chain infect now?
Why does a single unblocked bridge undo containment on a chain?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=16
python3 tools/figures/build.py 16
```

## Step G — Run the Current Procedure (Simplified)

The research procedure for this topic has changed since the first version of this demo. This step teaches the current version.

```bash
python3 student/relay_control.py
python3 -m pytest tests/test_current_procedure.py -v
```

**Expected output**:

```text
model arm        instructed  control  instruction effect
m1    none            7/10     6/10        +0.10
m2    none            5/10     5/10        +0.00
m3    none            8/10     4/10        +0.40
m1    boundary        2/10     5/10        -0.30
m2    boundary        1/10     4/10        -0.30
m3    boundary        3/10     4/10        -0.10
lesson: compare with an uninstructed code in the same position; most of the 'spread' is ordinary copying, and a boundary mechanism can push the instructed reach below it.
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| R0 (chain) | ___ |
| Uncontained / Chain contained | ___ / ___ |
| Commit | Git SHA or `local` |
