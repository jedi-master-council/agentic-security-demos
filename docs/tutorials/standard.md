# Standard Exercises

The middle tier: evaluation design, authority boundaries and provenance. Allow three to four hours after the beginner tier.

## Core exercises

| Order | Demo | What to do | Lab |
|:---:|---|---|---|
| 1 | [Evaluation Invariants](../demos/03-eval-invariants.md) | Break one of the five evaluation checks | [Lab 03](../course/lab-03-eval-invariants.md) |
| 2 | [Authority Bound](../demos/04-authoritybound.md) | Trace how provenance becomes authority | [Lab 04](../course/lab-04-authoritybound.md) |
| 3 | [InclusionTrap](../demos/08-inclusiontrap.md) | Separate reading a file from executing it | [Lab 08](../course/lab-08-inclusiontrap.md) |
| 4 | [InterceptBound](../demos/09-interceptbound.md) | Follow a taint label to a blocked action | [Lab 09](../course/lab-09-interceptbound.md) |
| 5 | [Typed Commitments](../demos/13-typed-commitments.md) | Show how a shared wrong cue defeats agreement | — |
| 6 | [Conformal Gating](../demos/14-conformal-gating.md) | Find the coverage failure under shift | — |

## Check your understanding

- Which invariant catches leakage that accuracy does not?
- Where does the confused-deputy path cross a capability boundary?
- Why does a taint label need an action guard, not just a warning?
- Why can two agreeing assessors still be wrong together?

## Next

Continue with [Extension Exercises](extension.md).
