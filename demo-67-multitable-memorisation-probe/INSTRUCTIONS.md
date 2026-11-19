# Demo 67: Multi-Table Memorisation Probe — Execution Instructions

> **Step-by-step guide for students.** For the concepts see [README.md](README.md).

---

## Overview

| What | Time | Command |
|------|------|---------|
| Environment check | 1 min | `python3 --version` |
| Run tests | 1 min | `python3 -m pytest tests/ -v` |
| Run the demo | 1 min | `python3 student/run_memprobe.py` (or `make demo DEMO=67` from root) |
| Record results | 5 min | Fill in the reproducibility table below |
| **Total** | **about 10 min** | |

**Safety**: fully offline, standard library only. Every fixture is synthetic JSON and is labelled as such.

## Step 0 — Environment check

```bash
python3 --version          # 3.11 or newer
```

## Step 1 — Run the tests

```bash
python3 -m pytest tests/ -v
```

**Expected**: all tests pass.

## Step 2 — Run the demonstration

```bash
python3 student/run_memprobe.py
```

This prints one line per case and writes `results/memprobe.json`.

## Step 3 — Break it (exercise)

Change one labelled entry in `fixtures/linked_tables.json` and re-run both commands. Record which printed line moved and why.

## Reproducibility table

| Field | Your run |
|-------|----------|
| Python version | |
| `pytest` result | ___ passed / ___ failed |
| Lines printed | ___ |
| Commit | Git SHA or `local` |
