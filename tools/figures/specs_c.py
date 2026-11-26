"""Procedure specs, demos 46-65."""
S = {}

S["46"] = dict(
    stages=[("env", "Artefacts", "packages, model cards", "secondary records", "fixtures/"),
            ("agent", "Baseline space", "v = E₀(x)", "simulated embedding", "student/drift.py"),
            ("agent", "Swapped space", "v′ = E₁(x)", "rotation plus warp stands in for a new model", "student/drift.py"),
            ("defender", "Shift", "1 − cos(v, v′)", "and neighbour-set churn", "student/run_drift.py")],
    flows=["x", "v", "v′"],
    output=("Triage impact", "specificity before → after", "at a threshold set in the old space"),
    scopes=[(1, 2, "both spaces simulated")],
    adversary=None,
    cap1="Swapping the embedding model moves every vector at once; a threshold set in the old space no longer means the same thing.",
    adds=["malicious-package records and model cards as the artefact set", "a seeded rotation-plus-warp family", "neighbour churn and specificity at a calibrated threshold"])

S["47"] = dict(
    stages=[("agent", "Assessor", "guess g", "sees a clean export and a symptom card", "fixtures/"),
            ("defender", "Seal", "h = SHA-256(g)", "written before the key opens", "student/seal.py"),
            ("env", "Answer key", "k", "opened after the seal", "fixtures/"),
            ("defender", "Verify", "H(g) = h ∧ g = k", "an edited guess is a mismatch", "student/run_seal.py")],
    flows=["g", "h", "k"],
    output=("Verdict", "hit | miss | tampered", "falsifiable before reveal"),
    scopes=[(1, 3, "pre-reveal commitment")],
    adversary=[(0, "post-seal edit")],
    cap1="Sealing the guess before the key opens makes any later edit detectable.",
    adds=["a benchmark of planted defects with sealed ground truth", "command-line assessors run without access to the run identifier"])

S["48"] = dict(
    stages=[("env", "Integration", "requested scopes R", "from the consent request", "fixtures/"),
            ("defender", "Oracle", "required scopes Q(op)", "per operation and context, may abstain", "student/scopes.py"),
            ("defender", "Over-privilege", "R ∖ Q", "requested minus required", "student/scopes.py"),
            ("defender", "Least-privilege consent", "simulate R′ = Q", "what a minimal request would show", "student/run_scopes.py")],
    flows=["R", "Q", "R ∖ Q"],
    output=("Comparison", "by provider documentation regime", "result pending"),
    scopes=[(1, 3, "required-scope oracle")],
    adversary=None,
    cap1="Over-privilege is what an integration requests beyond what its operations require.",
    adds=["integrations across four identity providers", "a context-sensitive oracle with explicit abstention", "registered amendments; confirmatory corpus not yet frozen"])

S["49"] = dict(
    stages=[("agent", "Orchestrator", "task, plan", "running on tier A", "fixtures/"),
            ("infra", "Fallback", "tier A → tier B", "quota, rate limit or cost ceiling", "fixtures/"),
            ("defender", "Monitor", "d(policy, action)", "never depends on the tier (R1)", "student/tier_invariance"),
            ("defender", "Re-validate", "steps proposed before switch", "fail closed (R2); every action mediated (R3)", "student/run_tiers.py")],
    flows=["plan", "switch event", "decision"],
    output=("Invariance", "violations R0–R3", "per trace"),
    scopes=[(2, 3, "orchestration boundary")],
    adversary=[(1, "weaker fallback tier")],
    cap1="Authority must not change when the model serving a task changes mid-way.",
    adds=["tier independence, re-validation and complete mediation stated as properties", "a fail-closed monitor costed for a fixed budget"])

S["50"] = dict(
    stages=[("infra", "Root principal", "budget B", "the only source of spend", "fixtures/"),
            ("agent", "Delegate", "grant g ≤ remaining", "attenuating capability", "student/delegation_budget"),
            ("defender", "Ledger", "invariants B1–B5", "conservation along every chain", "student/delegation_budget"),
            ("defender", "Conditions", "C0 … C3", "defaults, fixed, attenuated, partial", "student/run_budget.py")],
    flows=["B", "spend", "ledger"],
    output=("Overrun and work", "overrun rate · completed work", "per condition"),
    scopes=[(1, 2, "delegation tree")],
    adversary=[(1, "runaway sub-agent")],
    cap1="If budgets travel as attenuating capabilities, no chain can spend more than its root.",
    adds=["seeded synthetic delegation trees across workload regimes", "bootstrap intervals for overrun rates", "a second stage on real pipelines"])

S["51"] = dict(
    stages=[("env", "Benign text", "standard form", "written English", "fixtures/"),
            ("env", "Surface variants", "transcript, typo, telegraphic", "same meaning, different form", "fixtures/"),
            ("defender", "Guardrail", "block ⇔ s ≥ τ", "input classifier", "student/guardrail_equity"),
            ("defender", "Disparity", "FPR(variant) − FPR(standard)", "and a variant-agnostic mitigation", "student/run_equity.py")],
    flows=["x", "x′", "verdicts"],
    output=("Equity", "false-positive disparity", "before and after mitigation"),
    scopes=[(2, 3, "admission control")],
    adversary=None,
    cap1="Benign text in a different surface form can be refused more often by the same guardrail.",
    adds=["open-weight classifiers on systematic surface-form shifts", "a deterministic offline measurement", "a mitigation that does not need to know the variant"])

S["52"] = dict(
    stages=[("agent", "Simulator", "LLM plays learners", "cohort model", "fixtures/"),
            ("env", "Fault injection", "seven fault classes", "contamination … silent substitution", "fixtures/"),
            ("defender", "Battery", "six registered tests", "held-out years, probes", "student/sim_validate.py"),
            ("defender", "Coverage", "detected / injected", "and false alarms", "student/run_sim.py")],
    flows=["outputs", "faulted outputs", "verdicts"],
    output=("Dependability", "calibrated ≠ validated", "per detector"),
    scopes=[(2, 3, "pass criteria registered first")],
    adversary=[(1, "recited published labels")],
    cap1="A simulator can match last year's rates for the wrong reason; injected faults test whether the checks would notice.",
    adds=["a seven-class fault model", "detectors measured on a non-LLM cohort model and on stored LLM outputs"])

S["53"] = dict(
    stages=[("agent", "Pipeline outputs", "labels, code, results", "too many to check", "fixtures/"),
            ("defender", "Sample", "seeded, stratified", "which items a human checks", "student/validate.py"),
            ("defender", "Plant errors", "known defects", "tests the checker itself", "student/validate.py"),
            ("defender", "Estimate", "error rate of the rest", "design-based", "student/run_validate.py")],
    flows=["items", "sample", "checked"],
    output=("Claim", "error rate ± interval", "for the unchecked outputs"),
    scopes=[(1, 3, "validation protocol (masked provenance)")],
    adversary=None,
    cap1="Planted errors measure the validator; sampling measures the pipeline.",
    adds=["double validation and provenance masking", "model-assisted and active-inference estimators", "a tested protocol on real agent outputs"])

S["54"] = dict(
    stages=[("env", "Scenarios", "attack and benign", "tutoring sessions", "fixtures/"),
            ("agent", "Simulated test", "scores in simulation", "the stress test", "student/transfer.py"),
            ("agent", "Direct test", "scores on the system", "the same scenarios", "student/transfer.py"),
            ("defender", "Transfer", "recall(sim) vs recall(direct)", "at one threshold", "student/run_transfer.py")],
    flows=["scenario", "s_sim", "s_direct"],
    output=("Agreement", "does simulation predict?", "result pending"),
    scopes=[(1, 2, "same scenarios, two settings")],
    adversary=[(0, "shifted attack")],
    cap1="A stress test passed in simulation is evidence only if its result transfers to the direct test.",
    adds=["agentic tutoring systems under both settings", "model-identity logging and a scenario schema", "design stage"])

S["55"] = dict(
    stages=[("env", "Learners", "randomised", "two arms", "fixtures/"),
            ("agent", "Arm", "direct answers | scaffolding", "the intervention", "fixtures/"),
            ("defender", "Immediate test", "Δ_now", "scaffold present", "student/power.py"),
            ("defender", "Delayed test", "Δ_later", "scaffold removed", "student/run_power.py")],
    flows=["n per arm", "outcomes", "outcomes"],
    output=("Power", "for Δ_now vs Δ_later", "which difference the study claims"),
    scopes=[(2, 3, "two waves")],
    adversary=None,
    cap1="Power depends on which difference the study claims; the residual difference is usually much smaller.",
    adds=["a two-wave experiment with adult distance learners", "cognitive load and error detection as secondary outcomes", "design stage"])

S["56"] = dict(
    stages=[("env", "Studies", "yᵢ, vᵢ", "assisted, unassisted, delayed", "fixtures/"),
            ("defender", "Weights", "wᵢ = 1 / vᵢ", "precise rows count more", "student/learning_meta.py"),
            ("defender", "Pool", "ȳ = Σwᵢyᵢ / Σwᵢ", "fixed effect", "student/learning_meta.py"),
            ("defender", "Heterogeneity", "Cochran Q", "do studies agree?", "student/run_meta.py")],
    flows=["rows", "w", "ȳ"],
    output=("Summary", "performance vs learning", "separated by outcome timing"),
    scopes=[(1, 3, "meta-analysis")],
    adversary=None,
    cap1="A meta-analysis weights each study by its precision rather than averaging headlines.",
    adds=["a systematic search and registered protocol", "experiments that separate assisted, unassisted and delayed outcomes", "design stage"])

S["57"] = dict(
    stages=[("env", "Policy documents", "excerpts", "a longitudinal frame", "fixtures/"),
            ("defender", "Codebook", "absent … enforced", "four ordered levels", "student/coding.py"),
            ("defender", "Two raters", "codes A, B", "independent", "student/coding.py"),
            ("defender", "Agreement", "percent, Cohen's κ", "chance-corrected", "student/run_coding.py")],
    flows=["text", "levels", "codes"],
    output=("Usable codebook?", "κ against a floor", "before the corpus is coded"),
    scopes=[(1, 3, "codebook validation")],
    adversary=None,
    cap1="A corpus is only as usable as its codebook; chance-corrected agreement tests the codebook first.",
    adds=["a population frame of institutions", "web-archive captures over time", "design stage"])

S["58"] = dict(
    stages=[("env", "Occupations", "tasks per role", "public task files", "fixtures/"),
            ("env", "Exposure labels", "per task", "published human labels", "fixtures/"),
            ("defender", "Join", "task ↔ label", "match rate reported", "student/exposure.py"),
            ("defender", "Aggregate", "role and family means", "teaching, support …", "student/run_exposure.py")],
    flows=["tasks", "labels", "matched"],
    output=("Exposure", "per family", "exposure is not displacement"),
    scopes=[(2, 3, "descriptive")],
    adversary=None,
    cap1="Exposure scores summarise overlap between tasks and what models can do; they do not measure displacement.",
    adds=["occupation and task files joined to public exposure labels", "six educational role families with Wilson intervals"])

S["59"] = dict(
    stages=[("env", "Briefing", "dated, hashed", "capability evidence", "fixtures/"),
            ("agent", "Panel round", "ratings rᵢ", "each stored with the briefing hash", "student/delphi.py"),
            ("defender", "Summarise", "median, IQR", "per proposition", "student/delphi.py"),
            ("defender", "Consensus rule", "IQR ≤ 1.5", "fixed before the round", "student/run_delphi.py")],
    flows=["h(briefing)", "ratings", "IQR"],
    output=("Foresight", "consensus | split", "at 5, 10 and 15 years"),
    scopes=[(1, 3, "provenance-labelled round")],
    adversary=None,
    cap1="Every rating is bound to the briefing it answered, so later rounds can be compared fairly.",
    adds=["a Delphi panel and experiential scenarios", "ethics approval and recruitment pending"])

S["60"] = dict(
    stages=[("env", "Task battery", "inputs, reference", "reference written before any run", "fixtures/"),
            ("agent", "Agent", "answer a", "analysis task", "student/battery.py"),
            ("defender", "Acceptance", "|a − ref| ≤ tol", "criteria fixed in advance", "student/battery.py"),
            ("defender", "Score", "pass per task", "and per workflow family", "student/run_battery.py")],
    flows=["task", "a", "pass"],
    output=("Battery result", "pass rate", "per family"),
    scopes=[(2, 3, "predeclared references")],
    adversary=None,
    cap1="An analysis battery is fair only if every reference answer was written before any model ran.",
    adds=["about forty engineering-biology tasks", "domain-scientist acceptance criteria"])

S["61"] = dict(
    stages=[("agent", "Agent analysis", "steps s₁ … sₙ, report", "scripts and a prose summary", "fixtures/fixtures.json"),
            ("defender", "Re-execute", "run steps in a clean copy", "do they finish?", "student/reexec.py"),
            ("defender", "Number provenance", "report number ∈ outputs?", "every number traced", "student/reexec.py"),
            ("defender", "Reference", "answer vs reference", "right, and for the right reason?", "student/reexec.py")],
    flows=["steps", "outputs", "traced"],
    output=("Machine verdict", "runs · traced · correct", "before a person reads it"),
    scopes=[(1, 3, "machine checks")],
    adversary=None,
    cap1="Before anyone reads an agent-written analysis, a machine can re-run it and trace every number in the report.",
    adds=["public engineering-biology tasks run by open-weight configurations, five times each", "deterministic, zero-GPU checks"])

S["62"] = dict(
    stages=[("env", "Learner record", "profile, history", "public learner data", "fixtures/fixtures.json"),
            ("agent", "LLM policy", "weekly decision", "active, engagement, submit, withdraw", "student/policy_checks.py"),
            ("defender", "Schema check", "valid fields?", "adherence", "student/policy_checks.py"),
            ("defender", "Calibration", "Brier vs baselines", "and persona sensitivity", "student/policy_checks.py")],
    flows=["inputs", "JSON", "valid"],
    output=("Policy quality", "adherence · calibration · sensitivity", "against non-LLM baselines"),
    scopes=[(2, 3, "checks")],
    adversary=None,
    cap1="An LLM learner policy is compared with simple baselines on adherence, calibration and sensitivity to persona wording.",
    adds=["presentations of a public learner dataset", "free models on a cloud machine", "design stage"])

S["63"] = dict(
    stages=[("env", "Policies", "wave 1, wave 2", "archived and live versions", "fixtures/fixtures.json"),
            ("agent", "Model A, model B", "codes per dimension", "two model families", "fixtures/fixtures.json"),
            ("defender", "Agreement", "Krippendorff α", "per dimension", "student/reliability.py"),
            ("defender", "Stability", "same text, same code?", "across waves", "student/reliability.py")],
    flows=["text", "codes", "α"],
    output=("Reliability", "α per dimension", "and code drift on unchanged text"),
    scopes=[(2, 3, "reliability analysis")],
    adversary=None,
    cap1="Two model families coding the same policies agree on some dimensions and not others.",
    adds=["an eleven-dimension codebook on a random sample of institutions", "a web-archive wave and a live wave"])

S["64"] = dict(
    stages=[("env", "Scripted dialogues", "learner demands", "repeated requests for the answer", "fixtures/fixtures.json"),
            ("agent", "Assistant", "reply r", "direct or Socratic", "fixtures/fixtures.json"),
            ("defender", "Answer guard", "leak score(r, key) ≥ τ", "checked before the reply is sent", "student/guard.py"),
            ("defender", "Calibrate", "leaks vs blocked hints", "sweep τ", "student/guard.py")],
    flows=["turn", "r", "score"],
    output=("Operating point", "leak rate · over-blocking", "at the chosen τ"),
    scopes=[(2, 3, "guard")],
    adversary=[(0, "adversarial learner")],
    cap1="An answer guard trades answers it lets through against helpful hints it blocks.",
    adds=["forty scripted dialogues over ten problem parts and four learner scripts", "two assistant conditions"])

S["65"] = dict(
    stages=[("env", "Bibliographic pool", "UK works 2023–2026", "retrieved under a registered protocol", "fixtures/fixtures.json"),
            ("agent", "Screen", "model A labels", "set S (security) or E (education)", "fixtures/fixtures.json"),
            ("defender", "Check", "model B on a sample", "agreement", "student/bibliometrics.py"),
            ("defender", "Co-authorship", "authors(S) ∩ authors(E)", "bridge works", "student/bibliometrics.py")],
    flows=["works", "labels", "sets"],
    output=("Do they work together?", "shared authors · bridge works", "a registered screen"),
    scopes=[(2, 3, "screen and analysis")],
    adversary=None,
    cap1="Two research communities are tested for collaboration by the authors and works they share.",
    adds=["a registered retrieval from an open bibliographic index", "a second model of another family on a stratified sample"])
