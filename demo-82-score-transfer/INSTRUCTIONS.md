# Demo 82: Guardrail Score Transfer — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/transfer.py` (or `make demo DEMO=82` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-82-score-transfer
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `5 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/transfer.py
```

**Expected output**:

```text
model family          bench rank  replay rank
g1    content-safety  0.94  1    0.41   5
g2    content-safety  0.90  2    0.38   6
g3    content-safety  0.86  3    0.45   4
g4    injection       0.78  4    0.83   1
g5    injection       0.71  5    0.76   2
g6    injection       0.62  6    0.71   3
Spearman rho = -0.71
cross-tab (replay pass at block share >= 0.7): {'top|pass': 0, 'top|fail': 3, 'bottom|pass': 3, 'bottom|fail': 0}
lesson: the benchmark ranking inverts on replay; the families split, not the scores.
```

This also writes `results/transfer.json`.

## Step 3 — Break It (Exercise)

Swap the replay outcomes of g3 and g4. What happens to rho and to the cross-tab?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=82
python3 tools/figures/build.py 82
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
