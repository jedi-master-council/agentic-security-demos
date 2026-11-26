# Demo 62: LLM Learner Policy Checks — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/policy_checks.py` (or `make demo DEMO=62` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-62-learner-policy-checks
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `3 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/policy_checks.py
```

**Expected output**:

```text
schema adherence 0.80  invalid outputs: l04, l07
Brier score: LLM policy 0.184  base-rate baseline 0.260  (lower is better)
persona-sensitive learners (|change| >= 0.20 under an equivalent rewording): l03, l08
lesson: check the format, then compare with a baseline that costs nothing, then perturb the wording.
```

This also writes `results/policy_checks.json`.

## Step 3 — Break It (Exercise)

Set `l08`'s reworded prediction to 0.85. How many learners remain persona-sensitive? What Brier score would a policy that always predicts 0.4 obtain?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=62
python3 tools/figures/build.py 62
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
