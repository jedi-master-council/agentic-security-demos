# Demo 33: Protocol Coverage — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_coverage.py` (or `make demo DEMO=33` from root) |
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

**Expected**: `5 passed` (determinism, 2/6 gaps, 4 covered, gap rule,
results parity).

## Step 2 — Run the Coverage Map

```bash
python3 student/run_coverage.py
```

**Expected**:

```text
element       mitigation  attack  gap
authorisation True        False   False
discovery     False       True    True
identity      True        True    False
session       True        True    False
streaming     False       True    True
transport     True        False   False
gaps 2/6: discovery,streaming
```

This also writes `results/coverage.json`.

## Step 3 — Break It (Exercise)

Give `streaming` `stated_mitigation: true` in `fixtures/elements.json` and
re-run both commands. Record: do gaps drop to 1/6? Does the lesson survive
with only discovery exposed? Why does one mitigation not fix the method?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=33
python3 tools/figures/build.py 33
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| Gaps | ___ /6 |
| Gap ids | ___ |
| Commit | Git SHA or `local` |
