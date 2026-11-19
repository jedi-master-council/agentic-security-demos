# Z code prompt: demo-69

Paste everything below the line into Z code (or another coding agent), opened in this folder on a machine that is not the author's own computer. Do the steps in order, check each one before moving on, and stop as soon as a stop rule applies.

---

You are working in the repository demo-69. Read `README.md` first.

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
2. Install Ollama and pull one open-weight model; record its tag and digest. Free or local models only.
3. `python3 -m pytest tests/ -q` must pass.

## Step 1. Collect and register
List the public terms pages to be read (AI services offered to education), capture each with a dated Internet Archive snapshot, and store the snapshot URL and SHA-256 of the captured text in `data/sources.csv`. For a random sample, the author writes gold values for the five fields before any model output is seen. Write `docs/PREREGISTRATION_<date>.md` fixing the extraction prompt, the normalisation and consistency rules and the outcomes, and commit it before step 2.

## Step 2. Run
Run the model extraction and the keyword baseline on every page. Log every call.

## Step 3. Report
A committed script in `analysis/` writes `results/PILOT_SUMMARY.json` and `results/PILOT_REPORT.md`: grounded-and-consistent share, fabricated-quote rate and accuracy on the gold sample, with intervals. The report makes no descriptive claim about any vendor's terms.
