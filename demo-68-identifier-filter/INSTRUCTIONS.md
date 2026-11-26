# Demo 68: Identifier Filter — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_idfilter.py` (or `make demo DEMO=68` from root) |
| Record results | 5 min | Fill in the reproducibility table below |
| **Total** | **about 10 min** | |

**Safety**: fully offline, standard library only. Every fixture is synthetic JSON and is labelled as such.

## Step 0 — Environment check

```bash
python3 --version          # 3.11 or newer
```

## Step 1 — Run the tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: all tests pass.

## Step 2 — Run the demonstration

```bash
python3 student/run_idfilter.py
```

This prints one line per case and writes `results/idfilter.json`.

## Step 3 — Break it (exercise)

Change one labelled entry in `fixtures/messages.json` and re-run both commands. Record which printed line moved and why.

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=68
python3 tools/figures/build.py 68
```

<!-- END generated: figures-step -->

## Reproducibility table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | ___ passed / ___ failed |
| Lines printed | ___ |
| Commit | Git SHA or `local` |
