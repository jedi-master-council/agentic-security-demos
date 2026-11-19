# Z code prompt: demo-67

Paste everything below the line into Z code (or another coding agent), opened in this folder on a machine that is not the author's own computer. Do the steps in order, check each one before moving on, and stop as soon as a stop rule applies.

---

You are working in the repository demo-67. Read `README.md` first.

## Hard rules
If any step would break one of these rules, write `results/BLOCKED.md` saying which rule and why, commit it, and stop.

1. Nothing costs money. Use only free allowances or open-weight models run on the machine. Never configure a paid endpoint.
2. Keys come only from environment variables. Never print, log or commit a key.
3. Public or synthetic data only, as stated in `README.md`.
4. Every reported number comes from a committed script in `analysis/` that reads the logs. Never type a number into a report by hand.
5. Tracked files carry no absolute paths, user names, machine names, host names or IP addresses. Never cite the repository owner's own work.
6. Commit after each step. Never force-push, rewrite history or delete logs.

## Step 0. Environment
1. `python3 -m venv .venv && source .venv/bin/activate`. Record versions in `results/ENVIRONMENT.md`.
2. Download OULAD from its official source (Kuzilek, Hlosta and Zdrahal, 2017, doi:10.1038/sdata.2017.171; CC BY 4.0) and record the archive's SHA-256. Keep only the 2013 presentations for this pilot; never load a 2014 presentation into any prompt.
3. Install Ollama and pull one or two open-weight models. Record tags and digests. Free or local models only.
4. `python3 -m pytest tests/ -q` must pass.

## Step 1. Register before the first real run
Write `docs/PREREGISTRATION_<date>.md` and commit it first. It fixes: the tests (header, row completion, feature completion, cross-table completion) and their prompts; the number of remapped copies (at least 40) and the remapping rule; the false-positive rate (5 per cent); the in-context positive control and its exposure counts; the models; the primary outcome (detection of the positive control at the registered false-positive rate).

## Step 2. Run
Score every model on the published 2013 tables and on every remapped copy. Log every call.

## Step 3. Report
A committed script in `analysis/` writes `results/PILOT_SUMMARY.json` and `results/PILOT_REPORT.md`. The report states that the positive control is in-context exposure, a weaker stand-in for fine-tuning, and that the pilot is not a validation of the probe.
