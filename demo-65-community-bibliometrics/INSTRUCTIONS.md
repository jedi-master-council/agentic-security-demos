# Demo 65: Security–Education Bibliometrics — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/bibliometrics.py` (or `make demo DEMO=65` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-65-community-bibliometrics
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `3 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/bibliometrics.py
```

**Expected output**:

```text
set S (agent security) 5 works; set E (AI in education) 5 works
second-model check on 8 sampled works: agreement 7/8
authors in both communities: Cedar
lesson: a bridge author is a measurable link; a screen is only as good as its second check.
```

This also writes `results/bibliometrics.json`.

## Step 3 — Break It (Exercise)

Relabel `w06` as the second model did. Does the shared-author count change? What would a single bridging author mean for a claim that the communities are separate?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=65
python3 tools/figures/build.py 65
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
