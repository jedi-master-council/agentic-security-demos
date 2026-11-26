# Demo 18: Crosslingual Gap — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_lang.py` |
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

**Expected**: `5 passed` (determinism, English recall, non-English recall,
marker semantics, results parity).

## Step 2 — Run the Detector

```bash
python3 student/run_lang.py
```

**Expected**:

```text
payloads 10  flagged 6
id    lang  injected  flagged
en1   EN    True     True
en2   EN    True     True
en3   EN    True     True
en4   EN    True     True
es1   ES    True     True
es2   ES    True     False
zh1   ZH    True     False
zh2   ZH    False    False
ar1   AR    True     True
ar2   AR    False    False
recall EN 4/4  non-EN 2/6  total 6/10
lesson: English recall is perfect (4/4); non-English recall drops to 2/6.
```

This also writes `results/lang_gap.json`.

## Step 3 — Break It (Exercise)

Edit `es2` in `fixtures/payloads.json` to append the `[TOOL]` marker and re-run
both commands. Record: does non-English recall rise to 3/6? Why does one
language-agnostic marker help only the payloads that carry it?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=18
python3 tools/figures/build.py 18
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| Recall EN / non-EN / total | ___ / ___ / ___ |
| Commit | Git SHA or `local` |
