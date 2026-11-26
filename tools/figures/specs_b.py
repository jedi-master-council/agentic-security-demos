"""Procedure specs, demos 21-45."""
S = {}

S["21"] = dict(
    stages=[("env", "Registry walk", "version records", "every server, every version, dated", "fixtures/registry_hosting.json"),
            ("defender", "Hosting", "host share, platform suffix", "where the tool layer runs", "student/registry_hosting.py"),
            ("defender", "Cadence", "gap between versions", "how fast it changes", "student/registry_hosting.py"),
            ("defender", "Endpoint change", "URL Δ under bump type", "patch, minor or major", "student/registry_hosting.py")],
    flows=["records", "latest", "transitions"],
    output=("Measurement", "concentration · cadence · drift", "plus secret-header requirements"),
    scopes=[(1, 3, "descriptive census")],
    adversary=[(3, "endpoint moved silently")],
    cap1="A dated registry walk shows where agent tool servers are hosted and how their endpoints change between versions.",
    adds=["the complete official registry walk on a fixed date", "intervals for every share", "description poisoning and capability tallies (the toy's first part)"],
    new="`student/registry_hosting.py` (hosting concentration, version cadence and endpoint changes in a registry walk).")

S["22"] = dict(
    stages=[("agent", "Agent session", "writes, reads", "memory layer of a framework", "fixtures/"),
            ("defender", "Flow tuple", "⟨s, r, j, τ, φ⟩", "scored against context norms", "student/memory.py"),
            ("defender", "Resurfacing", "item in a later session?", "across sessions and users", "student/memory.py"),
            ("defender", "Erasure audit", "bytes after delete", "vector, key-value, cache, disk", "student/run_memory.py")],
    flows=["events", "violations", "deleted ids"],
    output=("Three regimes", "violation · resurfacing · residue", "per framework"),
    scopes=[(1, 3, "instrumented harness")],
    adversary=None,
    cap1="Contextual integrity is measured as flows; erasure is measured as bytes that remain after a delete.",
    adds=["three pinned production memory frameworks", "privacy vignettes interleaved with a large benign filler corpus", "storage-level audits of every persistence layer"])

S["23"] = dict(
    stages=[("agent", "Agent loop", "framework + model", "a task that uses tools", "fixtures/"),
            ("env", "Fault proxy", "fault ∈ six types", "transport or payload faults injected", "student/faults.py"),
            ("defender", "Oracle", "graceful | cascade | silent-wrong", "compares the answer with ground truth", "student/run_faults.py"),
            ("defender", "Static audit", "broad except handlers", "do handlers swallow errors?", "student/faults.py")],
    flows=["tool call", "faulted result", "outcome"],
    output=("Fault handling", "silent-wrong rate by fault class", "against a registered margin"),
    scopes=[(1, 2, "pre-registered campaign")],
    adversary=[(1, "duplicated or truncated record")],
    cap1="Payload faults that look like valid data produce silent wrong answers more often than transport faults that raise errors.",
    adds=["a pre-registered campaign over several frameworks and local models", "a blinded check of the oracle", "a static census of exception handlers across many frameworks"])

S["24"] = dict(
    stages=[("env", "Protocol model", "roles, messages", "authorisation profile and delegation", "fixtures/"),
            ("defender", "Properties", "audience ∧ scope ⊑", "same audience; scope never grows", "student/authz.py"),
            ("defender", "Check each chain", "hop by hop", "user → agent → agent → tool", "student/run_authz.py"),
            ("defender", "Counter-example", "violating trace", "the chain that breaks a property", "student/run_authz.py")],
    flows=["model", "lemmas", "traces"],
    output=("Verdict", "holds | attack trace", "per property"),
    scopes=[(1, 3, "formal analysis")],
    adversary=[(0, "confused audience")],
    cap1="Delegation is safe only if every hop names the same audience and no hop widens the scope.",
    adds=["a symbolic model checked in a protocol prover", "agent-to-agent delegation modelled beside the authorisation profile", "design stage: lemmas and traces still pending"])

S["25"] = dict(
    stages=[("env", "Registry", "servers → packages", "names declared by each server", "fixtures/"),
            ("env", "Attestation state", "signed build provenance?", "registry-reported per release", "fixtures/"),
            ("defender", "Install check", "fail-closed | fail-open", "block or warn when unattested", "student/verifier.py"),
            ("defender", "Advisory join", "malicious-package list", "what the check would catch", "student/run_verify.py")],
    flows=["names", "state", "decisions"],
    output=("Cost and catch", "blocked share · caught share", "remote-only servers offer nothing to check"),
    scopes=[(2, 3, "install-time gate")],
    adversary=[(0, "malicious package")],
    cap1="A fail-closed provenance check blocks every unattested package; its cost is what it blocks and its value is what it catches.",
    adds=["the official registry joined to attestation state for all declared names", "coverage by release count", "cluster bootstrap intervals"])

S["26"] = dict(
    stages=[("env", "Framework", "executor code, docs", "pinned repositories", "fixtures/"),
            ("defender", "Default config", "egress · metadata · user", "what isolation is on by default", "student/sandbox.py"),
            ("defender", "Probes", "escape attempts", "file system, network, credentials", "student/run_sandbox.py"),
            ("defender", "Advisories", "isolation CVEs", "classified by component", "student/sandbox.py")],
    flows=["executors", "config", "escapes"],
    output=("Isolation score", "escape rate per config", "claims against configuration"),
    scopes=[(1, 3, "audit")],
    adversary=[(2, "prompt-injected code")],
    cap1="Isolation claims are checked against the configuration that actually ships and against escape probes.",
    adds=["executor files mined across pinned framework repositories", "advisories classified across the stack", "container paths coded for user, capabilities and mounts"])

S["27"] = dict(
    stages=[("env", "Workflow file", "trigger, gate, perms", "stored syntax only", "fixtures/"),
            ("defender", "Trigger", "outsider can start it?", "issue, comment, pull request", "student/scanner.py"),
            ("defender", "Identity gate", "author check present?", "who may start the run", "student/scanner.py"),
            ("defender", "Permissions", "write declared?", "authority of the run", "student/run_scan.py")],
    flows=["file", "public", "ungated"],
    output=("Exposure", "public ∧ ungated ∧ write", "per repository, a lower bound"),
    scopes=[(1, 3, "static rules")],
    adversary=[(0, "issue text from any account")],
    cap1="An agent job is exposed when an outside account can start it, nothing gates the author, and the run can write.",
    adds=["a stored pilot pack of repositories found by code search", "conservative and permissive rules side by side", "every count stated as a lower bound for the search space"])

S["28"] = dict(
    stages=[("env", "Memory store", "entries e", "opened through an adapter", "fixtures/"),
            ("defender", "Origin recorded?", "hash(e), source", "does the store keep provenance?", "student/memascope.py"),
            ("defender", "Instruction-likeness", "rules + classifier", "scored per entry, never edited", "student/memascope.py"),
            ("defender", "Canary", "write → later retrieve", "through the framework's own paths, on a copy", "student/run_memascope.py")],
    flows=["entries", "origins", "scores"],
    output=("Audit report", "flagged entries · persistence", "read-only: no edit, no delete"),
    scopes=[(1, 3, "auditor (read-only)")],
    adversary=[(0, "poisoned write")],
    cap1="A memory auditor reports origin, instruction-likeness and persistence without changing the store.",
    adds=["adapters for real framework stores", "an open-weight classifier run locally", "a benign canary planted into a copy of the store"])

S["29"] = dict(
    stages=[("agent", "Agent logs", "turns, tool calls", "four public formats", "fixtures/"),
            ("defender", "Completeness", "name, args, id, input", "is each turn structurally complete?", "student/provenance.py"),
            ("defender", "Attribution", "action → cause", "rare-token rule against recency", "student/provenance.py"),
            ("defender", "Integrity", "hash chain", "has the log been altered?", "student/run_prov.py")],
    flows=["turns", "complete turns", "chain"],
    output=("Attribution", "attributable / actions", "against a registered floor"),
    scopes=[(1, 3, "post-incident reconstruction")],
    adversary=[(0, "injected input")],
    cap1="Attribution after an incident needs each action to point back to the input that caused it.",
    adds=["four public trajectory formats", "post-injection actions from successful injection runs", "a registered accuracy floor"])

S["30"] = dict(
    stages=[("env", "Deployment artefact", "compose, helm, config", "copied by operators", "fixtures/"),
            ("defender", "Codebook", "flag rules", "bind, auth, privilege, versions", "student/checker.py"),
            ("defender", "Composites", "exposure · privilege", "security-bearing combinations", "student/checker.py"),
            ("defender", "Drift", "pinned version vulnerable?", "advisories at the snapshot", "student/run_defaults.py")],
    flows=["files", "flags", "composite"],
    output=("Insecure by default", "flagged share", "Wilson and repository bootstrap intervals"),
    scopes=[(1, 3, "codebook (versioned)")],
    adversary=None,
    cap1="Defaults in shipped configuration become the operator's posture; a codebook makes them countable.",
    adds=["deduplicated configurations across several serving stacks", "a versioned codebook and snapshot date", "repository-level bootstrap"])

S["31"] = dict(
    stages=[("env", "Read the listing", "registry entry", "no field for scopes; names in descriptions", "fixtures/"),
            ("env", "Read credentials", "what the user supplies", "tokens and keys requested", "fixtures/"),
            ("env", "Read run-time metadata", "authorisation hints", "protocol metadata", "fixtures/"),
            ("defender", "Read code and docs", "scopes exercised", "published source", "student/declarations.py")],
    flows=["declared", "requested", "advertised"],
    output=("Declaration gap", "declared ⊋ exercised", "where authority is reviewable"),
    scopes=[(0, 3, "four places authority could be declared")],
    adversary=None,
    cap1="Authority is reviewable only where it is declared; the four places are compared per integration.",
    adds=["every latest version in the official registry", "provider scope catalogues for four identity providers", "strict and lenient matching rules"])

S["32"] = dict(
    stages=[("env", "Literature", "attacks, defences, evals", "search, screen, include", "fixtures/"),
            ("defender", "Classify", "channel × layer", "content, tool, memory, multi-agent", "student/audit.py"),
            ("defender", "Artefact check", "code ∧ data?", "is anything released?", "student/audit.py"),
            ("defender", "Re-run", "reproduces?", "within a tolerance", "student/run_audit.py")],
    flows=["papers", "classes", "artefacts"],
    output=("Reproducibility", "reproduces / released", "per channel"),
    scopes=[(1, 3, "audit protocol")],
    adversary=None,
    cap1="A systematisation counts what was published and then what can still be run.",
    adds=["a registered search and screening protocol", "artefact re-execution under a time budget", "design stage"])

S["33"] = dict(
    stages=[("env", "Specifications", "pinned revisions", "normative statements", "fixtures/"),
            ("defender", "Elements", "discovery … streaming", "six protocol elements", "student/coverage.py"),
            ("defender", "Map", "attack × mitigation", "stated normatively or left open", "student/coverage.py"),
            ("defender", "Composition", "per hop ⇏ end to end", "delegation across protocols", "student/run_coverage.py")],
    flows=["text", "elements", "cells"],
    output=("Coverage gap", "known attack ∧ no mitigation", "per element"),
    scopes=[(1, 3, "systematisation")],
    adversary=[(3, "cross-protocol delegation")],
    cap1="Per-hop guarantees stated by each protocol do not compose into an end-to-end guarantee.",
    adds=["pinned specification revisions and their OAuth foundations", "normative text coded per element", "the compositional reading challenged"])

S["34"] = dict(
    stages=[("env", "Corpora", "three secondary sets", "unified under one schema", "fixtures/"),
            ("env", "Screen", "pixels with text", "typographic or embedded-interface", "fixtures/"),
            ("agent", "VLM agent", "reads and acts", "acts on what it reads", "student/visual.py"),
            ("defender", "Policy", "region trust", "untrusted region ⇏ instruction", "student/run_visual.py")],
    flows=["records", "image", "action"],
    output=("Benchmark", "attack success · benign acted", "plus a registered attention hypothesis"),
    scopes=[(3, 4, "defence")],
    adversary=[(1, "typographic instruction")],
    cap1="Text rendered in pixels reaches a vision-language agent as an instruction unless the region is treated as untrusted.",
    adds=["a registered benchmark from three corpora with a seeded split", "an attention-capture hypothesis per layer and head", "falsification criteria fixed in advance"])

S["35"] = dict(
    stages=[("env", "Published results", "rate, model, suite", "extracted rows", "fixtures/"),
            ("defender", "Moderators", "size, date, regime", "coded per row", "student/meta.py"),
            ("defender", "Meta-regression", "y ~ size + suite", "suite as a fixed effect", "student/meta.py"),
            ("defender", "Compare", "with and without suite", "does size survive?", "student/run_meta.py")],
    flows=["rows", "codes", "fit"],
    output=("Scaling claim", "slope(size | suite)", "design stage"),
    scopes=[(1, 3, "analysis")],
    adversary=None,
    cap1="A size trend across benchmarks can be the benchmark mix; holding the suite fixed tests it.",
    adds=["published agent-safety and injection results extracted under a protocol", "release date and training regime as moderators", "design stage"])

S["36"] = dict(
    stages=[("env", "Registry", "model cards, downloads", "and derivation edges", "fixtures/"),
            ("defender", "Code disclosure", "safety section?", "per card", "student/cards.py"),
            ("defender", "Weight", "binned tiers | per card", "registered estimator against descriptive", "student/cards.py"),
            ("defender", "Registered test", "gap ≥ +15 pp?", "falsified below +10 pp", "student/run_cards.py")],
    flows=["cards", "codes", "estimates"],
    output=("Verdict", "confirmed | falsified", "on the registered estimator"),
    scopes=[(2, 3, "registered after data access")],
    adversary=None,
    cap1="Whether popular models disclose more is decided on the registered estimator; a different weighting can say otherwise.",
    adds=["a census of model cards and derivation edges", "a fixed-weight blend of download-tier rates", "the descriptive per-card estimate reported beside it"])

S["37"] = dict(
    stages=[("env", "Public text", "prompts, labels", "direct-prompt corpora", "fixtures/"),
            ("env", "Benign pool", "constructed negatives", "defines the false-positive budget", "fixtures/"),
            ("defender", "Guard", "s(x) ≥ τ", "open classifier", "student/detectors.py"),
            ("defender", "Matched threshold", "τ : FPR = 1%", "recall read at a fixed budget", "student/run_cost.py")],
    flows=["x", "negatives", "τ"],
    output=("Report", "recall @ FPR", "with the template's required fields"),
    scopes=[(2, 3, "evaluation")],
    adversary=[(0, "injection")],
    cap1="A recall figure means little until the false-positive budget behind it is stated.",
    adds=["two open guards on public text", "bootstrap intervals for matched-threshold recall", "partly registered, partly post hoc, stated as such"])

S["38"] = dict(
    stages=[("env", "System cards", "developer documents", "retrieved on a fixed date", "fixtures/"),
            ("env", "Obligations", "articles, code, framework", "the regulatory expectation", "fixtures/"),
            ("defender", "Two coders", "covered | vague | absent", "agreement against a floor", "student/claims.py"),
            ("defender", "Tabulate", "obligation × developer", "coverage", "student/run_claims.py")],
    flows=["cards", "checklist", "codes"],
    output=("Assurance evidence", "covered share", "per obligation"),
    scopes=[(2, 3, "content analysis")],
    adversary=None,
    cap1="Each assurance claim in a system card is coded against a named obligation.",
    adds=["cards from four developers across several years", "a kappa floor fixed before coding", "retrieval paths documented"])

S["39"] = dict(
    stages=[("env", "Incident records", "frozen, hashed", "two public databases", "fixtures/"),
            ("defender", "Screen", "inclusion rule", "AI systems acting in real settings", "student/taxonomy.py"),
            ("defender", "Double-code", "pattern ∈ ten", "two coders, kappa gate", "student/taxonomy.py"),
            ("defender", "Map", "pattern → technique", "known adversary techniques", "student/run_tax.py")],
    flows=["records", "incidents", "patterns"],
    output=("Taxonomy", "prevalence · unmapped gap", "for practitioners"),
    scopes=[(1, 3, "pre-registered coding")],
    adversary=None,
    cap1="Incident sketches become counts by pattern, and the patterns no technique catalogue covers are the gap.",
    adds=["hundreds of frozen, hash-verified records", "rule-based lexicon coders against a registered gate", "a second, rules-free mapping"])

S["40"] = dict(
    stages=[("env", "Source packs", "files + licences", "many public benchmarks", "fixtures/"),
            ("defender", "Licence screen", "redistributable?", "excluded sources listed with reasons", "student/corpus.py"),
            ("defender", "Map to schema", "one record format", "with a provenance manifest", "student/corpus.py"),
            ("defender", "Deduplicate", "SHA-256", "cross-source duplicates", "student/run_corpus.py")],
    flows=["files", "admitted", "records"],
    output=("Compilation", "records · manifest", "every file traced to its source"),
    scopes=[(1, 3, "release pipeline")],
    adversary=None,
    cap1="A shared corpus answers two questions before release: what is duplicated, and what may be redistributed.",
    adds=["many source packs screened against upstream licences", "a provenance manifest per source file", "a data descriptor format"])

S["41"] = dict(
    stages=[("env", "Programme evidence", "studies, demos", "what each one measured", "fixtures/"),
            ("defender", "Invariant", "property I", "stated testably", "student/invariants.py"),
            ("defender", "Check", "holds | violated", "per system", "student/invariants.py"),
            ("defender", "Evidence link", "I → study", "why the invariant earns its place", "student/run_inv.py")],
    flows=["findings", "I", "verdicts"],
    output=("Checklist", "ten invariants", "with the evidence behind each"),
    scopes=[(1, 3, "synthesis")],
    adversary=None,
    cap1="A checklist turns scattered findings into testable properties, each tied to the evidence that motivates it.",
    adds=["a synthesis across the programme's studies", "design stage: each invariant awaits its evidence"])

S["42"] = dict(
    stages=[("env", "Advisories", "OSV records", "pinned snapshot", "fixtures/"),
            ("defender", "Deduplicate", "package × vulnerability", "unique pairs", "student/lifecycle.py"),
            ("defender", "Latency", "disclosure → patch", "survival tail for the unpatched", "student/lifecycle.py"),
            ("defender", "Hygiene", "pinning, CI practice", "static census", "student/run_cycle.py")],
    flows=["records", "pairs", "intervals"],
    output=("Lifecycle", "median lag · tail", "with cluster bootstrap"),
    scopes=[(1, 3, "analysis")],
    adversary=[(0, "exploited in the wild")],
    cap1="Patch latency is a distribution with a tail, not a single number.",
    adds=["core packages across three ecosystems", "survival analysis for unpatched records", "a hygiene census of agent-framework repositories"])

S["43"] = dict(
    stages=[("env", "Tool catalogue", "input schemas", "a third-party catalogue", "fixtures/confirmation_gap.json"),
            ("defender", "Categorise", "state-altering?", "four vendor categories", "student/confirmation_gap.py"),
            ("defender", "Keyword check", "confirm · approve · consent", "a confirmation step in the schema?", "student/confirmation_gap.py"),
            ("defender", "Gap", "altering ∧ ¬confirm", "where oversight cannot be exercised", "student/confirmation_gap.py")],
    flows=["schemas", "altering", "flags"],
    output=("Enforcement gap", "share without confirmation", "terms expect oversight; schemas lack the hook"),
    scopes=[(1, 3, "schema analysis")],
    adversary=None,
    cap1="Oversight that platform terms expect can only be exercised if the tool's schema offers a confirmation step.",
    adds=["a large third-party catalogue of protocol tools", "runtime verification affordances beside the schema keywords", "terms coding (the toy's first part) as context"],
    new="`student/confirmation_gap.py` (state-altering tool schemas checked for a confirmation step).")

S["44"] = dict(
    stages=[("env", "Framework source", "pinned versions", "dispatch paths", "fixtures/"),
            ("defender", "Def-use pass", "tool-return → argument", "intra-procedural flows", "student/taint.py"),
            ("defender", "Guard rubric", "token in scope?", "provenance, capability, approval", "student/taint.py"),
            ("defender", "FlowGate", "fail-closed replay", "prices provenance enforcement", "student/run_taint.py")],
    flows=["code", "flows", "unguarded"],
    output=("Integrity", "unguarded sink sites", "per framework"),
    scopes=[(1, 3, "static audit + replay")],
    adversary=[(0, "tool output as authority")],
    cap1="A value that is data when a tool returns it becomes authority when it is copied into the next call.",
    adds=["ten pinned frameworks and four profiled by control contracts", "an offline replay shim that prices enforcement", "recorded dispatch cells"])

S["45"] = dict(
    stages=[("env", "Pool", "P items, D defects", "fixed before data", "fixtures/"),
            ("agent", "Method", "selects k", "budgeted localisation", "fixtures/"),
            ("defender", "Exact null", "TP ~ Hypergeom(P, D, k)", "recall, precision, F1 share it", "student/nulls.py"),
            ("defender", "Design limit", "min P for power", "before collecting data", "student/run_nulls.py")],
    flows=["P, D", "TP", "p-value"],
    output=("Claim", "significant | not", "chance level transfers; ratios do not"),
    scopes=[(2, 3, "closed form")],
    adversary=None,
    cap1="At a fixed budget, recall, precision and F1 rise with the same true-positive count, so one exact null serves all three.",
    adds=["blind threat models from several models", "real vulnerabilities in independent projects", "a proof that ratio-to-null statistics do not transfer"])
