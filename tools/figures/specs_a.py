"""Procedure specs, demos 01-20. Stage tuple: (kind, role, law, note, where-in-this-demo)."""
S = {}

S["01"] = dict(
    stages=[("env", "Clean export", "tree T, card c", "synthetic service and a symptom card; defect hidden", "fixtures/"),
            ("agent", "Assess", "format f ∈ {free, typed}", "the assessor answers in free text or a typed schema", "student/verified_agent.py"),
            ("defender", "Seal", "h = SHA-256(C)", "at most k files committed before the reveal", "student/format_effect.py"),
            ("defender", "Reveal and score", "hit = [g ∈ C]", "answer key opened only after sealing", "student/oracle_evaluator.py")],
    flows=["T, c", "C", "h, C"],
    output=("Compare formats", "Δ = hit_typed − hit_free", "paired per configuration; exact sign-flip test"),
    scopes=[(2, 4, "after the seal: no edits possible")],
    adversary=[(1, "post-hoc rationalisation")],
    cap1="Blind verification commits the assessor's answer before the key is opened, so the output format is the only thing that differs between arms.",
    adds=["many planted-defect instances and several exact-versioned model configurations",
          "a registered prediction and a decomposition of the format effect, registered before new cells were run",
          "configuration-level bootstrap intervals in place of the toy's single paired difference"],
    new="`student/format_effect.py` (free-text versus typed-schema commitments, sealed before reveal; exact sign-flip floor).")

S["02"] = dict(
    stages=[("env", "CI census", "repos R, workflows W", "pinning, permissions and triggers read from configuration", "fixtures/ci_census.json"),
            ("defender", "Rules", "R1 pin · R2 perms · R3 trigger", "each rule is a violation test on one workflow", "student/enforcement_cost.py"),
            ("defender", "Waivers", "w approved ∧ in force", "approved, scoped, time-bounded exceptions", "fixtures/aibom.json"),
            ("defender", "Fail-closed gate", "BLOCK ⇔ V ∖ W ≠ ∅", "a release waits until every violation is fixed or waived", "student/policy_gate.py")],
    flows=["W", "V", "V ∖ W"],
    output=("Cost of obedience", "share blocked, per rule", "agent repositories against a comparison sample"),
    scopes=[(1, 3, "the gate (trusted)")],
    adversary=[(0, "unpinned or over-privileged step")],
    cap1="A fail-closed gate turns each supply-chain rule into a release decision; counting what it would block is the cost of enforcing it.",
    adds=["a census of real continuous-integration configurations with a comparison sample",
          "independent scanners run in blocking mode beside the gate",
          "one registered hold-out test"],
    new="`student/enforcement_cost.py` (what a fail-closed gate would block across a census of CI configurations).")

S["03"] = dict(
    stages=[("env", "Item bank", "items I, provenance", "benchmark items with their source", "fixtures/"),
            ("defender", "Leakage rules", "Jaccard vs containment", "two rules scored against planted copies", "student/leakage_rules.py"),
            ("defender", "Saturation", "share at ceiling", "is the benchmark still informative?", "student/eval_invariants.py"),
            ("defender", "Transport check", "FPR(τ) as |ref| grows", "a threshold set on one reference may not hold on a larger one", "student/leakage_rules.py")],
    flows=["I", "flags", "τ"],
    output=("Pre-publication gate", "PUBLISH | HOLD", "fail-closed: an unvalidated diagnostic holds the release"),
    scopes=[(1, 4, "executable invariants")],
    adversary=[(0, "contaminated item")],
    cap1="An evaluation's own diagnostics are checked against planted, labelled items before they are trusted.",
    adds=["a large item bank with per-item provenance and a response matrix re-derived from published runs",
          "a natural experiment in which a released benchmark declares the source task of each item",
          "item-response models validated against labelled data"],
    new="`student/leakage_rules.py` (whole-corpus Jaccard against per-item containment, and threshold transport as the reference grows).")

S["04"] = dict(
    stages=[("env", "Public release", "per-case outcomes", "undefended and defended runs of the same cases", "fixtures/zero_audit.json"),
            ("defender", "Exercised denominator", "E = {c : undefended hijacked}", "only these cases can show a reduction", "student/zero_audit.py"),
            ("defender", "Utility", "U = share of user tasks done", "a defence that stops all work also scores zero", "student/zero_audit.py"),
            ("defender", "Authority check", "untrusted ⇏ authority", "the mechanism: content never grants tool authority", "student/authoritybound.py")],
    flows=["outcomes", "|E|", "U"],
    output=("Reading of a zero", "worked | nothing to defend | no power | no utility", "printed beside every reported rate"),
    scopes=[(1, 2, "audit (no model queried)")],
    adversary=[(0, "injected instruction")],
    cap1="A reported zero attack-success rate is read against the cases that could have shown a reduction and the work the agent still does.",
    adds=["the full set of public releases with per-case outcomes found by a documented census",
          "a ledger of inclusion decisions and presented-zero codings",
          "release-level, not model-level, claims"],
    new="`student/zero_audit.py` (four readings of a zero, separated by the exercised denominator and utility).")

S["05"] = dict(
    stages=[("agent", "Agent run", "trace t₁ … tₙ", "each step emits an event", "fixtures/"),
            ("defender", "Witness", "rᵢ = Sig(H(tᵢ) ‖ H(rᵢ₋₁))", "receipts chained and signed outside the agent", "student/eviassure.py"),
            ("defender", "Completeness", "count(r) = count(t)", "an omitted step breaks the chain", "student/eviassure.py"),
            ("defender", "Release gate", "verify(chain) ∧ policy", "evidence, not claims, decides", "student/benchmark.py")],
    flows=["tᵢ", "chain", "verified"],
    output=("Release", "SHIP | HOLD", "omission or tampering holds the release"),
    scopes=[(1, 3, "witness domain (outside the agent)")],
    adversary=[(0, "dropped or edited step")],
    cap1="Witnessed receipts make an omitted or altered step detectable before release.",
    adds=["formal statements of witnessed trace completeness with proofs",
          "a fault model, fault injection and an availability analysis",
          "adversarial-collector campaigns and integrity baselines"])

S["06"] = dict(
    stages=[("env", "Fixture strings", "channel-framed text", "banner, DNS or header carrying an instruction", "fixtures/"),
            ("agent", "Agent", "one probe tool", "single-turn response to each fixture", "student/reconscope.py"),
            ("defender", "Text label", "names target ∨ proposes call", "a lenient heuristic over the response", "student/label_vs_oracle.py"),
            ("defender", "Execution oracle", "nonce at loopback sink", "did the per-trial nonce reach the prohibited socket?", "student/label_vs_oracle.py")],
    flows=["fixture", "response", "same trial"],
    output=("Compare rankings", "rank(text) vs rank(oracle)", "Kendall τ between the two orderings"),
    scopes=[(2, 3, "two labels of the same units")],
    adversary=[(0, "injected banner")],
    cap1="Two labels of the same trials, one from the text and one from the socket, can rank models differently.",
    adds=["a preregistered roster of endpoints across vendor families and serving paths",
          "contemporaneous receipts for every trial, re-derivable offline from open data",
          "rank-instability statistics with intervals"],
    new="`student/label_vs_oracle.py` (text-heuristic labels against a transport-layer execution oracle on identical trials).")

S["07"] = dict(
    stages=[("env", "Artefact", "OLE · PE · JS · LNK", "canary payloads hidden in channels", "fixtures/"),
            ("infra", "Extractor", "survives(channel, mode)", "decides which attacker bytes reach the prompt", "student/triagetrap.py"),
            ("agent", "LLM triage", "verdict ∈ {benign, malicious}", "reads extracted content", "student/triagetrap.py"),
            ("defender", "Provenance gate", "untrusted text ⇏ BENIGN", "quarantine cannot be lifted by artefact text", "student/triagetrap.py")],
    flows=["bytes", "extracted text", "verdict"],
    output=("Quarantine decision", "QUARANTINE | RELEASE", "provenance-gated"),
    scopes=[(3, 4, "gated decision")],
    adversary=[(0, "certification-style text")],
    cap1="The extractor decides which attacker bytes reach the model; a provenance gate stops artefact text from clearing its own artefact.",
    adds=["canaries embedded in real malware families under several extractors",
          "live studies on constructed and real feature records across model lineages",
          "certification wordings compared with imperative ones"])

S["08"] = dict(
    stages=[("env", "Isolated range", "PHP include() target", "lab-only, no external network", "fixtures/"),
            ("agent", "Exploiting agent", "payload family p", "benign and instruction-carrying variants paired", "student/inclusiontrap.py"),
            ("defender", "Tool-call log", "calls C, scope S", "every call recorded against the engagement scope", "student/inclusiontrap.py"),
            ("defender", "Classifier", "hijack ∨ over-reach", "included content as instruction; acting outside scope", "student/generate_inclusion_results.py")],
    flows=["returned file", "calls", "C ⊄ S ?"],
    output=("Verdict per trial", "HIJACK | OVER-REACH | CLEAN", "pre-registered exclusion rule"),
    scopes=[(2, 4, "sealed harness")],
    adversary=[(0, "attacker-authored file")],
    cap1="File content returned by an exploit enters the agent's context, so the exploit can carry instructions back to the exploiter.",
    adds=["sealed live trials over several pinned model generations",
          "a replication on a genuine include() substrate, cell by cell",
          "payload families compared, remote inclusion against local"])

S["09"] = dict(
    stages=[("env", "Wire", "frames f", "sniffed traffic, untrusted by construction", "fixtures/"),
            ("defender", "Scope filter", "f ∈ scope", "out-of-scope frames never reach the agent", "student/interceptbound.py"),
            ("defender", "Taint label", "ℓ ∈ {local, user, wire, forged}", "four-level lattice, propagated", "student/interceptbound.py"),
            ("agent", "Agent action", "a(args)", "TTL-bounded credential buffers", "student/interceptbound.py")],
    flows=["frames", "in-scope f", "f, ℓ"],
    output=("Action guard", "ALLOW ⇔ ℓ(args) ⊑ policy", "downstream confinement"),
    scopes=[(1, 2, "in-line mediation")],
    adversary=[(0, "forged frame")],
    cap1="When the agent is the transport, every observation is untrusted; scope filtering and taint decide what may act.",
    adds=["a verifier-loaded kernel scope filter and stream reassembly",
          "a confinement invariant stated under complete taint propagation",
          "deterministic censuses against an in-segment rogue peer"])

S["10"] = dict(
    stages=[("agent", "Scanner agent", "proposal p", "every proposal kept, even unparseable", "fixtures/blocked_vs_contained.json"),
            ("infra", "Scope resolver", "dest(p) ∈ scope?", "resolves the destination a rule will see", "student/blocked_vs_contained.py"),
            ("defender", "Guardrail", "BLOCK | ALLOW", "destination-scoped rule", "student/scanbound.py"),
            ("agent", "Next proposal", "p′ after a block", "an effect-preserving rewrite", "student/blocked_vs_contained.py")],
    flows=["p", "dest", "blocked"],
    output=("Containment", "contained ≠ blocked", "counted over one fail-closed denominator"),
    scopes=[(1, 2, "deterministic guardrail")],
    adversary=[(3, "proxy or pivot rewrite")],
    cap1="A block is an event; containment is the outcome after the agent's next proposal.",
    adds=["three corpora of live action proposals, one from an isolated laboratory range",
          "several existing guardrail arms expressing one intent",
          "offline simulation of effect-preserving rewrites after a block"],
    new="`student/blocked_vs_contained.py` (blocks against containment, keeping unparseable proposals in the denominator).")

S["11"] = dict(
    stages=[("env", "Reported defences", "rows (work, metric)", "the openly retrievable record", "fixtures/"),
            ("defender", "Degenerate baseline", "π₀ = read nothing", "attains the attacker's-goal rate trivially", "student/audit_reporting.py"),
            ("defender", "Code each row", "reports π₀ on own metric?", "victim-only baseline is not enough", "student/audit_reporting.py"),
            ("defender", "Specification grid", "strict … permissive", "the share under each analysis choice", "student/generate_audit_results.py")],
    flows=["rows", "π₀", "codes"],
    output=("Audit verdict", "PASS | DEGENERATE", "per row and per work"),
    scopes=[(1, 3, "audit protocol")],
    adversary=None,
    cap1="A defence whose number a do-nothing policy also attains says nothing until the do-nothing baseline is reported.",
    adds=["many coded rows from works and detector model cards",
          "quote-verified positive codes and a frozen string screen",
          "a grid of analysis specifications"])

S["12"] = dict(
    stages=[("env", "Message or invite", "envelope, body", "may forward or quote external content", "fixtures/"),
            ("defender", "Sender verdict", "domain authenticated?", "authenticates the domain, not the intent", "student/provenancebound.py"),
            ("defender", "Originator", "identifiable at boundary?", "who wrote the instruction-bearing span?", "student/provenancebound.py"),
            ("defender", "Taint fallback", "value-level labels", "when the originator is not identifiable", "student/provenancebound.py")],
    flows=["message", "verdict", "origin"],
    output=("Authorisation", "ALLOW | DENY", "decided by provenance"),
    scopes=[(1, 3, "authorisation boundary")],
    adversary=[(0, "laundered or quoted content")],
    cap1="Provenance-based authorisation needs the untrusted party to be identifiable at the boundary; forwarding and quoting break that precondition.",
    adds=["historical corporate mail and recent phishing measured under pre-sealed protocols",
          "agent mail tools checked for whether they can pass the sender verdict on",
          "a lexical upper bound on value-level taint in coding-agent sessions"])

S["13"] = dict(
    stages=[("env", "Workspace", "planted defect d", "one synthetic codebase", "fixtures/"),
            ("env", "Coverage cue", "note ∈ {none, true, false}", "upstream metadata every assessor reads", "fixtures/"),
            ("agent", "Assessors", "a₁ … aₖ", "each localises the defect", "student/cue_follower.py"),
            ("defender", "Agreement gate", "accept ⇔ all agree", "agreement cannot see a shared wrong cue", "student/agreement_gate.py")],
    flows=["code", "cue", "files"],
    output=("Localisation hit", "hit(cue) − hit(none)", "and whether agreement rose"),
    scopes=[(2, 3, "assessors share the cue")],
    adversary=[(1, "wrong note")],
    cap1="When every assessor reads the same wrong cue, agreement rises while localisation falls.",
    adds=["a sufficient condition proved for agreement rising while localisation falls",
          "a sealed, preregistered factorial of runs",
          "Holm-adjusted tests on confirmatory planted-defect instances"])

S["14"] = dict(
    stages=[("env", "Calibration set", "scores of injections", "exchangeable with the test traffic?", "fixtures/"),
            ("defender", "Conformal threshold", "τ̂ : risk ≤ α", "split-conformal on calibration scores", "student/conformal_gate.py"),
            ("agent", "Tool call", "score s(x)", "classifier scores the call's input", "student/run_gate.py"),
            ("defender", "Gate", "HOLD ⇔ s ≥ τ̂", "integrity and availability both counted", "student/run_gate.py")],
    flows=["scores", "τ̂", "s"],
    output=("Dependability", "risk vs availability", "same corpus against shifted corpus"),
    scopes=[(1, 1, "bound holds only if exchangeable")],
    adversary=[(2, "shifted or adaptive input")],
    cap1="A conformal bound is a promise about exchangeable traffic; under shift the realised risk can exceed it.",
    adds=["many corpora and replays of recorded agent trajectories",
          "leave-one-suite-out calibration and label-free safeguards",
          "a white-box attacker measured in inserted words"])

S["15"] = dict(
    stages=[("agent", "Open-weight agent", "hidden states hₗ", "read at each layer", "fixtures/"),
            ("defender", "Linear probe", "s = wᵀhₗ", "trained on clean against hijacked episodes", "student/probe.py"),
            ("defender", "Threshold", "flag ⇔ s ≥ τ", "a fixed operating point", "student/run_probe.py"),
            ("defender", "Evaluate", "catches, false alarms", "per episode", "student/run_probe.py")],
    flows=["hₗ", "s", "flags"],
    output=("Where it changes its mind", "layer of first separation", "design stage"),
    scopes=[(1, 3, "monitor")],
    adversary=[(0, "instruction hijack")],
    cap1="A linear read-out of hidden states can flag a hijack at the layer where the model's plan changes.",
    adds=["probes across layers of several open-weight tool-using models",
          "held-out attack families", "every number bound to committed analysis output (design stage)"])

S["16"] = dict(
    stages=[("env", "Ticket", "marker m (instructed) | code c", "matched chains differ only in the instruction", "fixtures/relay_control.json"),
            ("agent", "Agent 1", "reads ticket", "", "student/relay_control.py"),
            ("agent", "Agent 2", "reads agent 1", "", "student/relay_control.py"),
            ("agent", "Agent 3", "reach(m), reach(c)", "did the code arrive?", "student/relay_control.py")],
    flows=["ticket", "output", "output"],
    output=("Instruction effect", "reach(m) − reach(c)", "per model and boundary arm"),
    scopes=[(1, 3, "pipeline (boundary mechanism on hops)")],
    adversary=[(0, "injected relay phrasing")],
    cap1="An uninstructed control code in the same position separates instructed relay from ordinary copying.",
    adds=["many payloads, a random marker per trial, several relay phrasings, models and boundary mechanisms",
          "ticket facts checked to survive the defence",
          "a network simulation with propagated uncertainty"],
    new="`student/relay_control.py` (instructed markers against uninstructed control codes along a three-agent chain).")

S["17"] = dict(
    stages=[("agent", "Coding agent", "actions A, report R", "closes the task with a natural-language report", "fixtures/"),
            ("defender", "Extract claims", "R → {c₁ … cₙ}", "tests ran, files untouched, steps taken", "student/fidelity.py"),
            ("defender", "Predicates", "pᵢ(A) per claim", "versioned, executable checks against the log", "student/fidelity.py"),
            ("defender", "Certificate", "S | C | U | V", "Supported, Contradicted, Unsupported, Unverifiable", "student/run_audit.py")],
    flows=["R", "claims", "verdicts"],
    output=("Report fidelity", "share Contradicted", "a predicate flag rate, not an error rate"),
    scopes=[(1, 3, "audit (log is ground truth)")],
    adversary=None,
    cap1="Each claim in an agent's completion report is checked against the agent's own action log.",
    adds=["a public scrape of terminal-task trials with task-clustered intervals",
          "four certificate outcomes instead of the toy's two",
          "sensitivity analyses for duplicate exports and rule sets"])

S["18"] = dict(
    stages=[("env", "Web content", "payload in language L", "same intent, different language", "fixtures/"),
            ("defender", "Detector", "s(x)", "calibrated mostly on English", "student/detector.py"),
            ("defender", "Calibrate per L", "τ_L", "threshold per language", "student/run_lang.py"),
            ("agent", "Bounded agent test", "acts or not", "does a missed payload change behaviour?", "student/run_lang.py")],
    flows=["x", "s", "τ_L"],
    output=("Language gap", "recall(EN) − recall(L)", "per language"),
    scopes=[(1, 2, "detector")],
    adversary=[(0, "translated injection")],
    cap1="A detector tuned on English phrasing misses the same intent in another language unless it is calibrated per language.",
    adds=["detector calibration across many languages", "a bounded agent test on web content"])

S["19"] = dict(
    stages=[("env", "Model hub", "base b, children", "declared lineage edges", "fixtures/"),
            ("defender", "Default path", "pickle ∧ ¬safetensors", "what a default loader would deserialise", "student/lineage.py"),
            ("defender", "Remote code", "auto_map ≠ ∅", "runs only after an opt-in", "student/lineage.py"),
            ("defender", "Inherit", "parent → child", "exposure along each edge", "student/run_lineage.py")],
    flows=["files", "flags", "edges"],
    output=("Exposure census", "exposed edges / edges", "depth one below each base"),
    scopes=[(1, 3, "file-listing approximation")],
    adversary=[(0, "pickled weights")],
    cap1="What a client fetches by default is decided by file-precedence rules, so exposure is read from file listings along lineage edges.",
    adds=["a depth-one census of declared edges below foundational base models", "parent states recorded at retrieval"])

S["20"] = dict(
    stages=[("env", "Crawl index", "status at /llms.txt", "what the crawler stored", "fixtures/soft404_gate.json"),
            ("env", "Archived bytes", "body b", "the file the server returned", "fixtures/soft404_gate.json"),
            ("defender", "Byte gate", "HTML ⇒ soft-404", "classifier on the bytes, not the status", "student/soft404_gate.py"),
            ("defender", "Tier", "by popularity", "ranked and unranked domains", "student/soft404_gate.py")],
    flows=["200", "b", "class"],
    output=("Adoption", "gated ≤ naive", "agent files, not status codes"),
    scopes=[(2, 3, "validated census")],
    adversary=None,
    cap1="An HTTP 200 at an agent-facing path is a claim by the server; the archived bytes decide whether a file exists.",
    adds=["every partition of both columnar index subsets of one crawl", "a live random-path probe and human labels to validate the gate",
          "a fixed-seed sample of registered domains across popularity tiers"],
    new="`student/soft404_gate.py` (HTTP 200 at an agent-facing path checked byte by byte for soft-404s).")
