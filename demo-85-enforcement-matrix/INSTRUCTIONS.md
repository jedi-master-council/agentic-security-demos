# Demo 85: The Enforcement Matrix — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/matrix.py` (or `make demo DEMO=85` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-85-enforcement-matrix
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `5 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/matrix.py
```

**Expected output**:

```text
mode = native
                    shell          network       file_write
  fw-a    documented-only           absent           absent
  fw-b    documented-only  documented-only           absent
  fw-c             absent           absent           absent
mode = monitor
                    shell          network       file_write
  fw-a           enforced         enforced         enforced
  fw-b           enforced         enforced  documented-only
  fw-c           enforced         enforced         enforced
label survival at the sink: {'verbatim': '2/2', 'paraphrase': '0/2', 'split': '0/2'}
lesson: a label that is documented is not a label that is enforced, and a token label rarely survives the model.
```

This also writes `results/matrix.json`.

## Step 3 — Break It (Exercise)

Design a label that would survive the 'split' transform. What would it cost in false positives?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=85
python3 tools/figures/build.py 85
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
