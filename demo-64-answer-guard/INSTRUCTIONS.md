# Demo 64: Socratic Answer Guard — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/guard.py` (or `make demo DEMO=64` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-64-answer-guard
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `3 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/guard.py
```

**Expected output**:

```text
threshold  answers let through  helpful hints blocked
      0.3                 0.00                   0.67
      0.5                 0.17                   0.33
      0.7                 0.33                   0.00
      0.9                 0.83                   0.00
lesson: no threshold gives both zero leaks and zero over-blocking; choose the operating point on purpose.
```

This also writes `results/guard_calibration.json`.

## Step 3 — Break It (Exercise)

Add a threshold of 0.65 to the fixture. Which operating point would you register before running the study, and why?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=64
python3 tools/figures/build.py 64
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
