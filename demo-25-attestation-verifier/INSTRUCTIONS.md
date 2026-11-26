# Demo 25: Attestation Verifier — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_verify.py` (or `make demo DEMO=25` from root) |
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

**Expected**: `5 passed` (determinism, fail-closed 6/10 blocked, fail-open
6 warnings, spot checks, results parity).

## Step 2 — Run the Verifier

```bash
python3 student/run_verify.py
```

**Expected**:

```text
attestation screen (seed 25): 10 packages
policy       blocked  warned  allowed
fail-closed  6/10        0/10       4/10
fail-open    0/10        6/10       10/10
lesson: fail-closed blocks 6/10 unattested; fail-open warns instead.
```

This also writes `results/attest.json`.

## Step 3 — Break It (Exercise)

Flip `p05` to `"attested": true` in `fixtures/packages.json` and re-run
both commands. Record: which two cells of the table move? Why does one
fixture change move both policies' rows at once?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=25
python3 tools/figures/build.py 25
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| Fail-closed blocked / Fail-open warned | ___ / ___ |
| Commit | Git SHA or `local` |
