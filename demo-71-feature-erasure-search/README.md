# Demo 71: Minimum-Cost Feature Erasure Search for Linear Classifiers

> **▶️ New here? Follow the step-by-step [Execution Instructions](INSTRUCTIONS.md)** — every command with expected output.

## Learning Objectives

- Explain the measurement question of this teaching demonstration
- Run the offline procedure on the labelled synthetic fixture
- Distinguish the teaching output from a confirmatory research result
- Name the target venue and why the topic is scoped to that venue

<!-- BEGIN generated: how-it-works (tools/figures/docs.py) -->
## How it works

<p align="center"><img src="figures/fig1_procedure.svg" width="100%" alt="Figure 1: the procedure of Demo 71 as numbered stages"></p>

**Figure 1.** The cheapest set of feature erasures that flips a linear score is found by search. Numbered boxes are stages (role on top, rule or variable beneath, in monospace); dashed grey panels mark a trust domain or scope; a dashed red arrow marks where an adversary acts. Teaching schematic: it simplifies the research procedure and leaves out its corpora, models and thresholds.

### Step by step

1. **Instance** (`x, weights w`). A linear score. In this demo: `fixtures/`.
2. **Candidates** (`feature subsets`). Ordered by erasure cost. In this demo: `student/erasure.py`.
3. **Search** (`cheapest flip`). Complete heuristic search. In this demo: `student/erasure.py`.
4. **Certificate** (`score(x ∖ S) < 0`). The erasure that flips it. In this demo: `student/run_erasure.py`.
5. **Minimum erasure** (`cost(S*)`). Per instance. Run `make demo` to print it.

<p align="center"><img src="figures/fig2_worked_example.svg" width="100%" alt="Figure 2: worked example of Demo 71 on the synthetic fixture"></p>

**Figure 2.** Greedy search matches the exhaustive minimum on these instances; the exhaustive answer is the certificate. Values come from `make demo` on the synthetic fixture: they are illustrative and are not research results.

### What the research version adds (withheld while under peer review)

- Larger feature spaces
- Complexity results

The study's data, exact protocol, thresholds and results are not part of this teaching demo. They will be linked here once the paper is published open access.

<!-- END generated: how-it-works -->

## Conceptual Explanation

Complete heuristic search for the cheapest feature erasures that flip a linear score. The fixture holds 8 labelled synthetic cases.
Running `student/run_erasure.py` prints one row per case and writes
`results/erasure.json`. Every number produced here belongs to the
toy fixture; it is not evidence about a live system or an external corpus.

Target venue (option A): **IEEE TAI**. Options B and C are
sequential fallbacks and are recorded in `venue.yaml`.

## Safety Notice

⚠️ **This is a teaching demonstration using synthetic fixtures only.**
- No real vulnerabilities, credentials, or production systems
- No network access (standard library only)
- All cases and verdicts are hand-built toys
- Results demonstrate a mechanism; they are not evidence about real deployments

## Reproducibility Metadata

| Field | Value |
|-------|-------|
| Seed | 71 (fixed; no randomness used) |
| Python | 3.11+ (stdlib only) |
| OS | Linux/macOS/Windows |
| Command | `make demo DEMO=71` |

## Research Connection

This demo illustrates the measurement question of a pending study aimed at
IEEE TAI. That study has collected no confirmatory data; every
quantity there is `[RESULT PENDING]`. Nothing here describes a publication,
a venue result, or a measured effect size.
