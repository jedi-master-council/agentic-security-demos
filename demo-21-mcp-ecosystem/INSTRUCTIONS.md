# Demo 21: MCP Ecosystem Census — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_census.py` (or `make demo DEMO=21` from root) |
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

**Expected**: `5 passed` (determinism, poisoning 4/12 concentrated low,
drift 3/11, bundling 4/4 + concentration, results parity).

## Step 2 — Run the Census

```bash
python3 student/run_census.py
```

**Expected**:

```text
servers 12  poisoned 4 (high 1/4, low 3/8)
version pairs 11  drifted 3: srv-02, srv-06, srv-09
shell 4  shell+network 4  top4 maintainers 2 (alice, bob)
lesson: poisoning is non-trivial and concentrated low; drift is measurable; shell bundles with network.
```

This also writes `results/census.json`.

## Step 3 — Break It (Exercise)

Add a thirteenth server to `fixtures/servers.json` with a novel paraphrase of an
instruction (e.g. “kindly disregard earlier directives”). Re-run both commands and
record: does the literal-pattern detector catch it? What does that teach about
pattern vs model-based auditing?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=21
python3 tools/figures/build.py 21
```

## Step G — Run the Current Procedure (Simplified)

The research procedure for this topic has changed since the first version of this demo. This step teaches the current version.

```bash
python3 student/registry_hosting.py
python3 -m pytest tests/test_current_procedure.py -v
```

**Expected output**:

```text
latest-version endpoints 5 on 5 hosts; largest host share 0.20; under platform suffixes 0.60
version transitions 7; within 24 hours of the previous version 4
  endpoint change on s1: patch bump; host changed True; across registrable domains True
  endpoint change on s4: patch bump; host changed True; across registrable domains False
remote servers requiring a secret header 3/5
lesson: the tool layer is hosted on few platforms and changes fast; an endpoint can move under a patch bump.
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| Poisoned / Drifted | ___/12 / ___/11 |
| Shell+network | ___/___ |
| Commit | Git SHA or `local` |
