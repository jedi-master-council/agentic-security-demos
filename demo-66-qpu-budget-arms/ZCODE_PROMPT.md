# Z code prompt: demo-66

Paste everything below the line into Z code (or another coding agent), opened in this folder on a machine that is not the author's own computer. Do the steps in order, check each one before moving on, and stop as soon as a stop rule applies.

---

You are working in the repository demo-66. Read `README.md` first.

## Hard rules
If any step would break one of these rules, write `results/BLOCKED.md` saying which rule and why, commit it, and stop.

1. Nothing costs money. Use only free allowances or open-weight models run on the machine. Never configure a paid endpoint.
2. Keys come only from environment variables. Never print, log or commit a key.
3. Public or synthetic data only, as stated in `README.md`.
4. Every reported number comes from a committed script in `analysis/` that reads the logs. Never type a number into a report by hand.
5. Tracked files carry no absolute paths, user names, machine names, host names or IP addresses. Never cite the repository owner's own work.
6. Commit after each step. Never force-push, rewrite history or delete logs.

## Step 0. Environment
1. `python3 -m venv .venv && source .venv/bin/activate && pip install qiskit qiskit-aer qiskit-ibm-runtime mitiq`. Record every package version in `results/ENVIRONMENT.md` and `pip freeze > results/pip_freeze.txt`.
2. Install Ollama and pull one open-weight model that fits the machine's memory. Record its tag, digest and quantisation. This is arm A2. No paid model is called, and arm A1 (frontier models) is not run.
3. `python3 -m pytest tests/ -q` must pass before anything else.

## Step 1. Register before the first real run
Write `docs/PREREGISTRATION_<date>.md` and commit it before step 2. It fixes: two workload families and six to ten instances small enough for an exact classical reference; the fake backend (one device-calibration snapshot from `qiskit_ibm_runtime.fake_provider`, named and versioned); the simulated QPU-time model (per-job overhead and per-shot time) and the budget; the acceptance tolerance per observable; arms B0, B1 and A2 with their exact rules and prompts; the primary outcome (accepted results per simulated QPU-second) and secondary outcomes; repeats and seeds.

## Step 2. Run
Run every arm on the same instances with the same seeds and budget. Log every simulated job (instance, arm, shots, noise scale, simulated seconds, estimate) and every model call (model, digest, tokens, time) to `results/`.

## Step 3. Report
A committed script in `analysis/` writes `results/PILOT_SUMMARY.json` and `results/PILOT_REPORT_<date>.md`: per arm, accepted results per simulated QPU-second with spread over repeats, N instances, and QPU-seconds lost. The report says on its first line that it is a simulation-only feasibility check and not hardware evidence.
