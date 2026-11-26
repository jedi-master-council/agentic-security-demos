# Demo 88: The Detection Confusion Matrix — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/confusion.py` (or `make demo DEMO=88` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-88-detection-confusion
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `4 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/confusion.py
```

**Expected output**:

```text
traj inj     taint mismatch  recency majority    union
r01  Y       FLAG     FLAG     FLAG     FLAG     FLAG
r02  -          -        -     FLAG        -     FLAG
r03  Y       FLAG     FLAG     FLAG     FLAG     FLAG
r04  -       FLAG        -     FLAG     FLAG     FLAG
r05  Y          -     FLAG        -        -     FLAG
r06  -          -        -        -        -        -
r07  Y       FLAG        -        -        -     FLAG
r08  -          -        -     FLAG        -     FLAG
r09  -       FLAG        -     FLAG     FLAG     FLAG
r10  Y          -        -     FLAG        -     FLAG
taint     tp 3 fp 2 fn 2 tn 3  TPR 0.60  FPR 0.40
mismatch  tp 3 fp 0 fn 2 tn 5  TPR 0.60  FPR 0.00
recency   tp 3 fp 4 fn 2 tn 1  TPR 0.60  FPR 0.80
majority  tp 2 fp 2 fn 3 tn 3  TPR 0.40  FPR 0.40
union     tp 5 fp 4 fn 0 tn 1  TPR 1.00  FPR 0.80
lesson: each structural cue misses a different attack; the union buys sensitivity with false alarms.
```

This also writes `results/detection.json`.

## Step 3 — Break It (Exercise)

Which single change to the recency rule would cut its false positives without losing a true positive?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=88
python3 tools/figures/build.py 88
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
