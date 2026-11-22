# Demo 82: Guardrail Score Transfer

> **▶️ New here? Follow the step-by-step [Execution Instructions](INSTRUCTIONS.md)** — every command with expected output.

## Learning Objectives

- Compute a rank correlation between benchmark scores and observed attack outcomes
- Trace the mechanism in the synthetic fixtures
- Name what the mechanism measures versus what a policy would decide

## Conceptual Explanation

4 synthetic models with benchmark scores and replay outcomes; the student computes Spearman's rank correlation by hand from the table

## Safety Notice

⚠️ **This is a teaching demonstration using synthetic fixtures only.**
- No real traces, systems, or credentials
- No network access (standard library only)
- All fixtures are hand-built toys
- Results demonstrate a mechanism; they are not evidence about real agents

## Reproducibility Metadata

| Field | Value |
|-------|-------|
| Seed | 82 (fixed; no randomness used) |
| Python | 3.11+ (stdlib only) |
| OS | Linux/macOS/Windows |
| Command | `make test` |

## Research Connection

This demo illustrates the design question of a measurement study on "Guardrail Score Transfer: What Benchmark Scores Predict About Tool-Use Attacks".
That measurement is **pending**; the research repository is private and carries no
measured results yet. Nothing here describes a publication, a venue result, or a
measured effect size.

Provenance: distilled from the topic portfolio
(`TOPIC_PORTFOLIO_R2_2026-11-22.md`, topic 82) in the private research repos.
