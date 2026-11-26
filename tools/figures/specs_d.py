"""Procedure specs, demos 66-90."""
S = {}

S["66"] = dict(
    stages=[("env", "Job queue", "circuits", "fixed QPU-time budget", "fixtures/"),
            ("agent", "Workflow arm", "default | rule | simulate-first", "how each job is submitted", "student/qpu_budget.py"),
            ("infra", "QPU", "seconds spent", "simulated hardware", "student/qpu_budget.py"),
            ("defender", "Acceptance", "result passes check?", "accepted results only", "student/run_qpu_budget.py")],
    flows=["jobs", "submissions", "results"],
    output=("Efficiency", "accepted results per QPU-second", "per arm"),
    scopes=[(1, 2, "fixed budget")],
    adversary=None,
    cap1="Under a fixed hardware budget, the workflow that filters jobs before submission can return more accepted results per second.",
    adds=["pilot runs on real hardware time", "design stage: no pilot data yet"])

S["67"] = dict(
    stages=[("env", "Public release", "linked tables", "learner records", "fixtures/"),
            ("agent", "Model", "completes rows", "row and cross-table prompts", "student/memprobe.py"),
            ("env", "Remapped control", "same schema, new values", "the model cannot have seen it", "fixtures/"),
            ("defender", "Score", "real vs remapped", "at a fixed false-positive rate", "student/run_memprobe.py")],
    flows=["rows", "completions", "null"],
    output=("Memorisation", "excess over the remapped null", "validated probe"),
    scopes=[(2, 3, "control-based validation")],
    adversary=None,
    cap1="A memorisation probe is validated by how it scores on remapped tables the model cannot have seen.",
    adds=["a public multi-table learner dataset", "design stage"])

S["68"] = dict(
    stages=[("env", "Learner messages", "with identifiers", "scripted", "fixtures/"),
            ("defender", "Filter", "rule-based redaction", "before the hosted model", "student/idfilter.py"),
            ("defender", "Residue", "spans that got through", "span-level recall", "student/idfilter.py"),
            ("defender", "Re-identification", "k = 1 records", "unique combinations left", "student/run_idfilter.py")],
    flows=["text", "redacted", "residue"],
    output=("Risk", "recall · residue · k = 1 share", "per identifier type"),
    scopes=[(1, 3, "filter audit")],
    adversary=None,
    cap1="What gets past an identifier filter is measured span by span, then as re-identification risk.",
    adds=["scripted learner messages at scale", "design stage"])

S["69"] = dict(
    stages=[("env", "Provider terms", "published text", "tiers, data use, price", "fixtures/"),
            ("agent", "Extractor", "clause + quote", "model-assisted", "fixtures/"),
            ("defender", "Grounding", "quote ∈ source?", "verbatim check", "student/grounding.py"),
            ("defender", "Consistency", "value matches quote?", "price, continuity, exit", "student/run_grounding.py")],
    flows=["text", "claims", "grounded"],
    output=("Extraction", "grounded share", "per term type"),
    scopes=[(2, 3, "grounding checks")],
    adversary=[(1, "hallucinated clause")],
    cap1="Every extracted clause must be found verbatim in the source before its value is trusted.",
    adds=["providers' published terms", "design stage"])

S["70"] = dict(
    stages=[("env", "Assignments", "users → roles", "effective RBAC", "fixtures/"),
            ("defender", "Expand", "roles → permissions", "effective permission sets", "student/sod.py"),
            ("defender", "SoD pairs", "mutually exclusive", "e.g. approve and post payment", "student/sod.py"),
            ("defender", "Detect", "pair ⊆ perms(u)", "per user", "student/run_sod.py")],
    flows=["roles", "perms", "pairs"],
    output=("Conflicts", "users in conflict", "deterministic"),
    scopes=[(1, 3, "analysis")],
    adversary=None,
    cap1="Separation-of-duty conflicts appear only after roles are expanded into effective permissions.",
    adds=["public access-control datasets", "scaling to large role graphs"])

S["71"] = dict(
    stages=[("env", "Instance", "x, weights w", "a linear score", "fixtures/"),
            ("defender", "Candidates", "feature subsets", "ordered by erasure cost", "student/erasure.py"),
            ("defender", "Search", "cheapest flip", "complete heuristic search", "student/erasure.py"),
            ("defender", "Certificate", "score(x ∖ S) < 0", "the erasure that flips it", "student/run_erasure.py")],
    flows=["x", "subsets", "S*"],
    output=("Minimum erasure", "cost(S*)", "per instance"),
    scopes=[(1, 3, "search")],
    adversary=[(0, "evasion")],
    cap1="The cheapest set of feature erasures that flips a linear score is found by search.",
    adds=["larger feature spaces", "complexity results"])

S["72"] = dict(
    stages=[("env", "Technique catalogue", "techniques T", "public", "fixtures/"),
            ("env", "Control catalogue", "controls C", "public", "fixtures/"),
            ("defender", "Align", "T ↔ C by set overlap", "shared mitigations", "student/mapping.py"),
            ("defender", "Uncovered", "T with no C", "the gap", "student/run_mapping.py")],
    flows=["T", "C", "pairs"],
    output=("Mapping", "coverage per technique", "set-based"),
    scopes=[(2, 3, "alignment")],
    adversary=None,
    cap1="Techniques are aligned to compensating controls by the mitigations they share.",
    adds=["full public catalogues", "an evaluation against expert mappings"])

S["73"] = dict(
    stages=[("env", "Training classes", "histogram patterns", "known classes", "fixtures/"),
            ("defender", "Class means", "μ_c", "nearest-class-mean", "student/ncm.py"),
            ("defender", "Distance", "d(x, μ_c)", "to the nearest mean", "student/ncm.py"),
            ("defender", "Reject", "d > θ ⇒ unknown", "open set", "student/run_ncm.py")],
    flows=["x", "μ", "d"],
    output=("Prediction", "class | unknown", "per sample"),
    scopes=[(1, 3, "classifier")],
    adversary=[(0, "novel pattern")],
    cap1="A distance threshold lets a nearest-class-mean classifier say 'unknown'.",
    adds=["real histogram patterns", "threshold selection under a budget"])

S["74"] = dict(
    stages=[("env", "Two-layer map", "W₂ σ(W₁ x)", "linear layers", "fixtures/"),
            ("defender", "Spectral norm", "‖W₁‖₂, ‖W₂‖₂", "exact for 2 × 2", "student/lipschitz.py"),
            ("defender", "Product bound", "L ≤ ‖W₂‖₂ ‖W₁‖₂", "upper bound", "student/lipschitz.py"),
            ("defender", "Check", "observed ratio ≤ L", "on sample pairs", "student/run_lipschitz.py")],
    flows=["W", "norms", "L"],
    output=("Certificate", "Lipschitz bound", "and its slack"),
    scopes=[(1, 3, "analysis")],
    adversary=[(0, "perturbation")],
    cap1="The product of spectral norms bounds how far a perturbation can move the output.",
    adds=["deeper networks", "tighter bounds than the product"])

S["75"] = dict(
    stages=[("env", "Advisory sources", "A, B, C", "public feeds", "fixtures/"),
            ("defender", "Link", "exact identifier", "same vulnerability", "student/linkage.py"),
            ("defender", "Compare severity", "strings per source", "normalised", "student/linkage.py"),
            ("defender", "Disagreement", "linked ∧ different", "per pair", "student/run_linkage.py")],
    flows=["records", "links", "severities"],
    output=("Linkage", "linked · disagreeing", "per source pair"),
    scopes=[(1, 3, "linkage")],
    adversary=None,
    cap1="Advisories are linked on exact identifiers before their severities are compared.",
    adds=["full public advisory feeds", "fuzzy linkage evaluated against exact links"])

S["76"] = dict(
    stages=[("env", "Graph", "nodes, attacker paths", "routes to targets", "fixtures/"),
            ("defender", "Budget", "k patrol nodes", "resources", "student/patrol.py"),
            ("defender", "Search", "exhaustive | greedy", "anytime", "student/patrol.py"),
            ("defender", "Coverage", "paths hitting the set", "uncovered paths", "student/run_patrol.py")],
    flows=["paths", "k", "set"],
    output=("Allocation", "minimum uncovered", "optimal against greedy"),
    scopes=[(1, 3, "search")],
    adversary=[(0, "attacker path")],
    cap1="A patrol set is good when few attacker paths avoid it; search finds the best k nodes.",
    adds=["larger graphs", "anytime bounds"])

S["77"] = dict(
    stages=[("env", "Knowledge base", "Horn clauses", "facts and rules", "fixtures/"),
            ("defender", "Forward chain", "derive ⊥?", "inconsistency", "student/horn.py"),
            ("defender", "Candidates", "deletion sets", "smallest first", "student/horn.py"),
            ("defender", "Repair", "KB ∖ D ⊬ ⊥", "minimum deletion", "student/run_horn.py")],
    flows=["clauses", "⊥", "D"],
    output=("Repair", "minimum D", "consistency restored"),
    scopes=[(1, 3, "reasoning")],
    adversary=None,
    cap1="The smallest set of clauses whose deletion stops the derivation of falsehood restores consistency.",
    adds=["larger knowledge bases", "complexity analysis"])

S["78"] = dict(
    stages=[("env", "URLs", "lexical features", "labelled", "fixtures/"),
            ("defender", "Best rule", "single feature", "maximum precision", "student/covering.py"),
            ("defender", "Remove covered", "examples it explains", "then repeat", "student/covering.py"),
            ("defender", "Decision list", "ordered rules", "first match decides", "student/run_covering.py")],
    flows=["features", "rule", "rest"],
    output=("Classifier", "ordered rule list", "interpretable"),
    scopes=[(1, 3, "learning")],
    adversary=[(0, "phishing URL")],
    cap1="Sequential covering learns one rule at a time and removes what it already explains.",
    adds=["real URL datasets", "comparison with other interpretable learners"])

S["79"] = dict(
    stages=[("env", "Window 1", "items", "earlier period", "fixtures/"),
            ("env", "Window 2", "items", "later period", "fixtures/"),
            ("defender", "Support", "supp₁, supp₂", "per item set", "student/contrast.py"),
            ("defender", "Growth", "supp₂ / supp₁ ≥ ρ", "emerging set", "student/run_contrast.py")],
    flows=["supp₁", "supp₂", "ratio"],
    output=("Emerging sets", "growth ≥ ρ", "per item set"),
    scopes=[(2, 3, "mining")],
    adversary=None,
    cap1="An item set is emerging when its support grows enough between adjacent windows.",
    adds=["real event logs", "significance control for many sets"])

S["80"] = dict(
    stages=[("env", "Defence papers", "screened records", "systematic search", "fixtures/fixtures.json"),
            ("agent", "Coder A", "layer, guarantee, adaptive", "three fields", "fixtures/fixtures.json"),
            ("agent", "Coder B", "same fields", "independent", "fixtures/fixtures.json"),
            ("defender", "Agreement", "κ per field ≥ 0.6?", "disagreements go to adjudication", "student/extract.py")],
    flows=["papers", "codes A", "codes B"],
    output=("Systematic map", "layer × adaptive testing", "agreed items only"),
    scopes=[(1, 3, "double-coded extraction")],
    adversary=None,
    cap1="Two coders extract the same fields independently; chance-corrected agreement decides whether a field is usable.",
    adds=["a large screened literature committed in several stages", "a sealed systematic map", "utility cost and formal guarantee fields"])

S["81"] = dict(
    stages=[("env", "Pinned corpora", "SHA-256 manifest", "refuse on mismatch", "fixtures/fixtures.json"),
            ("defender", "Frozen gate", "lexicon A ∧ lexicon B", "no model, no randomness", "student/harness.py"),
            ("defender", "Run twice", "table hash h₁, h₂", "byte for byte", "student/harness.py"),
            ("defender", "Score", "tp, fp, fn, tn", "against labels", "student/harness.py")],
    flows=["corpus", "flags", "h₁ = h₂"],
    output=("Benchmark", "reproducible baseline", "reproducible is not correct"),
    scopes=[(1, 3, "zero-GPU harness")],
    adversary=[(0, "altered corpus")],
    cap1="Pinned data and a frozen gate make a benchmark re-runnable byte for byte.",
    adds=["many SHA-256-pinned external corpora across four domains", "baselines packaged for re-use"])

S["82"] = dict(
    stages=[("env", "Leaderboard", "benchmark score", "public cohorts", "fixtures/fixtures.json"),
            ("env", "Replays", "tool-attack trajectories", "recorded", "fixtures/fixtures.json"),
            ("defender", "Rank both", "ρ (Spearman)", "rank agreement", "student/transfer.py"),
            ("defender", "Cross-tab", "top/bottom × pass/fail", "at a registered cut", "student/transfer.py")],
    flows=["scores", "block rates", "ranks"],
    output=("Transfer", "does the ranking hold?", "per detector family"),
    scopes=[(2, 3, "analysis")],
    adversary=[(1, "indirect injection")],
    cap1="A benchmark ranking is useful only if it survives on the attacks the deployment faces.",
    adds=["many public detectors from five evaluation cohorts", "threshold collapse across corpora"])

S["83"] = dict(
    stages=[("env", "Registry snapshots", "t₁, t₂", "complete, dated", "fixtures/fixtures.json"),
            ("defender", "Description scan", "marker lexicon", "override, exfiltration, privilege", "student/census.py"),
            ("defender", "Auth metadata", "remote ∧ ¬auth", "authorisation gap", "student/census.py"),
            ("defender", "Name confusion", "edit distance ≤ 1", "look-alike names", "student/census.py")],
    flows=["manifests", "markers", "gaps"],
    output=("Census", "flagged per snapshot", "and change between snapshots"),
    scopes=[(1, 3, "static census")],
    adversary=[(0, "poisoned description")],
    cap1="The manifest description is the only text a client sees before connecting, so it is scanned at registry scale.",
    adds=["the complete official registry at two dates", "tool descriptions from a catalogue", "deployed-agent checks"])

S["84"] = dict(
    stages=[("env", "Releases", "tags per framework", "multi-release history", "fixtures/fixtures.json"),
            ("defender", "Sink census", "shell, eval, net, write", "per release", "student/drift.py"),
            ("defender", "Transitions", "Δ per class", "release to release", "student/drift.py"),
            ("defender", "Review rule", "new shell ∨ eval ⇒ review", "and elasticity to code", "student/drift.py")],
    flows=["code", "counts", "Δ"],
    output=("Drift graph", "flagged transitions", "per framework"),
    scopes=[(1, 3, "longitudinal census")],
    adversary=None,
    cap1="A release-by-release census of privileged sinks tells an engineer which upgrades need review.",
    adds=["many tags across frameworks and package releases", "wild cluster bootstrap for elasticity", "a pre-registered outcome linkage"])

S["85"] = dict(
    stages=[("env", "Frameworks", "pinned", "native and with a monitor", "fixtures/fixtures.json"),
            ("defender", "Probe", "labelled value → sink", "per sink class", "student/matrix.py"),
            ("defender", "Matrix", "enforced | documented | absent", "framework × sink × mode", "student/matrix.py"),
            ("agent", "Through the model", "verbatim | paraphrase | split", "does the label survive?", "student/matrix.py")],
    flows=["probes", "outcomes", "cells"],
    output=("Enforcement", "cells enforced · labels kept", "documentation is not enforcement"),
    scopes=[(1, 2, "sink-side mediation")],
    adversary=[(3, "paraphrased value")],
    cap1="A provenance label protects a sink only if it is enforced there and survives the language model.",
    adds=["SHA-pinned open-source frameworks", "live episodes with hosted models", "label recall and precision against benchmark ground truth"])

S["86"] = dict(
    stages=[("env", "Trajectories", "tool-call arguments", "pinned corpora", "fixtures/fixtures.json"),
            ("defender", "Shape lexicon", "five closed families", "email, phone, IP, key, path user", "student/pii.py"),
            ("defender", "Classify", "per argument", "per tool class", "student/pii.py"),
            ("defender", "Audit", "tp / fp per family", "a version string is not an address", "student/pii.py")],
    flows=["arguments", "patterns", "matches"],
    output=("Census", "shapes per tool class and sink", "deterministic, zero-GPU"),
    scopes=[(1, 3, "closed lexicon")],
    adversary=None,
    cap1="Personal-data shapes in recorded tool arguments are counted with a closed lexicon whose errors can be audited.",
    adds=["several pinned trajectory corpora", "per-sink breakdowns and a registered lexicon"])

S["87"] = dict(
    stages=[("env", "Skill bundle", "declaration + handler", "marketplace listing", "fixtures/fixtures.json"),
            ("defender", "Static extraction", "patterns over source", "what the code can do", "student/diff.py"),
            ("defender", "Hidden", "extracted ∖ declared", "understatement", "student/diff.py"),
            ("defender", "Unused", "declared ∖ extracted", "overstatement", "student/diff.py")],
    flows=["source", "capabilities", "diff"],
    output=("Supply chain", "both directions per skill", "zero-LLM audit"),
    scopes=[(1, 3, "static audit")],
    adversary=[(0, "undeclared shell call")],
    cap1="A skill's declaration is compared with what its handler can actually do, in both directions.",
    adds=["marketplace listings and public repositories", "Wilson intervals and exact tests"])

S["88"] = dict(
    stages=[("env", "Trajectory", "steps, candidate call", "labelled injected or not", "fixtures/fixtures.json"),
            ("defender", "Provenance taint", "args ∩ untrusted output", "", "student/confusion.py"),
            ("defender", "Task mismatch", "tool ∉ task tools", "", "student/confusion.py"),
            ("defender", "Recency", "last step untrusted", "", "student/confusion.py")],
    flows=["call", "call", "call"],
    output=("Combine and score", "2-of-3 · union", "confusion matrix, TPR, FPR"),
    scopes=[(1, 3, "zero-GPU detectors (before execution)")],
    adversary=[(0, "injected tool output")],
    cap1="Three cheap structural cues each catch a different subset of injected actions; combining them trades sensitivity against false alarms.",
    adds=["attacked benchmark runs with byte-identical reproduction", "false-positive costs and cross-domain transfer"])

S["89"] = dict(
    stages=[("env", "Tool schema", "JSON Schema", "one declaration", "fixtures/fixtures.json"),
            ("env", "Boundary payloads", "coercion, null, extra key …", "adversarial arguments", "fixtures/fixtures.json"),
            ("defender", "Framework A", "lenient validator", "coerces and drops", "student/divergence.py"),
            ("defender", "Framework B", "strict validator", "exact types and keys", "student/divergence.py")],
    flows=["schema", "payload", "same payload"],
    output=("Divergence", "accept(A) ≠ accept(B)", "per schema-framework pair"),
    scopes=[(2, 3, "live differential probe")],
    adversary=[(1, "type-confused argument")],
    cap1="The same schema becomes a different gate in each framework; a differential probe shows where.",
    adds=["live probes across several frameworks", "a static interpretation analysis"])

S["90"] = dict(
    stages=[("agent", "Coding agent", "trajectory of actions", "maintenance task", "fixtures/fixtures.json"),
            ("defender", "Exposure", "file appears in observations", "e.g. in ls output", "student/acquisition.py"),
            ("defender", "Acquisition", "agent opened the file", "reads, not mentions", "student/acquisition.py"),
            ("defender", "Outcome", "resolved, within task", "task held fixed", "student/acquisition.py")],
    flows=["log", "visible", "opened"],
    output=("Context acquisition", "exposure–acquisition gap", "and its association with resolution"),
    scopes=[(1, 3, "measurement instrument")],
    adversary=None,
    cap1="Guidance a repository writes for agents is visible far more often than it is read.",
    adds=["public trajectory corpora across many harnesses", "task fixed effects and trajectory-length controls", "a push-policy comparison on the same tasks"])
