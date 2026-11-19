# Z code prompt: demo-68

Paste everything below the line into Z code (or another coding agent), opened in this folder on a machine that is not the author's own computer. Do the steps in order, check each one before moving on, and stop as soon as a stop rule applies.

---

You are working in the repository demo-68. Read `README.md` first.

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
2. Optional second filter: install Ollama and pull one small open-weight model; record its tag and digest.
3. `python3 -m pytest tests/ -q` must pass.

## Step 1. Write the scripted messages and register
Write at least 200 scripted messages in the style of questions typed during statistics problems, each hand-labelled for identifier spans by type and form (ordinary, obfuscated, case-varied, split across tokens), plus a synthetic roster with quasi-identifiers. No real person's details. Then write `docs/PREREGISTRATION_<date>.md` fixing the filter rules, the optional model prompt, the span-overlap rule and the outcomes, and commit it before step 2.

## Step 2. Run
Run the rule filter and, if used, the rule filter followed by the local model. Log every call.

## Step 3. Report
A committed script in `analysis/` writes `results/PILOT_SUMMARY.json` and `results/PILOT_REPORT.md`: recall and precision by type with Wilson intervals, the residue table, and the share of messages singled out (k = 1). The report states that no participant data were used.
