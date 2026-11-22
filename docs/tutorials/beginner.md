# Beginner Exercises

A first pass through the collection for readers who have not run an agentic-security toy before. Allow two to three hours.

## Before you start

1. Complete [Lab 00 — Setup](../course/lab-00-setup.md).
2. Run `make test` once; the full suite is offline and deterministic.
3. Read [Safety First](../getting-started/safety.md).

## Core exercises

| Order | Demo | What to do | Lab |
|:---:|---|---|---|
| 1 | [Blind Verification](../demos/01-blind-verification.md) | Commit to an answer before the oracle reveals the key | [Lab 01](../course/lab-01-blind-verification.md) |
| 2 | [Supply Chain AIBOM](../demos/02-supply-chain-aibom.md) | Detect a component change that a policy gate should block | [Lab 02](../course/lab-02-supply-chain-aibom.md) |
| 3 | [ReconScope](../demos/06-reconscope.md) | Separate observed network data from instructions | [Lab 06](../course/lab-06-reconscope.md) |
| 4 | [TriageTrap](../demos/07-triagetrap.md) | Show how a base rate changes a triage verdict | [Lab 07](../course/lab-07-triagetrap.md) |

## Check your understanding

- Why is a post-hoc explanation weaker than a pre-committed answer?
- Which policy gate blocks the drift, and what happens when it is waived?
- Why is network output data rather than authority?
- How does a low base rate inflate a false-positive count?

## Next

Continue with [Standard Exercises](standard.md).
