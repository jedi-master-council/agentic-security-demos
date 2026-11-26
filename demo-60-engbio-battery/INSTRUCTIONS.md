# Demo 60: Engineering-Biology Analysis Battery — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_battery.py` (or `make demo DEMO=60` from root) |
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

**Expected**: `4 passed`.

## Step 2 — Run the Demo

```bash
python3 student/run_battery.py
```

**Expected** (abridged):

```
Demo 60: scoring a synthetic engineering-biology analysis battery

  hplc-peak  predicted 2  reference 2  ok
  growth-shape  predicted flat  reference flat  ok
  construct-parts  predicted True  reference True  ok
  accuracy 1.0 (3/3)
```

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=60
python3 tools/figures/build.py 60
```

<!-- END generated: figures-step -->

## What to look for

- References sit in the fixture, not in the scorer, so the check is against a predeclared answer.
- A perfect score on three toys is not evidence about any model or laboratory workflow.
