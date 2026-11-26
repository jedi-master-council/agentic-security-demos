# Demo 56: Learning Performance Meta-analysis — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_meta.py` (or `make demo DEMO=56` from root) |
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
python3 student/run_meta.py
```

**Expected** (abridged):

```
Demo 56: fixed-effect mean on synthetic study rows

  k 4  mean 0.3448  se 0.0788  Q 2.1207 (df 3)
```

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=56
python3 tools/figures/build.py 56
```

<!-- END generated: figures-step -->

## What to look for

- S4 (yi=0.40, vi=0.01) is the most precise row and pulls the mean toward 0.40.
- Q being positive only says the four toys are not identical; it is not a finding about the literature.
