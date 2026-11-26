# Demo 83: Manifest Census at Registry Scale — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/census.py` (or `make demo DEMO=83` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-83-manifest-census
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `4 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/census.py
```

**Expected output**:

```text
snapshot t1: {'servers': 8, 'description_flagged': 2, 'remote_without_auth': 3, 'name_confusable': 0}
  s01 calendar-tools  markers=-                            auth_gap=no  confusable=-
  s02 contact-sync    markers=exfiltration-endpoint,instruction-override auth_gap=yes confusable=-
  s03 weather         markers=-                            auth_gap=yes confusable=-
  s04 notes           markers=-                            auth_gap=no  confusable=-
  s05 git-helper      markers=-                            auth_gap=no  confusable=-
  s06 gihub-helper    markers=privilege-claim              auth_gap=yes confusable=-
  s07 translate       markers=-                            auth_gap=no  confusable=-
  s08 files           markers=-                            auth_gap=no  confusable=-
snapshot t2: {'servers': 10, 'description_flagged': 3, 'remote_without_auth': 4, 'name_confusable': 2}
  s01 calendar-tools  markers=-                            auth_gap=no  confusable=calendar-tool
  s02 contact-sync    markers=exfiltration-endpoint,instruction-override auth_gap=yes confusable=-
  s03 weather         markers=-                            auth_gap=yes confusable=-
  s04 notes           markers=-                            auth_gap=no  confusable=-
  s05 git-helper      markers=-                            auth_gap=no  confusable=-
  s06 gihub-helper    markers=privilege-claim              auth_gap=yes confusable=-
  s07 translate       markers=-                            auth_gap=no  confusable=-
  s08 files           markers=-                            auth_gap=no  confusable=-
  s09 calendar-tool   markers=exfiltration-endpoint        auth_gap=yes confusable=calendar-tools
  s10 pdf-reader      markers=-                            auth_gap=no  confusable=-
lesson: the description is the only text a client sees before install; scan it, and read auth metadata as a signal, not a guarantee.
```

This also writes `results/census.json`.

## Step 3 — Break It (Exercise)

Add a server named `pdf-reader2` at t2. Is it confusable? Should edit distance alone decide?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=83
python3 tools/figures/build.py 83
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
