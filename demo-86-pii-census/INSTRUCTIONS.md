# Demo 86: Personal-Data Exposure Census — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/pii.py` (or `make demo DEMO=86` from the repository root) |
| Exercise | 10 min | see Step 3 |
| **Total** | **~15 min** | |

**Safety**: 100% offline, standard library only. All fixtures are synthetic.

---

## Step 0 — Environment Check

```bash
cd demo-86-pii-census
python3 --version          # 3.10 or newer
```

## Step 1 — Run the Tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: `4 passed`.

## Step 2 — Run the Demonstration

```bash
python3 student/pii.py
```

**Expected output**:

```text
c01 email    email
c02 shell    path_username
c03 shell    ip_address   <- differs from truth
c04 http     api_key
c05 http     ip_address
c06 message  phone
c07 file     path_username
c08 file     -
c09 message  -
c10 shell    api_key
c11 email    email
c12 http     -
per family (tp/fp): {'email': '2/0', 'phone': '1/0', 'ip_address': '1/1', 'api_key': '2/0', 'path_username': '2/0'}
per tool class: {'email': {'email': 2}, 'shell': {'path_username': 1, 'ip_address': 1, 'api_key': 1}, 'http': {'api_key': 1, 'ip_address': 1}, 'message': {'phone': 1}, 'file': {'path_username': 1}}
lesson: a closed shape lexicon is auditable and reproducible; it still mistakes a version string for an address.
```

This also writes `results/pii_census.json`.

## Step 3 — Break It (Exercise)

Tighten the IP pattern so that `pkg==1.2.3.4` no longer matches. Does anything else change?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=86
python3 tools/figures/build.py 86
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your value |
|-------|------------|
| Python version | |
| Tests passed | |
| Output identical to Step 2? | |
