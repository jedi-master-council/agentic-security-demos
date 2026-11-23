# Demo 88: The Detection Confusion Matrix

> **▶️ New here? Follow the step-by-step [Execution Instructions](INSTRUCTIONS.md)** — every command with expected output.

## Learning Objectives

- Compute a confusion matrix and per-class rates from a detection run
- Trace the mechanism in the synthetic fixtures
- Name what the mechanism measures versus what a policy would decide

## Conceptual Explanation

8 synthetic trajectories (3 injected); two baseline detectors' verdicts; the student fills the confusion matrix

## Safety Notice

⚠️ **This is a teaching demonstration using synthetic fixtures only.**
- No real traces, systems, or credentials
- No network access (standard library only)
- All fixtures are hand-built toys
- Results demonstrate a mechanism; they are not evidence about real agents

## Reproducibility Metadata

| Field | Value |
|-------|-------|
| Seed | 88 (fixed; no randomness used) |
| Python | 3.11+ (stdlib only) |
| OS | Linux/macOS/Windows |
| Command | `make test` |

## Research Connection

This demo illustrates the design question of a measurement study on "A Detection Benchmark for Injected Actions in Agent Trajectories".
That measurement is **pending**; the research repository is private and carries no
measured results yet. Nothing here describes a publication, a venue result, or a
measured effect size.

Provenance: distilled from the topic portfolio
(`TOPIC_PORTFOLIO_R2_2026-11-22.md`, topic 88) in the private research repos.
