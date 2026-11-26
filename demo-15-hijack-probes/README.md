# Demo 15: Hijack Probes

> **New here? Follow the step-by-step [Execution Instructions](INSTRUCTIONS.md)** — every command with expected output.

## Learning Objectives

- Explain what a white-box hijack probe is (flag an episode when its probe score meets a fixed threshold)
- Apply a fixed threshold (0.55) to 8 synthetic episodes and read the outcome table
- Show the probe catches 3/4 hijacked episodes with 0/4 false positives, missing borderline h4
- Distinguish this teaching toy from the research study it illustrates (in progress or under peer review; its data and results are not released here)

<!-- BEGIN generated: how-it-works (tools/figures/docs.py) -->
## How it works

<p align="center"><img src="figures/fig1_procedure.svg" width="100%" alt="Figure 1: the procedure of Demo 15 as numbered stages"></p>

**Figure 1.** A linear read-out of hidden states can flag a hijack at the layer where the model's plan changes. Numbered boxes are stages (role on top, rule or variable beneath, in monospace); dashed grey panels mark a trust domain or scope; a dashed red arrow marks where an adversary acts. Teaching schematic: it simplifies the research procedure and leaves out its corpora, models and thresholds.

### Step by step

1. **Open-weight agent** (`hidden states hₗ`). Read at each layer. In this demo: `fixtures/`.
2. **Linear probe** (`s = wᵀhₗ`). Trained on clean against hijacked episodes. In this demo: `student/probe.py`.
3. **Threshold** (`flag ⇔ s ≥ τ`). A fixed operating point. In this demo: `student/run_probe.py`.
4. **Evaluate** (`catches, false alarms`). Per episode. In this demo: `student/run_probe.py`.
5. **Where it changes its mind** (`layer of first separation`). Design stage. Run `make demo` to print it.

<p align="center"><img src="figures/fig2_worked_example.svg" width="100%" alt="Figure 2: worked example of Demo 15 on the synthetic fixture"></p>

**Figure 2.** The probe catches 3 of 4 hijacked episodes with 0 false alarms at this operating point. Values come from `make demo` on the synthetic fixture: they are illustrative and are not research results.

### What the research version adds (withheld while under peer review)

- Probes across layers of several open-weight tool-using models
- Held-out attack families
- Every number bound to committed analysis output (design stage)

The study's data, exact protocol, thresholds and results are not part of this teaching demo. They will be linked here once the paper is published open access.

<!-- END generated: how-it-works -->

## Conceptual Explanation

Deployed monitors score each episode for hijack signatures and flag the suspicious
ones. A fixed threshold trades catches against false alarms.

This toy uses 8 hand-built episodes (4 clean, 4 hijacked):

| Episode | Score | Truth | Flagged (>= 0.55) |
|---------|-------|-------|-------------------|
| c1 | 0.10 | clean | no |
| c2 | 0.20 | clean | no |
| c3 | 0.35 | clean | no |
| c4 | 0.50 | clean | no |
| h1 | 0.60 | hijacked | yes |
| h2 | 0.75 | hijacked | yes |
| h3 | 0.90 | hijacked | yes |
| h4 | 0.45 | hijacked | **no (missed)** |

Episode `h4` is the lesson: a borderline hijacked episode below threshold slips
through the same probe that catches the obvious cases.

## Safety Notice

WARNING: **This is a teaching demonstration using synthetic fixtures only.**
- No real trajectories, probes, models, or credentials
- No network access (standard library only)
- All episodes, scores and verdicts are hand-built toys
- Results demonstrate a mechanism; they are not evidence about real probes

## Reproducibility Metadata

| Field | Value |
|-------|-------|
| Seed | 15 (fixed; no randomness used) |
| Python | 3.11+ (stdlib only) |
| OS | Linux/macOS/Windows |
| Command | `python3 student/run_probe.py` |

## Research Connection

This demo illustrates the design question of a preregistered study on hijack
representation probing. That study has **collected no
confirmatory data**; every quantity there is `[RESULT PENDING]`. Nothing here describes
a publication, a venue result, or a measured effect size.

Provenance: distilled from `demo-15-hijack-representations-iclr` (private research repo).
It is a sibling of Demo 14 (conformal gating): this demo is white-box probe
signatures over representation scores; Demo 14 is black-box statistical gating
over action scores. Different signals, data, and claims.

### Difference from the Research Study

| Aspect | Research study | This demo |
|--------|----------------|-----------|
| Data | Preregistered probe-score corpus (pending) | 8 hand-built episodes |
| Method | Calibrated white-box probe signatures | Single fixed threshold 0.55 |
| Claims | Falsifiable detection hypotheses with registered margins | **No claims** — mechanism illustration only |
| Artefact | Probe calibration suite | One tiny probe class |
