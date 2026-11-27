# Demo 90: The Unread Manual — Exposure and Acquisition of Repository Guidance

> **▶️ New here? Follow the step-by-step [Execution Instructions](https://github.com/jedi-master-council/agentic-security-demos/blob/main/demo-90-unread-manual/INSTRUCTIONS.md)** — every command with expected output.

## Learning Objectives

- Separate **exposure** (a guidance file appeared in the agent's observations) from **acquisition** (the agent opened it)
- Measure *when* guidance is read relative to the first edit in a trajectory
- Compare outcomes **within the same task** before reading anything into an association
- Explain why a naive readers-versus-non-readers comparison can point the wrong way

## Conceptual Explanation

Repository owners write guidance for coding agents — README, CONTRIBUTING, `AGENTS.md`, `docs/` — on the assumption that it will be read. An agent's own action log records what it actually consulted. A directory listing puts the README in front of every run, so counting *mentions* says every agent saw it; counting *reads* gives a very different answer. Whether reading predicts success then has to be checked within the same task, because harder tasks prompt more reading.

The fixture holds 12 synthetic runs. `student/acquisition.py` prints the per-class exposure and acquisition rates, the number of runs that edited before reading any prose guidance, the naive comparison, and the within-task comparison. Every number belongs to the toy fixture.

Target venue (option A): **Empirical Software Engineering (EMSE)**, rolling submission. Options B and C are the sequential fallbacks recorded in `venue.yaml`.

## Safety Notice

⚠️ **This is a teaching demonstration using synthetic fixtures only.**
- Every trajectory, file name, task and verdict is invented
- No network access (standard library only)
- No credentials, real repositories or collected personal data
- Results demonstrate a mechanism; they are not evidence about real systems

## Reproducibility Metadata

| Field | Value |
|-------|-------|
| Randomness | none (deterministic) |
| Python | 3.10+ (standard library only) |
| OS | Linux/macOS/Windows |
| Command | `make demo DEMO=90` |
| Output | `demo-90-unread-manual/results/context_acquisition.json` |

## Exercise

Make run `r06` open `README.md` before editing and resolve the task. What happens to the naive comparison and to the within-task comparison?

## Research Connection

This demo distils, in simplified form, the procedure of a study in the author's research programme that is in progress. The full study measures exposure and acquisition across public trajectory corpora, holds the task fixed with task effects and trajectory-length controls, and compares guidance policies on the same tasks. Its data, exact protocol, thresholds and results are withheld while the paper is under review and will be linked here once it is published open access. Nothing on this page describes a publication, a venue result or a measured effect size.

---

Source: [`demo-90-unread-manual`](https://github.com/jedi-master-council/agentic-security-demos/blob/main/demo-90-unread-manual) in the repository.
