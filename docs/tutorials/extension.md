# Extension Exercises

Independent work for readers who have completed the standard tier: cryptographic evidence, scope control and measurement limits. Allow three to four hours.

## Core exercises

| Order | Demo | What to do | Lab |
|:---:|---|---|---|
| 1 | [Evidence Assurance](../demos/05-eviassure.md) | Verify a Merkle inclusion proof and tamper with one leaf | [Lab 05](../course/lab-05-eviassure.md) |
| 2 | [ScanBound](../demos/10-scanbound.md) | Add an out-of-scope target and watch the guard fire | [Lab 10](../course/lab-10-scanbound.md) |
| 3 | [Degenerate Reporting](../demos/11-degenerate-reporting.md) | Score a do-nothing policy against the reported metric | [Lab 11](../course/lab-11-degenerate-reporting.md) |
| 4 | [ProvenanceBound](../demos/12-provenancebound.md) | Add a paraphrase that the lexical detector misses | [Lab 12](../course/lab-12-provenancebound.md) |
| 5 | [Toolflow Taint](../demos/44-toolflow-taint.md) | Add a labelled flow across two tool hops | — |
| 6 | [Pre-reveal Seal](../demos/47-blind-seal.md) | Edit a sealed answer and verify the mismatch | — |

## Check your understanding

- What does a hash chain prove that a log file does not?
- Why is scope validation necessary even when the scanner is correct?
- Which reported metric could a do-nothing policy win?
- Why must provenance outrank a detector's classification?
- Where does a taint label get lost between tools?

## Capstone

Pick one demo and write a one-page claim ledger: the question, the fixture, the baseline, the measured quantity and the limit of the claim. Use the [assessment rubric](../demos/overview.md#assessment-rubric) as the marking guide.
