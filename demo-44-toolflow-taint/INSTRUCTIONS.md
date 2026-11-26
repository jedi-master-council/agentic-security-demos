# Demo 44: Toolflow Taint — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_taint.py` (or `make demo DEMO=44` from root) |
| Record results | 5 min | Fill reproducibility table below |
| **Total** | **~10 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic JSON.

---

## Step 0 — Environment Check

```bash
python3 --version          # must be 3.11 or newer
```

**Expected**: `Python 3.11.x` (or higher).

## Step 1 — Run the Tests

From this directory:

```bash
python3 -m pytest tests/ -v
```

**Expected**: `5 passed` (determinism, 5/8 unlabelled-to-sensitive, flow ids
pinned, results parity, stdlib-only).

## Step 2 — Run the Taint Check

```bash
python3 student/run_taint.py
```

**Expected**:

```text
flows 8  sensitive sinks code/shell/file/network/memory
id     sink     provenance
flow1  shell    False
flow2  file     False
flow3  network  False
flow4  memory   False
flow5  code     False
flow6  shell    True
flow7  next-args False
flow8  next-args True
unlabelled to sensitive: 5/8 (flow1, flow2, flow3, flow4, flow5).
```

This also writes `results/taint.json`.

## Step 3 — Break It (Exercise)

Flip `flow3`'s `provenance` to `true` in `fixtures/edges.json` and re-run
both commands. Record: does the count drop to 4/8? Why does labelling one
edge change the measurement but not the enforcement question — and where
does enforcement live (see Demo 04 AuthorityBound)?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=44
python3 tools/figures/build.py 44
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| Unlabelled to sensitive | ___ |
| Tainted flow ids | ___ |
| Commit | Git SHA or `local` |
