# Demo 61: Re-execution Checks — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/reexec.py` (or `make demo DEMO=61` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-61-reexecution-checks
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `3 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/reexec.py
```

**Expected output**:

```text
run  finishes  numbers traced  answer correct  reading
r1   NO       0/3             yes             steps do not re-run
r2   yes      3/3             yes             right, and for the right reason
r3   yes      2/3             no              wrong and untraceable
r4   yes      2/3             yes             right answer, untraceable number
r5   yes      3/3             yes             right, and for the right reason
r6   yes      3/3             no              traceable but wrong
lesson: score the analysis, not only the answer; a report can be right for the wrong reason.
```

This also writes `results/reexecution.json`.

## Step 3 — Break It (Exercise)

Change `r4` so that it computes the ratio it reports. Which reading does it move to? Then add a run whose steps re-run and trace but use the wrong input column.

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=61
python3 tools/figures/build.py 61
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
