# Demo 78: Sequential Covering Decision Lists for Lexical URL Features

> **▶️ New here? Follow the step-by-step [Execution Instructions](INSTRUCTIONS.md)** — every command with expected output.

## Learning Objectives

- Explain the measurement question of this teaching demonstration
- Run the offline procedure on the labelled synthetic fixture
- Distinguish the teaching output from a confirmatory research result
- Name the target venue and why the topic is scoped to that venue

<!-- BEGIN generated: how-it-works (tools/figures/docs.py) -->
## How it works

<p align="center"><img src="figures/fig1_procedure.svg" width="100%" alt="Figure 1: the procedure of Demo 78 as numbered stages"></p>

**Figure 1.** Sequential covering learns one rule at a time and removes what it already explains. Numbered boxes are stages (role on top, rule or variable beneath, in monospace); dashed grey panels mark a trust domain or scope; a dashed red arrow marks where an adversary acts. Teaching schematic: it simplifies the research procedure and leaves out its corpora, models and thresholds.

### Step by step

1. **URLs** (`lexical features`). Labelled. In this demo: `fixtures/`.
2. **Best rule** (`single feature`). Maximum precision. In this demo: `student/covering.py`.
3. **Remove covered** (`examples it explains`). Then repeat. In this demo: `student/covering.py`.
4. **Decision list** (`ordered rules`). First match decides. In this demo: `student/run_covering.py`.
5. **Classifier** (`ordered rule list`). Interpretable. Run `make demo` to print it.

<p align="center"><img src="figures/fig2_worked_example.svg" width="100%" alt="Figure 2: worked example of Demo 78 on the synthetic fixture"></p>

**Figure 2.** Two single-feature rules and a default classify all 8 URLs (accuracy 1.00). Values come from `make demo` on the synthetic fixture: they are illustrative and are not research results.

### What the research version adds (withheld while under peer review)

- Real URL datasets
- Comparison with other interpretable learners

The study's data, exact protocol, thresholds and results are not part of this teaching demo. They will be linked here once the paper is published open access.

<!-- END generated: how-it-works -->

## Conceptual Explanation

Greedy sequential covering that learns an ordered list of single-feature rules. The fixture holds 8 labelled synthetic cases.
Running `student/run_covering.py` prints one row per case and writes
`results/covering.json`. Every number produced here belongs to the
toy fixture; it is not evidence about a live system or an external corpus.

Target venue (option A): **AAAI**. Options B and C are
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
| Seed | 78 (fixed; no randomness used) |
| Python | 3.11+ (stdlib only) |
| OS | Linux/macOS/Windows |
| Command | `make demo DEMO=78` |

## Research Connection

This demo illustrates the measurement question of a pending study aimed at
AAAI. That study has collected no confirmatory data; every
quantity there is `[RESULT PENDING]`. Nothing here describes a publication,
a venue result, or a measured effect size.
