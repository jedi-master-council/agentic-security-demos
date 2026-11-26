# Demo 43: Terms Coding — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## ⏱️ Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_terms.py` (or `make demo DEMO=43` from root) |
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

**Expected**: `5 passed` (determinism, disclaim 5/8, monitoring 4/8 with
consent 3/8, results parity, stdlib-only).

## Step 2 — Run the Terms Coding

```bash
python3 student/run_terms.py
```

**Expected**:

```text
platforms 8
clause                   count
disclaims_autonomy       5/8
requires_monitoring      4/8
consent_for_delegation   3/8
```

This also writes `results/terms.json`.

## Step 3 — Break It (Exercise)

Flip `plat6`'s `consent_for_delegation` to `true` in
`fixtures/platforms.json` and re-run both commands. Record: which tally
moves, and which tests fail? What would a fourth clause (e.g. incident
disclosure) add to the accountability gradient?

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=43
python3 tools/figures/build.py 43
```

## Step G — Run the Current Procedure (Simplified)

The research procedure for this topic has changed since the first version of this demo. This step teaches the current version.

```bash
python3 student/confirmation_gap.py
python3 -m pytest tests/test_current_procedure.py -v
```

**Expected output**:

```text
send_payment     state-altering  confirmation parameter: yes
refund           state-altering  confirmation parameter: NO
send_message     state-altering  confirmation parameter: NO
post_tweet       state-altering  confirmation parameter: NO
write_file       state-altering  confirmation parameter: NO
delete_file      state-altering  confirmation parameter: yes
change_password  state-altering  confirmation parameter: NO
close_account    state-altering  confirmation parameter: yes
search           read-only       confirmation parameter: -
get_weather      read-only       confirmation parameter: -
list_files       read-only       confirmation parameter: -
read_calendar    read-only       confirmation parameter: -
state-altering tools 8/12; with a confirmation keyword 3/8; gap 5
lesson: terms may expect a human to confirm; the schema is where that confirmation would have to live (and a keyword rule misses 'require_approval').
```

<!-- END generated: figures-step -->

## Reproducibility Table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | 5 passed / ___ failed |
| Disclaim / Monitoring / Consent | ___ / ___ / ___ |
| Commit | Git SHA or `local` |
