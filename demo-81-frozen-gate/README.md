# Demo 81: The Frozen Gate Benchmark

> **▶️ New here? Follow the step-by-step [Execution Instructions](INSTRUCTIONS.md)** — every command with expected output.

## Learning Objectives

- Explain why a benchmark harness must be deterministic (the same inputs, the same verdicts, twice)
- Trace the mechanism in the synthetic fixtures
- Name what the mechanism measures versus what a policy would decide

## Conceptual Explanation

6 synthetic trajectories through a frozen classifier, run twice; the two result tables compared byte-for-byte

## Safety Notice

⚠️ **This is a teaching demonstration using synthetic fixtures only.**
- No real traces, systems, or credentials
- No network access (standard library only)
- All fixtures are hand-built toys
- Results demonstrate a mechanism; they are not evidence about real agents

## Reproducibility Metadata

| Field | Value |
|-------|-------|
| Seed | 81 (fixed; no randomness used) |
| Python | 3.11+ (stdlib only) |
| OS | Linux/macOS/Windows |
| Command | `make test` |

## Research Connection

This demo illustrates the design question of a measurement study on "The Agent-Security Benchmark: Frozen Gates, Pinned Corpora, Registered Falsification".
That measurement is **pending**; the research repository is private and carries no
measured results yet. Nothing here describes a publication, a venue result, or a
measured effect size.

Provenance: distilled from the topic portfolio
(`TOPIC_PORTFOLIO_R2_2026-11-22.md`, topic 81) in the private research repos.
