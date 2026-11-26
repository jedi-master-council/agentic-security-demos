# Demo 24: Delegation Checks — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_authz.py` (or `make demo DEMO=24` from root) |
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

**Expected**: `5 passed` (determinism, 4 clean, 2 pinned violations,
end-to-end counts, results parity).

## Step 2 — Run the Checker

```bash
python3 student/run_authz.py
```

**Expected**:

```text
delegation checks (seed 24): 6 chains
chain  verdict
c1     clean
c2     clean
c3     clean
c4     clean
c5     audience-mismatch: expected all 'shop' got ['shop', 'evil']
c6     scope-amplification at hop 1: 2->5
lesson: 4 clean, 2 violations (c5 audience, c6 scope).
```

This also writes `results/authz.json`.

## Step 3 — Break It (Exercise)

Change `c4`'s second hop scope from 2 to 3 in `fixtures/chains.json`
(equal audience, growing scope) and re-run both commands. Record: which
property fires now? Why is equal-scope delegation allowed but any growth
a violation?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=24
python3 tools/figures/build.py 24
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| Clean / Violations | ___ / ___ |
| c5 failure / c6 failure | ___ / ___ |
| Commit | Git SHA or `local` |
