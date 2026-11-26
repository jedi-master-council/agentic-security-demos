# Demo 57: HE Governance Corpus Coding — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_coding.py` (or `make demo DEMO=57` from root) |
| **Total** | **~5 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic JSON.

## Step 0 — Environment Check

```bash
python3 --version          # must be 3.11 or newer
```

## Step 1 — Run the Tests

From this directory:

```bash
python3 -m pytest tests/ -v
```

**Expected**: `3 passed`.

## Step 2 — Run the Demo

```bash
python3 student/run_coding.py
```

**Expected** (abridged):

```
Demo 57: double-coding a synthetic governance excerpt

  documents 6  invalid codes 0
  percent agreement 0.6667
  Cohen kappa 0.5714
```

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=57
python3 tools/figures/build.py 57
```

<!-- END generated: figures-step -->

## What to look for

- Four of six pairs match (p1, p2, p4, p6).
- p3 and p5 disagree by one step on the ordinal scale.
- Kappa is lower than 4/6 because some chance agreement is expected.
