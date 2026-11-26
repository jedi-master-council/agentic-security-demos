# Demo 81: The Frozen Gate Benchmark — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/harness.py` (or `make demo DEMO=81` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-81-frozen-gate
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `6 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/harness.py
```

**Expected output**:

```text
pin check: corpus SHA-256 matches the manifest
traj  override sink  flag
t1    True     True  FLAG
t2    False    False -
t3    True     True  FLAG
t4    False    False -
t5    True     False -
t6    False    False -
t7    True     True  FLAG
t8    True     True  FLAG
run 1 table 69dac3a83281db5a  run 2 table 69dac3a83281db5a  byte-identical True
tp 3 fp 1 fn 1 tn 3
lesson: a frozen gate is reproducible byte for byte; reproducible is not the same as correct.
```

This also writes `results/frozen_gate.json`.

## Step 3 — Break It (Exercise)

Edit one call in the corpus and run the harness. What happens? Then add a phrase to the override lexicon so that `t5` is caught, and update the manifest hash.

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=81
python3 tools/figures/build.py 81
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
