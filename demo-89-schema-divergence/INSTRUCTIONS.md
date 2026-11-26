# Demo 89: Tool-Schema Interpretation Divergence — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/divergence.py` (or `make demo DEMO=89` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-89-schema-divergence
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `4 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/divergence.py
```

**Expected output**:

```text
payload  dimension            fw-a (lenient)   fw-b (strict)  divergent
p1       control              accept           accept         -
p2       type coercion        accept-coerced   reject         YES
p3       bounds               accept           reject         YES
p4       enum case            accept-coerced   reject         YES
p5       undeclared keyword   accept-coerced   reject         YES
p6       nullability          accept-coerced   reject         YES
p7       control              accept           accept         -
p8       type coercion        accept-coerced   reject         YES
divergent payloads 6/8
lesson: the same schema is a different gate in each framework; test the gate, not the schema.
```

This also writes `results/divergence.json`.

## Step 3 — Break It (Exercise)

Make the lenient validator reject undeclared keywords. Which divergences remain?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=89
python3 tools/figures/build.py 89
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
