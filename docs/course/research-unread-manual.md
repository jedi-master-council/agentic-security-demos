# Research Module: The Unread Manual

**Duration**: 1 hour (seminar) or a project brief | **Format**: Demo walkthrough (15 min) + discussion (20 min) + project brief (25 min)
**Prerequisites**: Module 11 (Degenerate Reporting) and Module 1 (Blind Verification)
**Demo directory**: `demo-90-unread-manual/`

> Optional research-format module. It applies the course's evidence discipline to a question every repository owner now faces: does writing guidance for coding agents change what agents do?

---

## 🎯 Learning Goals

By the end of this module you can:
1. Define **exposure** and **acquisition** operationally from an agent action log
2. Show why a file appearing in a directory listing is not evidence that it was read
3. Compute the naive readers-versus-non-readers comparison and explain its confounding
4. Compare outcomes within the same task and say what the difference does and does not identify
5. State the falsification condition for "reading guidance improves repair"

## 🧪 Demo Script (15 min, facilitator runs)

Follow [`demo-90-unread-manual/INSTRUCTIONS.md`](https://github.com/jedi-master-council/agentic-security-demos/blob/main/demo-90-unread-manual/INSTRUCTIONS.md) Steps 0–3 live.

1. **Before running**, ask the room: in a run where the README appears in `ls` output, did the agent read it? Most cohorts say yes. The demo's exposure and acquisition columns separate the two.
2. **After the naive comparison**, ask why readers appear to resolve *less* often. The answer is task difficulty: harder tasks prompt more reading, so the marginal association is negative even when reading helps.
3. **After the within-task table**, ask what the flat difference does *not* prove. (It does not identify a causal effect: reading is chosen by the agent, and unobserved task features remain.)

## 📝 Exercises (25 min, pairs or project brief)

- **Exercise R1.1** — Make run `r06` open `README.md` before editing and resolve the task. Record the naive and within-task differences before and after.
- **Exercise R1.2** — Add a second confounder: make the hardest task the only one whose agents read `AGENTS.md`. Predict the naive comparison, then run it.
- **Exercise R1.3** — Write the falsification condition for the claim "acquisition predicts resolution within task" and name the smallest fixture change that would falsify it.

## 🔗 Links to Earlier Modules

| This module revisits | Connection |
|---|---|
| Module 1 (Blind Verification) | Commit the prediction before running the fixture, then compare |
| Module 11 (Degenerate Reporting) | Baseline, base rate and metric sanity before trusting a headline association |
| Final Assessment | Use the exposure/acquisition distinction in the portfolio reflection |

## ✅ Completion Criteria

- `results/context_acquisition.json` regenerated and checked against the terminal output
- Prediction recorded before Exercise R1.1 is run
- A written falsification condition for the within-task claim
- One paragraph on why the naive comparison is not a treatment effect

---

*Research-format module. The teaching demo is synthetic; the study's data, protocol and results are withheld while under review.*
