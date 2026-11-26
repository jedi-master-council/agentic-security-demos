# Demo 80: SoK Extraction Protocol — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/extract.py` (or `make demo DEMO=80` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-80-sok-extraction
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `6 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/extract.py
```

**Expected output**:

```text
papers 12  fields 3  kappa floor 0.6
field               agree  kappa  floor  disagreements
layer                0.92   0.89  pass   p03
formal_guarantee     0.92   0.82  pass   p09
adaptive_attack      0.75   0.47  FAIL   p02,p07,p12
map (layer | adaptive attack tested):
  architecture|no              1
  architecture|yes             1
  input-filter|no              2
  policy|no                    2
  policy|yes                   1
  training|yes                 1
sent to adjudication: p02,p03,p07,p12
lesson: high percent agreement can hide a kappa below the floor when one category dominates.
```

This also writes `results/extraction.json`.

## Step 3 — Break It (Exercise)

Resolve the disagreement on `p02` in favour of coder A. Does the adaptive-attack field now meet the 0.6 floor?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=80
python3 tools/figures/build.py 80
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
