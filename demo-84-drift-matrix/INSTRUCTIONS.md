# Demo 84: Longitudinal Drift Matrix — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/drift.py` (or `make demo DEMO=84` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-84-drift-matrix
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `4 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/drift.py
```

**Expected output**:

```text
fw-a: elasticity 0.66 (sinks grow slower than code)
  1.0 -> 1.1: network+1                        -
  1.1 -> 1.2: shell+1 eval+1 file_write+1      REVIEW
  1.2 -> 2.0: network+2 file_write+1           -
fw-b: elasticity 1.47 (sinks grow faster than code)
  0.4 -> 0.5: shell+1                          REVIEW
  0.5 -> 0.6: network+1                        -
  0.6 -> 0.7: file_write+1                     -
fw-c: elasticity 0.44 (sinks grow slower than code)
  3.0 -> 3.1: shell-1                          -
  3.1 -> 3.2: eval+1 network+1                 REVIEW
  3.2 -> 3.3: file_write+1                     -
lesson: a release-by-release drift matrix shows where review effort is due; growth alone does not.
```

This also writes `results/drift.json`.

## Step 3 — Break It (Exercise)

Change the rule to flag any increase in network egress as well. How many transitions now need review?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=84
python3 tools/figures/build.py 84
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
