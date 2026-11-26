# Demo 87: Declared versus Actual Capability — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/diff.py` (or `make demo DEMO=87` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-87-capability-diff
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `4 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/diff.py
```

**Expected output**:

```text
s1: declared=['read_file'] extracted=['read_file']
     hidden (extracted, not declared) = -   unused (declared, not found) = -
s2: declared=['read_file'] extracted=['read_file', 'run_shell']
     hidden (extracted, not declared) = ['run_shell']   unused (declared, not found) = -
s3: declared=['read_file', 'web_search'] extracted=['web_search']
     hidden (extracted, not declared) = -   unused (declared, not found) = ['read_file']
s4: declared=[] extracted=['network_post']
     hidden (extracted, not declared) = ['network_post']   unused (declared, not found) = -
s5: declared=['run_shell'] extracted=['run_shell']
     hidden (extracted, not declared) = -   unused (declared, not found) = -
s6: declared=['network_post', 'read_file', 'write_file'] extracted=['read_file', 'write_file']
     hidden (extracted, not declared) = -   unused (declared, not found) = ['network_post']
skills with hidden capability 2/6; with unused declaration 2/6
lesson: both directions matter; a hidden capability is a risk, an unused declaration erodes the manifest's meaning.
```

This also writes `results/capability_diff.json`.

## Step 3 — Break It (Exercise)

Add a skill whose handler calls `os.system`. Which pattern catches it, and which direction does it fall in?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=87
python3 tools/figures/build.py 87
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
