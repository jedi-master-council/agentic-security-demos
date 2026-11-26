# Demo 63: Policy-Coding Reliability — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/reliability.py` (or `make demo DEMO=63` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-63-coding-reliability
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `5 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/reliability.py
```

**Expected output**:

```text
permits_use          alpha = +1.00  acceptable (>= 0.667)
requires_disclosure  alpha = +0.76  acceptable (>= 0.667)
assessment_rules     alpha = +0.06  unreliable
staff_guidance       alpha = +1.00  acceptable (>= 0.667)
model A changed its codes on unchanged text: u3
lesson: report reliability per dimension; and re-code unchanged text to see whether a model is stable.
```

This also writes `results/reliability.json`.

## Step 3 — Break It (Exercise)

Make model B agree with model A on `assessment_rules` for u2 and u3. How far does alpha rise? Why does a dimension where almost every code is 1 give a fragile alpha?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=63
python3 tools/figures/build.py 63
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
