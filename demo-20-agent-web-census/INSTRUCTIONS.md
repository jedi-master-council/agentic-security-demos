# Demo 20: Agent Web Census — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_web.py` |
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

**Expected**: `5 passed` (determinism, adoption 4/10, injections low-pop,
helper definitions, results parity).

## Step 2 — Run the Census

```bash
python3 student/run_web.py
```

**Expected**:

```text
sites 10  adopting 4/10  exposed 2/10
id   popularity  adopted  exposed
s01  high       True     False
s02  high       True     False
s03  medium     True     False
s04  low        True     True
s05  low        False    True
s06  high       False    False
s07  medium     False    False
s08  medium     False    False
s09  low        False    False
s10  low        False    False
lesson: adoption 4/10; injections 2/10, both on low-popularity sites.
```

This also writes `results/web_census.json`.

## Step 3 — Break It (Exercise)

Give site `s06` in `fixtures/sites.json` `"llms_txt": true` and re-run both
commands. Record: does adoption rise to 5/10? Does exposure change? Why are the
two tallies independent?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=20
python3 tools/figures/build.py 20
```

## Step G — Run the Current Procedure (Simplified)

The research procedure for this topic has changed since the first version of this demo. This step teaches the current version.

```bash
python3 student/soft404_gate.py
python3 -m pytest tests/test_current_procedure.py -v
```

**Expected output**:

```text
h01 top      status 200  -> agent-file
h02 top      status 200  -> soft-404
h03 top      status 200  -> agent-file
h04 top      status 404  -> no-200
h05 top      status 200  -> agent-file
h06 top      status 200  -> soft-404
h07 unranked status 200  -> soft-404
h08 unranked status 200  -> soft-404
h09 unranked status 200  -> agent-file
h10 unranked status 200  -> soft-404
h11 unranked status 301  -> no-200
h12 unranked status 200  -> soft-404
top     : naive adoption (200s) 5/6  gated adoption 3/6  soft-404 share of 200s 2/5
unranked: naive adoption (200s) 5/6  gated adoption 1/6  soft-404 share of 200s 4/5
lesson: a status code is a claim by the server; read the bytes before counting adoption.
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| Adopting / Exposed | ___ / ___ |
| Exposed sites | ___ |
| Commit | Git SHA or `local` |
