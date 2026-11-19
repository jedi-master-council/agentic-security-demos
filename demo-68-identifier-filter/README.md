# Demo 68: What Gets Past the Filter? Identifier Residue and Re-identification Risk in Learner Text Sent to Hosted Language Models

> **▶️ New here? Follow the step-by-step [Execution Instructions](INSTRUCTIONS.md)** — every command with expected output.

**Status (19 November 2026):** design stage. A teaching toy with labelled synthetic fixtures runs offline and its tests pass. **No pilot data have been collected and no results exist.** Every study quantity is `[RESULT PENDING]`.

## Research question

When typed learner text passes through an identifier filter before it reaches a hosted language model, which identifiers get through, at what rate by type and phrasing, and how often do the quasi-identifiers that remain single out one person in a roster?

## Why it matters

Study assistants built on hosted models send what learners type to a third party. Filtering common identifiers before text leaves the institution is a standard safeguard, but its residue is rarely measured, and redacting direct identifiers does not remove the combinations of attributes that can identify someone.

## Design of the pilot study

| Arm or control | What it is |
|---|---|
| Rule filter | regular expressions for e-mail addresses, UK telephone numbers, UK postcodes and a student-number format, plus a name list |
| Rule filter with a local model | the same rules followed by a local open-weight model asked to mark remaining identifiers (pilot only) |
| Re-identification check | remaining quasi-identifiers matched against a synthetic roster; a message is flagged when exactly one entry matches |

**Outcomes**
- primary: span-level recall per identifier type on scripted messages written to include ordinary, obfuscated and case-varied identifiers
- secondary: precision (false redaction of subject content such as numbers in statistics problems); share of messages whose remaining quasi-identifiers single out one roster entry

**How the pilot runs.** Scripted messages and a synthetic roster written for this check only; no participants and no real learner text. The local model, if used, runs on the machine through Ollama and its tag and digest are logged. The steps are in [`ZCODE_PROMPT.md`](ZCODE_PROMPT.md); the study is registered in `docs/` before the first real run.

**Data.** Scripted synthetic messages, hand-labelled spans and a synthetic roster.

## The teaching toy

`student/idfilter.py` implements the measurement on `fixtures/messages.json`; `student/run_idfilter.py` prints one line per case and writes `results/idfilter.json`. Every number it prints belongs to the toy fixture and is not evidence about any real system, dataset or population.

## Learning objectives

- State the measurement question and the registered primary outcome
- Run the offline procedure on the labelled synthetic fixture
- Explain which control or baseline makes the outcome interpretable
- Distinguish the teaching output from a confirmatory research result

## Venues

| Option | Venue | Dates and rules |
|---|---|---|
| A | [Proceedings on Privacy Enhancing Technologies (PoPETs) 2027, Issue 4](https://www.petsymposium.org/cfp27.php) | submission 28 Feb 2027 (firm, AoE); rebuttal 10 to 16 Apr 2027; notification 1 May 2027; revision deadline 1 Jun 2027. at most four submissions per author per issue; rejected papers must skip a full issue; page limit not read (UNVERIFIED). Issue 3 (30 Nov 2026) is nearer but leaves eleven days and no data, so it is not used |
| B | [ACM Transactions on Privacy and Security (TOPS)](https://dl.acm.org/journal/tops) | rolling submission. use only after PoPETs' notification on 1 May 2027 |
| C | [IEEE Transactions on Information Forensics and Security (TIFS)](https://signalprocessingsociety.org/publications-resources/ieee-transactions-information-forensics-and-security) | rolling submission. use only after ACM TOPS' decision; page limit and fees UNVERIFIED |

B and C are sequential fallbacks: each is used only after the previous option's official notification, so the same work is never under review in two places. Paste-ready fields are in `submission/option-A/`, `option-B/` and `option-C/` (`REGISTRATION.md`).

**Risks for the venue plan**
- None recorded beyond the UNVERIFIED items above.

## Safety notice

⚠️ **This is a teaching demonstration using synthetic fixtures only.**
- No real people, credentials, production systems or provider accounts
- No network access in the toy (standard library only)
- Results demonstrate a mechanism; they are not evidence about real deployments

## Reproducibility metadata

| Field | Value |
|-------|-------|
| Seed | 68 where randomness is used |
| Python | 3.11+ (standard library only) |
| Command | `make demo DEMO=68` |

## Author

Petar Radanliev, The Open University (ORCID [0000-0001-5629-6857](https://orcid.org/0000-0001-5629-6857)).
