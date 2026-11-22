# Tool-Schema Interpretation Divergence Across Agentic Frameworks — the 50 execution prompts

**Demo 89 | venue target: FSE/ICSE | the class: `\documentclass[sigconf,review,anonymous]{acmart} (the ACM class vendored)` | the limit: the FSE/ICSE page limit from the call (typically 10-12 pages excluding references); the registered target is 11 pages**

**How to run:** one prompt per fresh session in GitHub Codespaces, in order, P01 to P50. Every prompt re-runs its predecessor's stated verification before building. Every prompt files its record and updates `docs/pipeline/R1_SEQ_STATE.md`. The prompts are long because the work is deep: the verification depth is the science — run each prompt to its full extent, and do not stop early. **The burn tracks the verification: schemas × frameworks × the interpretation dimensions, each pair's divergence anchored at the pinned code and double-checked**

**The author performs the registration and the upload. The agents perform everything else and record everything. Every `[DECIDE]` goes to the author through the question interface; the answer executes immediately and the resolution is recorded in the same stage.**

---

Phase A — the ground truth

## P01 — The environment and capability probe

**Role:** loop-orchestrator. **Predecessor:** none — this opens the demo.

**Steps:**

1. Read `AGENTS.md`, `docs/pipeline/EXECUTION_PROMPTS.md`, `docs/RESEARCH_QUESTION.md`, `docs/STATE.md`, and `git log --oneline -10`.
2. Verify the toolchain: the Python version (`python3 --version`), the pinned stack (`pip install -q -r requirements.txt` into the session venv — the default interpreter is never used for the pinned stack), and the LaTeX toolchain for the class `\documentclass[sigconf,review,anonymous]{acmart} (the ACM class vendored)` (install from the venue's author kit if absent; record the kit file's SHA-256 in `paper/TEMPLATE_PROVENANCE.md` when vendored).
3. Probe what N is actually available: measure the corpus size from the pinned packs' manifests (files, bytes, the item counts) — the size is recorded, never guessed.
4. Bootstrap the ledger `docs/pipeline/R1_SEQ_STATE.md` with all 50 rows pending.
5. Probe the platform: confirm the Codespace's resources (the CPU count, the memory, the disk) — the day's measurement plan is sized to what the machine can run.
6. Record the capability bounds for the day: what can run, what cannot, and what is deferred.

**Record:** file `docs/pipeline/R1-P01_probe.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase A — the ground truth

## P02 — The corpus pin

**Role:** data-collector. **Predecessor:** P01 — re-run its toolchain verification first.

**Steps:**

1. Fetch the corpus: python3 scripts/fetch_corpus.py --frameworks all --schemas registered --pin-revision; python3 scripts/verify_manifest.py.
2. Write a `MANIFEST.json` per pack: the source URL, the revision/date, the licence, the retrieval time, and **SHA-256 per file** — the hashing loop runs over every file, no sampling.
3. Verify the manifests: re-hash every file against its entry; any mismatch is a stop-and-report.
4. Record the corpus size (files, bytes, the item counts per stratum) — this becomes the paper's N and is never guessed.
5. Check the licences: nothing gated or non-commercial enters without an author decision (`[DECIDE]` filed if any is ambiguous).

**Predecessor verification (re-run before building):** P01's ledger row exists and the toolchain probe recorded
**Record:** file `docs/pipeline/R1-P02_corpus.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase A — the ground truth

## P03 — The hash verification of the corpus

**Role:** science-auditor. **Predecessor:** P02.

**Steps:**

1. Re-hash every file in every pack against its manifest entry — the loop runs over all files, and the pass/fail counts are recorded per pack.
2. Any mismatch is a stop-and-report: the pack is quarantined, the fetch is re-run, and the re-verification is recorded before proceeding.
3. Record the verification table in the stage record (the packs, the file counts, the pass counts, the mismatches).

**Predecessor verification (re-run before building):** P02's manifests exist and the corpus size recorded
**Record:** file `docs/pipeline/R1-P03_hashverify.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase A — the ground truth

## P04 — The hypothesis registration

**Role:** research-scientist. **Predecessor:** P03.

**Steps:**

1. Register the hypotheses in `docs/RESEARCH_QUESTION.md`: H1 — the divergence is systematic per the registered dimensions; H2 — the divergences cause the recorded misbehaviours in the trajectories; H3 — the divergences cluster by framework family.
2. Register the margins and thresholds **before any confirmatory run**; if a threshold requires judgement, file the `[DECIDE]` for the author (the pop-up) and record it.
3. Register the falsification conditions in the same edit: F1 — a divergence claim is a claim about recorded behaviour — a divergence without a recorded instance is removed; F2 — a contested classification beyond the registered agreement bound is re-adjudicated and the outcome recorded; F3 — a framework version mismatch in a pair is recorded honestly and the pair excluded from that comparison.
4. Hash `docs/RESEARCH_QUESTION.md` (sha256), date the registration, and record the hash in the ledger and the stage record.
5. Never register a threshold after the data is seen without disclosing the post-hoc timing in the same sentence.

**Predecessor verification (re-run before building):** P03's verification table shows zero mismatches
**Record:** file `docs/pipeline/R1-P04_hypotheses.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase A — the ground truth

## P05 — The instrument registration

**Role:** research-scientist. **Predecessor:** P04.

**Steps:**

1. Register the instrument in this repository as committed code: the interpretation-diff instrument (the argument binding, the type coercion, the default handling measured per schema-framework pair) + the divergence taxonomy registered over the dimensions.
2. Register the instrument's guards: the divergence taxonomy is a closed list (a divergence outside the registered dimensions is a stop-and-record); the census is double-coded on the registered sample before the classification tables.
3. Register what the instrument cannot measure — the boundaries stated now, not discovered later.
4. Write the instrument's unit checks (the guards fire correctly on the synthetic inputs).
5. The instrument is code in this repository — never a manual pass.

**Predecessor verification (re-run before building):** P04's hash recorded and dated
**Record:** file `docs/pipeline/R1-P05_instrument.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase A — the ground truth

## P06 — The instrument's unit checks

**Role:** science-auditor. **Predecessor:** P05.

**Steps:**

1. Run the instrument's unit checks on the synthetic inputs: every guard fires correctly, every registered class is reachable, every boundary behaves as registered.
2. Record the guard-firing table (the input, the expected guard, the observed).
3. Any guard that does not fire is a stop-and-record: the instrument is repaired before the measurement.

**Predecessor verification (re-run before building):** P05's instrument code committed
**Record:** file `docs/pipeline/R1-P06_unit_checks.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase A — the ground truth

## P07 — The pilot run

**Role:** research-scientist. **Predecessor:** P06.

**Steps:**

1. Run the instrument on a small registered sample (5-10 items from the corpus, sampled with the recorded seed).
2. Verify the outputs' shape: every field populated, every class within the registered list, every anchor resolvable.
3. Record the pilot's observations: the ambiguities the sample exposed, the codebook clarifications needed, the N's feasibility check.
4. **The pilot never enters the paper's results** — it is recorded as the pilot, with its sample and seed.

**Predecessor verification (re-run before building):** P06's guard-firing table green
**Record:** file `docs/pipeline/R1-P07_pilot.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase A — the ground truth

## P08 — the full-N run, part 1: S1

**Role:** research-scientist. **Predecessor:** P07.

**Steps:**

1. Run the instrument over the first stratum — the interpretation census per pair.
2. Commands: every schema-framework pair's interpretation measured per dimension (the argument binding, the type coercion, the default handling); the census recorded per pair.
3. Every item's output recorded with its anchor; no sampling at this stage — the stratum runs at full N.
4. The outputs land under `analysis/out/` with the stratum's run manifest (the seed, the instrument's sha256, the corpus revision).

**Predecessor verification (re-run before building):** P07's pilot recorded and its clarifications applied to the codebook
**Record:** file `docs/pipeline/R1-P08_run_s1.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P09 — the full-N run, part 2: S2

**Role:** research-scientist. **Predecessor:** P08.

**Steps:**

1. Run the instrument over the second stratum — the divergence classification pass.
2. Commands: every measured difference classified per the registered divergence taxonomy (binding, coercion, defaults, error handling); the classes file:line-anchored.
3. Every item's output recorded with its anchor; the stratum's run manifest recorded.
4. The cross-stratum consistency check: the items appearing in both strata carry consistent classifications, or the inconsistency is recorded.

**Predecessor verification (re-run before building):** P08's outputs committed with the run manifest
**Record:** file `docs/pipeline/R1-P09_run_s2.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P10 — the full-N run, part 3: S3

**Role:** research-scientist. **Predecessor:** P09.

**Steps:**

1. Run the instrument over the third stratum — the double-coding pass.
2. Commands: the divergence classifications double-coded on the registered sample; the agreement statistics computed per dimension.
3. Every item's output recorded with its anchor; the stratum's run manifest recorded.
4. The running totals recorded per stratum: the paper's headline numbers begin here.

**Predecessor verification (re-run before building):** P09's outputs committed
**Record:** file `docs/pipeline/R1-P10_run_s3.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P11 — the full-N run, part 4: S4

**Role:** research-scientist. **Predecessor:** P10.

**Steps:**

1. Run the instrument over the fourth stratum — the recorded-misbehaviour anchoring pass.
2. Commands: every divergence linked to the recorded corpus instances where the misbehaviour manifests (the trajectory file:line anchors).
3. Every item's output recorded with its anchor; the full-N run completed — the total N recorded.
4. Commit all four strata's outputs in one commit: the measurement's ground truth is now the repository's own committed record.

**Predecessor verification (re-run before building):** P10's outputs committed
**Record:** file `docs/pipeline/R1-P11_run_s4.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P12 — The determinism re-run

**Role:** science-auditor. **Predecessor:** P11.

**Steps:**

1. Re-run the full measurement (all four strata) with the identical seeds and the identical instrument commit.
2. Compare byte-for-byte: every output file identical, or the diff recorded and investigated — never accepted silently.
3. The determinism verification table recorded per output file (the path, the sha256 before, the sha256 after, the verdict).
4. A non-identical re-run is a stop-and-record: the measurement's determinism is the benchmark's foundation.

**Predecessor verification (re-run before building):** P11's outputs committed as the ground truth
**Record:** file `docs/pipeline/R1-P12_determinism.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P13 — The double-coding

**Role:** second coder (a fresh session, a clean reading). **Predecessor:** P12.

**Steps:**

1. Execute the registered protocol independently over the full N: the second coder reads the items and codes every field per the codebook, without seeing the first coder's entries.
2. The second coder's entries land in separate files; the comparison happens only after both complete.
3. Record the coding time, the codebook ambiguities encountered, and the items that required the codebook re-reading.

**Predecessor verification (re-run before building):** P12's determinism table green
**Record:** file `docs/pipeline/R1-P13_double_coding.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P14 — The agreement statistics

**Role:** science-auditor. **Predecessor:** P13.

**Steps:**

1. Compute the agreement statistics per field: the raw agreement, the registered agreement bound check, and the disagreement list verbatim.
2. The disagreements beyond the registered bound are re-adjudicated by the author (the pop-up); the outcomes recorded verbatim.
3. The agreement table recorded per field — the paper prints this table.

**Predecessor verification (re-run before building):** P13's entries complete over the full N
**Record:** file `docs/pipeline/R1-P14_agreement.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P15 — The falsification condition 1 evaluated

**Role:** science-auditor. **Predecessor:** P14.

**Steps:**

1. Evaluate F1: a divergence claim is a claim about recorded behaviour — a divergence without a recorded instance is removed.
2. The outcome recorded **whatever it is** — confirmation and failure are both legitimate outcomes; only silence is a defect.
3. The evaluation's inputs, the comparison, and the outcome recorded verbatim in the stage record and in the falsification ledger.

**Predecessor verification (re-run before building):** P14's agreement table complete
**Record:** file `docs/pipeline/R1-P15_falsifier1.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P16 — The falsification condition 2 evaluated

**Role:** science-auditor. **Predecessor:** P15.

**Steps:**

1. Evaluate F2: a contested classification beyond the registered agreement bound is re-adjudicated and the outcome recorded.
2. The outcome recorded whatever it is; the ledger updated.

**Predecessor verification (re-run before building):** P15's outcome recorded
**Record:** file `docs/pipeline/R1-P16_falsifier2.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P17 — The falsification condition 3 evaluated

**Role:** science-auditor. **Predecessor:** P16.

**Steps:**

1. Evaluate F3: a framework version mismatch in a pair is recorded honestly and the pair excluded from that comparison.
2. The outcome recorded whatever it is; the ledger updated.

**Predecessor verification (re-run before building):** P16's outcome recorded
**Record:** file `docs/pipeline/R1-P17_falsifier3.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P18 — The claim-ledger construction

**Role:** science-auditor. **Predecessor:** P17.

**Steps:**

1. Build the claim ledger: every number the paper will print, with its arrow shown — the corpus row → the output JSON field → the macro → the body sentence.
2. Zero tolerance: any number without a complete arrow is removed from the ledger and never reaches the paper.
3. The ledger recorded as `docs/pipeline/CLAIM_LEDGER.md` — the paper's numeric spine.

**Predecessor verification (re-run before building):** P17's falsification outcomes recorded
**Record:** file `docs/pipeline/R1-P18_claim_ledger.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase B — the measurement

## P19 — The macro chain

**Role:** paper-writer. **Predecessor:** P18.

**Steps:**

1. Write the macro generator (`scripts/generate_paper_macros.py`): every ledger number emitted as a macro into `docs/generated/macros.tex`, with the source JSON field named in the generated comment per macro.
2. Run the generator; verify the diff contains exactly the ledger's macros — nothing more, nothing less.
3. The macros are the paper's only numeric source: a hand-typed numeral in the body is a violation caught at the review.

**Predecessor verification (re-run before building):** P18's ledger complete with the arrows
**Record:** file `docs/pipeline/R1-P19_macros.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P20 — The paper skeleton at the venue class

**Role:** paper-writer. **Predecessor:** P19.

**Steps:**

1. Vendor the venue's class kit (\documentclass[sigconf,review,anonymous]{acmart} (the ACM class vendored)); record the kit file's SHA-256 in `paper/TEMPLATE_PROVENANCE.md`; the class line is a byte-copy of the template.
2. Stand the skeleton: the abstract (the registered claims, no unregistered numbers), the sections (the divergence matrix (the schemas × the frameworks × the dimensions) as the results spine), the mandatory parts per the venue's structure.
3. Build once; verify zero errors; record the page count.

**Predecessor verification (re-run before building):** P19's macros emitted
**Record:** file `docs/pipeline/R1-P20_skeleton.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P21 — The threat model section

**Role:** paper-writer. **Predecessor:** P20.

**Steps:**

1. Write the threat model section: the adversary, the assets, the trust boundary, the exclusions — registered from `docs/THREAT_MODEL.md`, not invented at the keyboard.
2. Every exclusion stated ("a result that needs a different adversary is a new claim").
3. Verify: every sentence's claim traces to `docs/THREAT_MODEL.md` or the registered instrument's scope.

**Predecessor verification (re-run before building):** P20's skeleton builds
**Record:** file `docs/pipeline/R1-P21_threat_model.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P22 — The design section

**Role:** paper-writer. **Predecessor:** P21.

**Steps:**

1. Write the design section: the population (the corpus, its N, its strata), the unit, the rubric, the instrument, the procedure's five steps — every number macro-bound, every falsification condition printed where the claim is made.
2. The cross-references resolved; the population's N stated exactly as the manifests record.

**Predecessor verification (re-run before building):** P21's threat model complete
**Record:** file `docs/pipeline/R1-P22_design.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P23 — The results section, part 1: the main rates

**Role:** paper-writer. **Predecessor:** P22.

**Steps:**

1. Write the results spine: the divergence matrix (the schemas × the frameworks × the dimensions) and the misbehaviour-anchoring table.
2. Every numeral macro-bound; every rate with its interval; every denominator printed; every falsification condition evaluated and its outcome stated beside the claim.
3. Verify: every macro resolves; every arrow in the claim ledger reaches this section.

**Predecessor verification (re-run before building):** P22's design section complete
**Record:** file `docs/pipeline/R1-P23_results_core.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P24 — The results section, part 2: the secondary tables

**Role:** paper-writer. **Predecessor:** P23.

**Steps:**

1. Write the secondary results: the double-coding agreement table per dimension; the framework-family clustering table; the version-mismatch exclusions recorded.
2. Every table's caption self-contained (the denominators restated); every number macro-bound.

**Predecessor verification (re-run before building):** P23's results spine complete
**Record:** file `docs/pipeline/R1-P24_results_secondary.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P25 — The analysis and discussion section

**Role:** paper-writer. **Predecessor:** P24.

**Steps:**

1. Write the analysis: what the results mean for the registered hypotheses, what they do not mean, and where the falsification conditions bound the claims.
2. The discussion never widens a claim past its registered scope: the corpus-scoped claims stay corpus-scoped.

**Predecessor verification (re-run before building):** P24's secondary results complete
**Record:** file `docs/pipeline/R1-P25_discussion.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P26 — The related work section

**Role:** paper-writer. **Predecessor:** P25.

**Steps:**

1. Write the related work: the API-misuse and schema-evolution literature, the cross-framework interop literature, the MCP/A2A spec papers; each positioned by what it measures versus what this study diffs.
2. Every rival positioned by what it measures versus what this paper measures — the difference stated in one sentence per rival, never a bare list.
3. Every citation verified against the source (the title, the venue, the year — checked, not assumed); the bibliography committed.

**Predecessor verification (re-run before building):** P25's discussion complete
**Record:** file `docs/pipeline/R1-P26_related_work.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P27 — The limitations and threats section

**Role:** paper-writer. **Predecessor:** P26.

**Steps:**

1. Write the threats-to-validity section: the rubric's stability, the population's scope, the instrument's blind spots, the corpus's coverage — every limitation carried from the registration, none discovered at the keyboard.
2. Every lower bound framed as a lower bound; every absence recorded as an absence.

**Predecessor verification (re-run before building):** P26's related work complete
**Record:** file `docs/pipeline/R1-P27_limitations.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P28 — The appendices and the mandatory parts

**Role:** paper-writer. **Predecessor:** P27.

**Steps:**

1. Write the appendices per the venue's mandatory structure: the artefact description, the ethics, the AI-usage disclosure — the venue's requirements read from the call and stated in the record.
2. Every appendix self-contained; the body never leans on an appendix for a headline claim.

**Predecessor verification (re-run before building):** P27's limitations complete
**Record:** file `docs/pipeline/R1-P28_appendices.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase C — the paper

## P29 — The figures

**Role:** paper-writer plus verifier. **Predecessor:** P28.

**Steps:**

1. Generate the figures from the committed outputs (never hand-drawn data); every plotted number macro-bound; every caption self-contained with its denominators.
2. Verify the legibility at the print size (the fonts, the line widths, the colour independence).
3. Determinism: every figure regenerated twice and byte-compared; the drift recorded, never committed silently.

**Predecessor verification (re-run before building):** P28's appendices complete
**Record:** file `docs/pipeline/R1-P29_figures.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase D — the audit

## P30 — The page-budget chase

**Role:** paper-writer plus verifier. **Predecessor:** P29.

**Steps:**

1. Build; measure the boundary (`grep bodyend` + one page extraction); the overflow quantified in lines.
2. Chase per build: the condensation passes (the bounded sentence-level edits, every disclosure kept), the float moves (the recorded fallback), the baseline adjustments (the reversible levers, recorded in the source comment) — until the boundary holds at the venue's limit.
3. Every iteration's before/after recorded; the final boundary verified by text extraction, not by the label alone.

**Predecessor verification (re-run before building):** P29's figures complete
**Record:** file `docs/pipeline/R1-P30_page_budget.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase D — the audit

## P31 — The citation sweep

**Role:** hallucination-auditor. **Predecessor:** P30.

**Steps:**

1. Verify every bibliography entry against the source (the title, the venue, the year, the DOI — checked via the free APIs or the publisher pages, never assumed).
2. Sweep the body for hand-typed numerals not macro-bound; every hit traces to the ledger or is removed.
3. The conflicts recorded (where the sources disagree, the publisher of record wins) — never silently corrected.

**Predecessor verification (re-run before building):** P30's boundary holds
**Record:** file `docs/pipeline/R1-P31_citations.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase D — the audit

## P32 — The concordance pass

**Role:** concordance-auditor. **Predecessor:** P31.

**Steps:**

1. Sweep the manuscript: the terminology drift (one concept, two names), the notation inconsistencies, the broken cross-references, the duplicated sentences, the macro-usage gaps.
2. The fix list recorded, ordered by severity; the fixes applied as bounded edits; the boundary re-measured after the edits.

**Predecessor verification (re-run before building):** P31's citations verified
**Record:** file `docs/pipeline/R1-P32_concordance.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase D — the audit

## P33 — The anonymity gate

**Role:** venue-compliance-auditor. **Predecessor:** P32.

**Steps:**

1. Run the anonymity gate over the whole tree; the findings recorded by class; nothing on an export-facing path.
2. The PDF metadata verified to the byte level (Title, Author empty); the acknowledgments and the appendices verified against the venue's structure requirements.

**Predecessor verification (re-run before building):** P32's concordance complete
**Record:** file `docs/pipeline/R1-P33_anonymity.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase D — the audit

## P34 — The macro parity re-verification

**Role:** science-auditor. **Predecessor:** P33.

**Steps:**

1. Regenerate the macros; verify the byte-identity against the committed file — any drift is a stop-and-record.
2. Re-derive every headline number end-to-end (the corpus row → the JSON → the macro → the body) — every arrow shown, zero tolerance.

**Predecessor verification (re-run before building):** P33's anonymity clean
**Record:** file `docs/pipeline/R1-P34_macro_parity.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase E — the audit, round two

## P35 — The adversarial review

**Role:** paper-evaluator (read-only). **Predecessor:** P34.

**Steps:**

1. Read the full manuscript as a hostile committee member; produce the ten most likely rejection reasons ranked, each with: the exact claim under attack (quoted and located), why a reviewer attacks it, the strongest defence available from the committed artefact, and whether that defence is already in the text, missing, or impossible.
2. Nothing edited — the review is a record the writer pass consumes.

**Predecessor verification (re-run before building):** P34's parity holds
**Record:** file `docs/pipeline/R1-P35_adversarial.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase E — the audit, round two

## P36 — The writer pass

**Role:** paper-writer. **Predecessor:** P35.

**Steps:**

1. Consolidate the review's critiques into the disposition ledger (the fix-now set, the author proposals, the parked items, the rejections with reasons).
2. Apply the fix-now set as bounded edits: British English, third person, additive scoping sentences before any qualifying rewrite; every numeric token macro-bound.
3. The per-edit annotation filed in the record, naming the critique each edit answers.

**Predecessor verification (re-run before building):** P35's review filed
**Record:** file `docs/pipeline/R1-P36_writer_pass.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase E — the audit, round two

## P37 — The delta verification

**Role:** hallucination-auditor. **Predecessor:** P36.

**Steps:**

1. Take the exact diffs of the writer pass; for every numeric token, claim and citation introduced: trace it to a committed source. Any untraceable token is reverted on the spot and recorded.
2. Verify the edits never cross a recorded scope: no claim widened, no lower bound promoted, no `[DECIDE]` resolved.

**Predecessor verification (re-run before building):** P36's edits complete
**Record:** file `docs/pipeline/R1-P37_delta_verify.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase E — the audit, round two

## P38 — The delta re-review

**Role:** paper-evaluator (read-only). **Predecessor:** P37.

**Steps:**

1. Review only the changed lines against the critiques they claim to answer: genuinely addressed, cosmetically addressed, or wrongly parked.
2. The residual list carried to the freeze.

**Predecessor verification (re-run before building):** P37's verification complete
**Record:** file `docs/pipeline/R1-P38_delta_review.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase E — the audit, round two

## P39 — The determinism battery, post-edit

**Role:** science-auditor. **Predecessor:** P38.

**Steps:**

1. Re-run the full measurement chain after all edits; byte-identical verification per output.
2. The falsification conditions re-evaluated (the edits must not have changed the outcomes); the ledger re-derived end to end.

**Predecessor verification (re-run before building):** P39's chains re-run
**Record:** file `docs/pipeline/R1-P39_battery2.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase E — the audit, round two

## P40 — The claim-ledger re-derivation

**Role:** science-auditor. **Predecessor:** P39.

**Steps:**

1. Re-derive every headline number end-to-end from the committed outputs: every arrow shown, zero tolerance — one untraceable number is a stop-and-record.
2. The claim ledger's rows against the final text; stale rows are findings.

**Predecessor verification (re-run before building):** P39's battery green
**Record:** file `docs/pipeline/R1-P40_ledger2.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase E — the audit, round two

## P41 — The venue compliance

**Role:** venue-compliance-auditor. **Predecessor:** P40.

**Steps:**

1. The full checklist on the final build: the template byte-copy (the class line a byte-copy of the venue's kit), the page limit with the recorded exemption, zero Type 3 fonts, zero overfull, the metadata anonymisation to the byte level, the mandatory sections present, the structure per the call.
2. Every no-go item named, located and assigned; every pass with its measurement recorded.

**Predecessor verification (re-run before building):** P40's re-derivation green
**Record:** file `docs/pipeline/R1-P41_compliance.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase E — the audit, round two

## P42 — The artefact packaging

**Role:** loop-orchestrator. **Predecessor:** P41.

**Steps:**

1. Assemble the artefact package per `docs/ARTEFACT_PLAN.md`: the export set computed mechanically, the manifests with SHA-256 per file, the anonymity gate on the assembled set.
2. Any gate finding stops the export; the package is a proposal until the author ratifies.

**Predecessor verification (re-run before building):** P41's checklist recorded
**Record:** file `docs/pipeline/R1-P42_packaging.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase F — the assessment

## P43 — The artefact readiness and the badges

**Role:** science-auditor. **Predecessor:** P42.

**Steps:**

1. Verify the availability statement's claims against the actual bundles; assess the badge eligibility honestly (available / functional / reproduced — what the artefact supports today and what it would need).
2. The gaps are proposals with the exact missing piece named — never new data collection.

**Predecessor verification (re-run before building):** P42's package assembled
**Record:** file `docs/pipeline/R1-P43_readiness.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase F — the assessment

## P44 — The rebuttal bank

**Role:** paper-evaluator (read-only). **Predecessor:** P43.

**Steps:**

1. Build the rebuttal bank: for each of the top objections, the pointer-answer with its artefact evidence (the file and the row), classified — which answers need no new measurement, which need the parked items, which are honest limitations to concede.

**Predecessor verification (re-run before building):** P43's readiness recorded
**Record:** file `docs/pipeline/R1-P44_rebuttal_bank.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase F — the assessment

## P45 — The AC-question assessment

**Role:** paper-evaluator (read-only). **Predecessor:** P44.

**Steps:**

1. Answer the programme chair's question directly: is this paper ready to be accepted — and if not, the single change that would most raise the odds.
2. The honest weak spots to own in the rebuttal, each with the strongest pre-drafted answer from the committed artefact; the risks that cannot be answered named plainly.

**Predecessor verification (re-run before building):** P44's bank complete
**Record:** file `docs/pipeline/R1-P45_ac_question.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase G — the freeze

## P46 — Repair slot A

**Role:** paper-writer plus verifier. **Predecessor:** the ledger's latest failure record.

**Steps:**

1. Pick the highest-severity open item; repair within house rules; re-run the failed gate until green; record before and after.

**Record:** file `docs/pipeline/R1-P46_repairA.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase G — the freeze

## P47 — Repair slot B, science-priority

**Role:** science-auditor plus research-scientist. **Predecessor:** the ledger.

**Steps:**

1. The science-integrity priority: the claim-ledger drift, the scope violations, the untraceable numbers first; formatting last. A dated block appended each run.

**Record:** file `docs/pipeline/R1-P47_repairB.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase G — the freeze

## P48 — The deadline watch

**Role:** venue-compliance-auditor. **Predecessor:** P45.

**Steps:**

1. The CFP re-probe; the countdown recorded; any drift an author alert at the top of the record.
2. The registration confirmation recorded (the author confirms; the receipt details filed).

**Predecessor verification (re-run before building):** P44's deadline state carried
**Record:** file `docs/pipeline/R1-P48_deadline.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase G — the freeze

## P49 — The seal

**Role:** loop-orchestrator. **Predecessors:** P40–P48.

**Steps:**

1. Record the final state: every gate with its numbers, every author action with its deadline, every parked item with its executor.
2. Nothing tagged — the author tags.

**Predecessor verification (re-run before building):** P40-P48's rows closed
**Record:** file `docs/pipeline/R1-P49_seal.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

Phase G — the freeze

## P50 — The final author handoff

**Role:** loop-orchestrator. **Predecessor:** the ledger at its final state.

**Steps:**

1. The one-page handoff: the commit delta (one line each), the deadlines with the remaining author actions, the parked items with reasons and executors, the rebuttal-bank pointer. Print-ready; no new claims.

**Record:** file `docs/pipeline/R1-P50_handoff.md` with the full execution narrative, the measured numbers, and the falsification notes; update `docs/pipeline/R1_SEQ_STATE.md`; commit and push.

**Rules (unchanged, every prompt):** secondary sources only, every pack with a `MANIFEST.json`; no paid APIs; no live attacks; no human subjects; never write a number that did not come from a shown calculation or a cited file; every hypothesis carries its falsification condition in the same edit; never resolve a `[DECIDE]` marker — propose and leave it, only the author resolves; British English, third person; failures reported faithfully; the registration and the upload are the author's. **Commit:** stage only this prompt's changed files, commit with a proper message, push to origin; if a gate fails, record and stop.


---

*End of the sequence. The paper is submission-ready when the seal (P49) records every gate green and the handoff (P50) is filed. The author performs the registration and the upload.*
