<p align="center">
  <img src="https://raw.githubusercontent.com/jedi-master-council/agentic-security-demos/main/assets/logo.svg" alt="Agentic Security Demos Logo" width="200">
</p>

<h1 align="center">Agentic AI Security Demos</h1>
<p align="center">
  <strong>A curated collection of 79 reproducible teaching demonstrations for agentic AI security — 74 in this repository and five (61–65) in separate repositories — distilled from research targeting top-tier venues (SaTML, CCS, NeurIPS, IEEE SP, USENIX, NDSS, RAID, ASIACCS, ESORICS, ACSAC, ICML, ICLR, AAAI, IJCAI, ACL, ICSE, WWW, EuroS&P, PoPETs, DSN, CSF, ACNS, Black Hat, DEF CON, TIFS, TDSC, TOPS, CSUR, COMST, TPAMI, TMLR, Nature MI, Journal of Cybersecurity, IEEE S&P Magazine, Scientific Data, CACM, TSE, FAccT, Computers & Security, IEEE TAI, ACM TIST, Pattern Recognition, IEEE TNNLS, IEEE TKDE, JAIR, AIJ, AAAI, KDD). All scenarios, numbers and verdicts here are synthetic coursework — they describe no real publication.</strong>
</p>

> 🐣 **Padawan-practice notice (read before citing).** These are teaching demos for agentic AI security — training missions for the classroom, not Jedi trials. Like Padawan exercises, each demo **may or may not be converted into a full paper**, and any paper **may or may not be accepted** at its listed venue. The venue column names the *training ground* that inspired the exercise, never a publication claim. No preprints, no datasets deposited, no reviewer verdicts — just lightsabers set to stun (synthetic fixtures, offline only).

<p align="center">
  <a href="https://github.com/jedi-master-council/agentic-security-demos/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/jedi-master-council/agentic-security-demos/ci.yml?branch=main&label=Build&style=flat-square" alt="Build Status"></a>
  <a href="https://pypi.org/project/agentic-security-demos/"><img src="https://img.shields.io/pypi/v/agentic-security-demos?style=flat-square&label=PyPI" alt="PyPI Version"></a>
  <a href="https://pypi.org/project/agentic-security-demos/"><img src="https://img.shields.io/pypi/pyversions/agentic-security-demos?style=flat-square" alt="Python Versions"></a>
  <a href="https://github.com/jedi-master-council/agentic-security-demos/blob/main/LICENSE"><img src="https://img.shields.io/github/license/jedi-master-council/agentic-security-demos?style=flat-square" alt="License"></a>
  <a href="https://github.com/jedi-master-council/agentic-security-demos/stargazers"><img src="https://img.shields.io/github/stars/jedi-master-council/agentic-security-demos?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/jedi-master-council/agentic-security-demos/issues"><img src="https://img.shields.io/github/issues/jedi-master-council/agentic-security-demos?style=flat-square" alt="Issues"></a>
</p>

<p align="center">
  <a href="#-demos">Demos</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-reproducibility">Reproducibility</a> •
  <a href="#-venues">Venues</a> •
  <a href="#-citation">Citation</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

---

## 🎯 Demos

| # | Demo | Focus | Status |
|---|------|-------|--------|
| 01 | **Blind Verification** | Cryptographic verification of agent outputs without trusted execution environments | 🟢 <a href="https://dl.acm.org/journal/tosem" target="_blank" rel="noopener noreferrer">ACM TOSEM</a> |
| 02 | **Supply Chain AIBOM Drift** | AI Bill of Materials tracking & drift detection across model updates | 🟢 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32" target="_blank" rel="noopener noreferrer">IEEE TSE</a> |
| 03 | **Eval Design Invariants** | Statistically rigorous evaluation frameworks with invariant guarantees | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 04 | **Prompt Injection & Tool Authority** | Capability-based authority mediation for tool-using agents | 🟢 <a href="https://sp2027.ieee-security.org/cfpapers.html" target="_blank" rel="noopener noreferrer">S&P</a> |
| 05 | **Evidence Release Assurance** | Cryptographic evidence chains for agent accountability | 🟢 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">TDSC</a> |
| 06 | **Network Recon** | eBPF-backed network reconnaissance with formal admission control | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">AsiaCCS</a> |
| 07 | **Malware Triage** | Statistical reconstruction of malware triage decisions | 🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 08 | **File Inclusion** | Provenance-tracked file inclusion for agent workflows | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">AsiaCCS</a> |
| 09 | **MITM Interception** | Ephemeral buffer interception for credential extraction detection | 🟢 <a href="https://sp2027.ieee-security.org/cfpapers.html" target="_blank" rel="noopener noreferrer">S&P</a> |
| 10 | **Vulnerability Assessment** | Cross-vendor vulnerability scanning with authoritative taxonomy | 🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 11 | **Degenerate Reporting** | Meta-science audit: evaluations that cannot rule out do-nothing policies | 🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 12 | **Provenance-Bound Authorization** | Provenance-aware authorization for untrusted calendar content | 🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 13 | **Typed Commitments & Coverage Cues** | Wrong coverage cues and agreement-gate failures in LLM assessors | 🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 14 | **Conformal Action Gating** | Distribution-free risk control for tool execution and how it fails under benchmark shift | 🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">DSN</a> |
| 15 | **Hijack Probes** | Hidden-state signatures of instruction hijack in open-weight agents | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 16 | **Infection Spread** | Epidemic dynamics of prompt-injection propagation in multi-agent systems | 🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">DSN</a> |
| 17 | **Report Fidelity** | Claims-versus-logs fidelity of coding agents | 🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 18 | **Cross-lingual Gap** | Cross-lingual transfer of injections and the detector language gap | 🟢 <a href="https://www2027.thewebconf.org/research-track-papers" target="_blank" rel="noopener noreferrer">WWW</a> |
| 19 | **Lineage Risk** | Inherited risk along fine-tune lineages on the model hub | 🟢 <a href="https://www2027.thewebconf.org/research-track-papers" target="_blank" rel="noopener noreferrer">WWW</a> |
| 20 | **Agent Web Census** | Agent-facing files and in-the-wild injections across the web | 🟢 <a href="https://www2027.thewebconf.org/research-track-papers" target="_blank" rel="noopener noreferrer">WWW</a> |
| 21 | **MCP Ecosystem Census** | Tool-poisoning exposure, rug-pull dynamics and capability surface across 36k MCP servers (toy census) | 🟢 <a href="https://www2027.thewebconf.org/research-track-papers" target="_blank" rel="noopener noreferrer">WWW</a> |
| 22 | **Memory Leakage** | Contextual-integrity leakage via agent memory stores | 🟠 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">PoPETs</a> |
| 23 | **Fault Injection** | Dependability of agent pipelines under pipeline faults | 🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">DSN</a> |
| 24 | **Delegation Checks** | Authorization and agent-to-agent delegation properties | 🟡 <a href="https://csf2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">CSF</a> |
| 25 | **Attestation Verifier** | Install-time provenance verification for agent supply chains | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">AsiaCCS</a> |
| 26 | **Sandbox Probes** | Agent sandbox isolation and exfiltration controls | 🟢 <a href="https://sp2027.ieee-security.org/cfpapers.html" target="_blank" rel="noopener noreferrer">S&P</a> |
| 27 | **CI Trigger Scan** | Injection surface of coding agents wired to CI | 🟢 <a href="https://www2027.thewebconf.org/research-track-papers" target="_blank" rel="noopener noreferrer">WWW</a> |
| 28 | **Memory Poisoning** | Persistent memory poisoning and the MemScope auditor toy | 🟢 <a href="https://www2027.thewebconf.org/demos/" target="_blank" rel="noopener noreferrer">WWW</a> |
| 29 | **Provenance Graphs** | Tamper-evident provenance for post-incident reconstruction | 🟢 <a href="https://sp2027.ieee-security.org/cfpapers.html" target="_blank" rel="noopener noreferrer">S&P</a> |
| 30 | **Default Configs** | Insecure defaults in self-hosted LLM stacks | 🟢 <a href="https://sp2027.ieee-security.org/cfpapers.html" target="_blank" rel="noopener noreferrer">S&P</a> |
| 31 | **Declaration Gap** | MCP registry declared-versus-exercised authority in agent integrations | 🟢 <a href="https://facctconference.org/2027/cfp.html" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 32 | **Reproducibility Audit** | Artefact audit of the agent-security literature | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">AsiaCCS SoK</a> |
| 33 | **Protocol Coverage** | Agent protocol element × threat coverage map | 🟢 <a href="https://sp2027.ieee-security.org/cfpapers.html" target="_blank" rel="noopener noreferrer">S&P</a> |
| 34 | **Visual Injection** | Typographic injection against vision-language agents | 🟠 <a href="https://cvpr.thecvf.com/Conferences/2027/CallForPapers" target="_blank" rel="noopener noreferrer">CVPR</a> |
| 35 | **Scaling Meta-regression** | Agent misbehaviour versus scale across benchmarks | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 36 | **Card Debt** | Documentation debt across open model cards | 🟢 <a href="https://www2027.thewebconf.org/research-track-papers" target="_blank" rel="noopener noreferrer">WWW</a> |
| 37 | **Detector Cost** | Injection-detector comparison with false-positive cost | 🟢 <a href="https://facctconference.org/2027/cfp.html" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 38 | **Assurance Claims** | System-card assurance claims versus obligations | 🟢 <a href="https://facctconference.org/2027/cfp.html" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 39 | **Incident Taxonomy** | Agentic-AI threat taxonomy for practitioners | 🟢 <a href="https://facctconference.org/2027/cfp.html" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 40 | **Corpus Union** | License-audited unified agentic-security corpus | 🔵 <a href="https://www.nature.com/sdata/" target="_blank" rel="noopener noreferrer">Sci Data</a> |
| 41 | **Ten Invariants** | Security invariants checklist synthesis | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 42 | **Patch Lifecycle** | Vulnerability lifecycle and patch adoption lag | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">AsiaCCS</a> |
| 43 | **Terms Coding** | Platform terms accountability allocation | 🟢 <a href="https://www2027.thewebconf.org/research-track-papers" target="_blank" rel="noopener noreferrer">WWW</a> |
| 44 | **Toolflow Taint** | Cross-tool dataflow integrity tracking | 🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 45 | **Exact Nulls for Localisation Claims** | Exact hypergeometric significance, ratio-to-null transfer failure and design-limit corollary; code lives in the private `demo-45-localisation-nulls` repository | 🟢 <a href="https://facctconference.org/2027/cfp.html" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 46 | **Embedding-swap Cosine Shift** | `1 − cosine` on two synthetic vectors against the frozen simulated-study mean 0.1222; code lives in the private `demo-46-simulated-embedding-drift-aibom` repository | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">AsiaCCS</a> |
| 47 | **Pre-reveal Seal** | Hash a localisation commitment before the answer key opens, so a post-seal edit is a mismatch; code lives in the private `demo-47-blind-verification-eval-sais` repository | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 48 | **OAuth Over-privilege** | OAuth scope over-privilege and scope creep in agent integrations; code lives in the private `demo-48-scope-creep-oauth-overprivilege-tops` repository | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 49 | **Tier Fallback** | Authority invariance when an orchestrator changes model tier mid-task | 🟡 <a href="https://csf2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">CSF</a> |
| 50 | **Budget Delegation** | Token and cost budgets conserved across a multi-agent delegation tree | 🟡 <a href="https://csf2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">CSF</a> |
| 51 | **Guardrail Equity** | Accessibility-related false-positive disparity in input guardrails | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 52 | **Simulation V&V** | Held-out and contamination-probe checks for toy cohort simulators | 🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">DSN</a> |
| 53 | **Human Validation** | Sampled validation of agent outputs with planted errors | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 54 | **Stress Transfer** | A detector that passes in-distribution stress items fails under shift | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 55 | **Scaffolding Retention** | Analytic power for an immediate versus residual two-arm contrast | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 56 | **Learning Meta-analysis** | Inverse-variance fixed-effect summary of synthetic study rows | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 57 | **Governance Corpus** | Codebook validation and rater agreement on synthetic HE policy excerpts | 🔵 <a href="https://cscw.acm.org/rolling.html" target="_blank" rel="noopener noreferrer">CSCW</a> |
| 58 | **Work Exposure** | Task-level exposure and an agentic-action share for synthetic HE roles | 🟡 <a href="https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/" target="_blank" rel="noopener noreferrer">IJCAI</a> |
| 59 | **Foresight Delphi** | Median, IQR and consensus on synthetic ratings bound to a briefing hash | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 60 | **EngBio Battery** | Score three synthetic analysis tasks against predeclared references | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">AsiaCCS</a> |
| 61 | **Re-execution Checks** | Machine re-execution and number-provenance checks of agent-written analyses of public biological data (kept in a separate repository; not included here) | 🟡 <a href="https://icml.cc/Conferences/2027/CallForPapers" target="_blank" rel="noopener noreferrer">ICML</a> |
| 62 | **LLM Learner Policy** | Schema adherence, persona sensitivity and calibration of an LLM learner policy against non-LLM baselines on public 2013 learner data (separate repository; not included here) | 🟡 <a href="https://educationaldatamining.org/edm2027/call-for-papers/" target="_blank" rel="noopener noreferrer">EDM</a> |
| 63 | **Policy-Coding Reliability** | How reliably two model families code public institutional AI policies across two archive waves (separate repository; not included here) | 🟡 <a href="https://aied-conference.org/2027/call-for-papers/main-track" target="_blank" rel="noopener noreferrer">AIED</a> |
| 64 | **Socratic Answer Guard** | Calibration of an answer guard for a Socratic study assistant on scripted adversarial learner dialogues (separate repository; not included here) | 🟡 <a href="https://aied-conference.org/2027/call-for-papers/main-track" target="_blank" rel="noopener noreferrer">AIED</a> |
| 65 | **Security–Education Bibliometrics** | A registered bibliometric screen of whether UK agentic-AI security and AI-in-education research communities co-author, 2023 to 2026 (separate repository; not included here) | 🟡 <a href="https://issi2027.ntu.edu.tw/submission-guidelines" target="_blank" rel="noopener noreferrer">ISSI</a> |
| 66 | **QPU Budget Arms** | Accepted results per simulated QPU-second for default, rule-based and simulate-first workflow arms | 🟠 <a href="https://isc-hpc.com/submissions/research-paper/" target="_blank" rel="noopener noreferrer">ISC 2027</a> |
| 67 | **Multi-Table Memorisation Probe** | Row and cross-table completion scores against a remapped-table null at a fixed false-positive rate | 🟡 <a href="https://2027.aclweb.org/calls/main/" target="_blank" rel="noopener noreferrer">ACL 2027 (ARR)</a> |
| 68 | **Identifier Filter** | Span-level recall, residue and k = 1 re-identification after rule-based redaction of scripted learner messages | 🟡 <a href="https://www.petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 4</a> |
| 69 | **Grounded Terms Extraction** | Verbatim-quote grounding and value consistency for extracted tier, data-use, price, continuity and exit terms | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 70 | **SoD Conflicts** | Deterministic detection of mutually exclusive permission pairs in effective RBAC assignments | 🔵 <a href="https://www.sciencedirect.com/journal/computers-and-security" target="_blank" rel="noopener noreferrer">Computers & Security</a> |
| 71 | **Feature-Erasure Search** | Complete heuristic search for the cheapest feature erasures that flip a linear score | 🔵 <a href="https://cis.ieee.org/publications/ieee-transactions-on-artificial-intelligence/ieee-transactions-on-artificial-intelligence" target="_blank" rel="noopener noreferrer">IEEE TAI</a> |
| 72 | **Control Mapping** | Set-based alignment of public technique catalogues to public control catalogues | 🔵 <a href="https://dl.acm.org/journal/tist" target="_blank" rel="noopener noreferrer">ACM TIST</a> |
| 73 | **Open-Set NCM** | Nearest-class-mean classification with a distance threshold that can reject unknowns | 🔵 <a href="https://www.sciencedirect.com/journal/pattern-recognition" target="_blank" rel="noopener noreferrer">Pattern Recognition</a> |
| 74 | **Lipschitz Bound** | Exact two-by-two spectral norms and the product Lipschitz bound of a two-layer linear map | 🔵 <a href="https://cis.ieee.org/publications/t-neural-networks-and-learning-systems/tnnls" target="_blank" rel="noopener noreferrer">IEEE TNNLS</a> |
| 75 | **Advisory Linkage** | Exact-identifier linkage of public advisories and measurement of severity-string disagreement | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=69" target="_blank" rel="noopener noreferrer">IEEE TKDE</a> |
| 76 | **Patrol Search** | Exhaustive and greedy search for a k-node patrol set that covers attacker paths | 🔵 <a href="https://www.jair.org/index.php/jair/about" target="_blank" rel="noopener noreferrer">JAIR</a> |
| 77 | **Horn Repair** | Smallest clause-deletion set that stops forward chaining from deriving false | 🔵 <a href="https://aij.ijcai.org/about-the-artificial-intelligence-journal/" target="_blank" rel="noopener noreferrer">Artificial Intelligence</a> |
| 78 | **Sequential Covering** | Greedy sequential covering that learns an ordered list of single-feature rules | 🔵 <a href="https://aaai.org/conference/aaai/aaai-27/main-technical-track-call/" target="_blank" rel="noopener noreferrer">AAAI</a> |
| 79 | **Contrast Sets** | Item support in two windows and the growth rate that marks an emerging contrast set | 🟡 <a href="https://kdd2027.kdd.org/research-track-call-for-papers/" target="_blank" rel="noopener noreferrer">KDD</a> |
| 80 | **SoK: Injection Defences** | A systematised review of indirect prompt-injection defences with a double-coded extraction protocol over the defence literature | 🟡 <a href="https://dl.acm.org/journal/csur" target="_blank" rel="noopener noreferrer">CSUR</a> |
| 81 | **The Agent-Security Benchmark** | Frozen gates, pinned corpora and registered falsification packaged as a re-runnable agent-security benchmark with baselines | 🟡 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS D&B</a> |
| 82 | **Guardrail Score Transfer** | Whether guardrail-model benchmark scores predict behaviour on recorded tool-attack trajectories; the score-to-replay cross-tabulation | 🟡 <a href="https://2027.emnlp.org/" target="_blank" rel="noopener noreferrer">EMNLP</a> |
| 83 | **MCP Registry Census** | Description-injection and authorisation-gap surface across MCP server manifests at registry scale, at two dated snapshots | 🟡 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P</a> |
| 84 | **Longitudinal Security Drift** | A ten-framework, multi-release census of agentic frameworks' security-relevant surface: the drift graph per transition | 🟡 <a href="https://ieeecss.org/committee/ieee-transactions-information-forensics-and-security" target="_blank" rel="noopener noreferrer">TIFS</a> |
| 85 | **The Enforcement Matrix** | Whether provenance labels are enforced at the sink per framework, per sink class and per mediation mode — or merely documented | 🟡 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 86 | **Personal-Data Exposure Census** | Personal-data shapes in recorded agent trajectories' tool arguments, per tool class and per sink, against a registered shape lexicon | 🟡 <a href="https://petsymposium.org/" target="_blank" rel="noopener noreferrer">PoPETs</a> |
| 87 | **The Skill-Plugin Supply Chain** | Declared tool access versus statically extractable capability per skill in the agent marketplaces, in both overstatement directions | 🟡 <a href="https://www.sciencedirect.com/journal/computers-and-security" target="_blank" rel="noopener noreferrer">C&S</a> |
| 88 | **Detection Benchmark: Injected Actions** | A labelled injected-action detection benchmark with baseline detectors and per-stratum metrics | 🟡 <a href="https://raid-symposium.org/" target="_blank" rel="noopener noreferrer">RAID</a> |
| 89 | **Tool-Schema Interpretation Divergence** | Where agentic frameworks interpret the same tool schema differently, measured per schema-framework pair | 🟡 <a href="https://conf.researchr.org/track/icse-2027/icse-2027-research-papers" target="_blank" rel="noopener noreferrer">FSE/ICSE</a> |

Each demo is a **self-contained, reproducible research artifact** with:
- 📦 Frozen dependencies & environment specifications
- 📊 Pre-computed evidence packages (JSON)
- 🧪 Comprehensive test suites (≥90% coverage)
- 📄 Venue-aligned documentation & claim ledgers
- 🔬 Statistical validation scripts

---

## ⚙️ Installation

```bash
git clone https://github.com/jedi-master-council/agentic-security-demos.git
cd agentic-security-demos
pip install -e ".[dev]"
```

### Verify Installation

```bash
# Run every demo's test suite
make test

# Run one demo's suite (folders demo-01 … demo-89; 61 to 65 are listed but kept in separate repositories)
make test DEMO=01
```

---

## 🚀 Quick Start

All demos run offline from the repository root — no API keys, no network.
Each demo folder also has step-by-step `INSTRUCTIONS.md` with expected outputs.

```bash
# Run a teaching demo (folders demo-01 … demo-89; 61 to 65 are listed but kept in separate repositories)
make demo DEMO=01   # Blind Verification
make demo DEMO=04   # Prompt Injection Authority
make demo DEMO=07   # Malware Triage
make demo DEMO=13   # Typed Commitments & Coverage Cues
make demo DEMO=14   # Conformal Action Gating (DSN 2027 toy)
make demo DEMO=21   # MCP Ecosystem Census (WWW toy)
make demo DEMO=28   # Memory Poisoning (WWW demo-track toy)
make demo DEMO=44   # Toolflow Taint (EuroS&P toy)
make demo DEMO=45   # Exact Nulls for Localisation Claims (FAccT toy)
make demo DEMO=46   # Embedding-swap Cosine Shift (AsiaCCS toy)
make demo DEMO=47   # Pre-reveal Seal (USENIX Security C2 toy)

# Run a demo's test suite
make test DEMO=01

# Run every demo sequentially
make all-demos

# Check offline-safety constraints (no network imports, no credentials)
make verify-safety
```

### 30-second wiring check

```bash
make help
```

Expected output: the root command list (`make setup`, `make test DEMO=01`,
`make demo DEMO=01`, `make verify-safety`, `make all-demos`).

---

## 🔬 Reproducibility

All demos follow the **Agentic Security Reproducibility Standard**:

| Guarantee | Mechanism |
|-----------|-----------|
| **Environment Freeze** | `requirements.lock` + `conda-lock.yml` + Docker images |
| **Evidence Immutability** | SHA-256 sealed reference outputs in each demo's `results/` (🌟 Episode VI sealed Holocron — Zenodo deposit only on acceptance) |
| **Statistical Rigor** | Pre-registered analysis plans with p-value correction |
| **Compute Transparency** | GPU-hours logged; CPU fallback documented |
| **Adversarial Robustness** | Seeded RNG; deterministic attack ordering |

### Reproducibility Checklist
- [ ] Clone repo at tagged release
- [ ] Install exact dependencies: `pip install -r requirements.lock`
- [ ] Use the fixtures and reference outputs in each demo's `results/` (no external download needed)
- [ ] Run: `agentic-security-demos reproduce --all`
- [ ] Compare outputs to `results/reference/`

---

## 🏛️ Venues & Publications

> Venue abbreviation links to the conference page; the deadline line under it links to the
> submission portal (abstract + full-paper dates). **A** is the first choice; **B** / **C**
> activate only after the previous option's decision — the same work is never under review
> in two places at once.
>
> **Caps (rebalanced 11 November 2026):** EuroS&P at most 7 papers per author (<a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">CFP</a>) — 7 allocated (07, 10, 11, 12, 13, 17, 44), full. IEEE S&P 6 per author per cycle — 6 submitted for Cycle 2 on 16 November 2026 (04, 09, 26, 29, 30, 33-SoK). USENIX Security 7 per cycle — 7 allocated (41, 47, 48, 51, 53, 54, 69). AsiaCCS R2 trimmed from 22 papers to 7 (06, 08, 25, 32-SoK, 42, 46, 60) to avoid one-author overload; displaced demos moved to the nearest-fitting top-tier deadlines: ICML 2027 (03, 15, 35, 55, 56; abstracts 14 Jan, papers 22 Jan), USENIX Security Cycle 2 (41, 47, 48, 53, 54), CSF Winter (49, 50) and DSN 2027 (52; DSN now hosts 14, 16, 23, 52). Caps are per venue; the same paper is never under review at two venues at once.
>
> **Demos 61 to 79 (19 November 2026):** demos 61 to 65 are kept in separate repositories and are listed here only. Demos 66 to 69 are new. Demo 69 takes the seventh USENIX Security Cycle 2 slot, which fills that cycle's per-author cap. The ten journal-targeted demos first numbered 61 to 70 are now 70 to 79, with unchanged content. ICML 2027's call (read 19 November 2026) gives abstracts 14 January and papers 22 January 2027, and limits an author who does not meet its reciprocal-reviewer criteria to two submissions.
>
> **New-tab links (22 November 2026):** every venue and deadline link below carries `target="_blank" rel="noopener noreferrer"`. GitHub's README renderer removes `target` for security, so the reliable way to keep the map open is the rendered **[Venue Map](https://jedi-master-council.github.io/agentic-security-demos/venues/)** on the documentation site, where every link opens in a new tab. On github.com itself, use Ctrl/Cmd-click or middle-click.
>
> **Option A rule (9 November 2026):** A is the nearest real deadline at a world-leading top-5/top-10 conference that fits the page length; B and C are later top-5/top-10 venues (a top journal may be B or C) whose deadlines fall after the previous option's official notification. Notification dates checked on the official CFPs on 9 November 2026: AsiaCCS R2 31 March 2027; EuroS&P 18 March 2027; S&P Cycle 2 acceptance 5 March 2027; USENIX Security Cycle 2 6 May 2027; CSF Winter 5 April 2027; IJCAI 21 April 2027; PoPETs Issue 3 1 February 2027. USENIX Security 2027 Cycle 2 (26 January) and CSF 2027 Winter (28 January) therefore cannot follow AsiaCCS R2, EuroS&P, S&P Cycle 2 or IJCAI. DSN, ACNS and USENIX SAIS are not used as Option A. **IJCAI 2027** is reserved as demo 58's primary paper (Primary Paper Initiative). **Demo 40 exception:** Scientific Data remains Option A because it is a dataset paper with an existing submission pack, and its data stays as-is. **Scope exceptions (11 November 2026):** demo 57 (governance corpus) uses CSCW 2027 rolling as Option A — no top-tier conference with a nearer deadline fits its scope; demo 59 (foresight Delphi) likewise uses FAccT 2028 (call unpublished).

| Demo | Option A | Option B | Option C |
|:---:|---|---|---|
| 01 | 🟢 <a href="https://dl.acm.org/journal/tosem" target="_blank" rel="noopener noreferrer">ACM TOSEM</a> | 🔵 <a href="https://link.springer.com/journal/10664" target="_blank" rel="noopener noreferrer">EMSE</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 02 | 🟢 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32" target="_blank" rel="noopener noreferrer">IEEE TSE</a> | 🔵 <a href="https://www.sciencedirect.com/journal/journal-of-systems-and-software" target="_blank" rel="noopener noreferrer">JSS</a> | 🔵 <a href="https://www.sciencedirect.com/journal/information-and-software-technology" target="_blank" rel="noopener noreferrer">IST</a> |
| 03 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 04 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/cfp.html" target="_blank" rel="noopener noreferrer">CCS 2027 (dates TBD)</a> |
| 05 | 🟢 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | — | — |
| 06 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/cfp.html" target="_blank" rel="noopener noreferrer">CCS 2027 (dates TBD)</a> |
| 07 | 🟠 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a><br>🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">reg 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://dl.acm.org/conference/raid" target="_blank" rel="noopener noreferrer">RAID 2027 (call unpublished)</a> | 🔵 <a href="https://www.acsac.org/" target="_blank" rel="noopener noreferrer">ACSAC</a> / <a href="https://conf.laas.fr/esorics" target="_blank" rel="noopener noreferrer">ESORICS</a> |
| 08 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://conf.laas.fr/esorics" target="_blank" rel="noopener noreferrer">ESORICS C2</a> | 🔵 <a href="https://dl.acm.org/conference/raid" target="_blank" rel="noopener noreferrer">RAID</a> |
| 09 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://conf.laas.fr/esorics" target="_blank" rel="noopener noreferrer">ESORICS</a> | 🔵 <a href="https://dl.acm.org/conference/raid" target="_blank" rel="noopener noreferrer">RAID</a> / <a href="https://www.acsac.org/" target="_blank" rel="noopener noreferrer">ACSAC</a> |
| 10 | 🟠 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a><br>🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">reg 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS</a> | 🔵 <a href="https://www.acsac.org/" target="_blank" rel="noopener noreferrer">ACSAC</a> / <a href="https://dl.acm.org/conference/raid" target="_blank" rel="noopener noreferrer">RAID</a> |
| 11 | 🟠 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a><br>🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">reg 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://dl.acm.org/conference/raid" target="_blank" rel="noopener noreferrer">RAID 2027 (call unpublished)</a> | 🔵 <a href="https://conf.laas.fr/esorics" target="_blank" rel="noopener noreferrer">ESORICS</a> / <a href="https://www.acsac.org/" target="_blank" rel="noopener noreferrer">ACSAC</a> |
| 12 | 🟠 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a><br>🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">reg 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS</a> | 🔵 <a href="https://www.ndss-symposium.org/" target="_blank" rel="noopener noreferrer">NDSS</a> |
| 13 | 🟠 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a><br>🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">reg 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/cfp.html" target="_blank" rel="noopener noreferrer">CCS 2027 (dates TBD)</a> |
| 14 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 15 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://iclr.cc/" target="_blank" rel="noopener noreferrer">ICLR 2028 (call unpublished)</a> |
| 16 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 17 | 🟠 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a><br>🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">reg 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://www.ifaamas.org/" target="_blank" rel="noopener noreferrer">AAMAS 2028 (call unpublished)</a> |
| 18 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://aclrollingreview.org/" target="_blank" rel="noopener noreferrer">ACL (ARR)</a> | 🔵 <a href="https://aclanthology.org/venues/emnlp/" target="_blank" rel="noopener noreferrer">EMNLP</a> |
| 19 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://www.icse-conferences.org/" target="_blank" rel="noopener noreferrer">ICSE</a><br>🔵 <a href="https://www.icse-conferences.org/" target="_blank" rel="noopener noreferrer">abs ~23 Jun 2027</a> | 🔵 <a href="https://www.esec-fse.org/" target="_blank" rel="noopener noreferrer">FSE</a> |
| 20 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🟠 <a href="https://www2027.thewebconf.org/research-track-papers" target="_blank" rel="noopener noreferrer">WWW short</a> / <a href="https://conferences.sigcomm.org/imc/" target="_blank" rel="noopener noreferrer">IMC</a><br>🟠 <a href="https://www2027.thewebconf.org/research-track-papers" target="_blank" rel="noopener noreferrer">16 Nov</a> | — |
| 21 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://conferences.sigcomm.org/imc/" target="_blank" rel="noopener noreferrer">IMC</a> | 🔵 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS</a> |
| 22 | 🟠 <a href="https://petsymposium.org/2027" target="_blank" rel="noopener noreferrer">PoPETs</a><br>🟠 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">Issue 3: 30 Nov</a> | 🟡 <a href="https://petsymposium.org/2027" target="_blank" rel="noopener noreferrer">PoPETs Issue 4</a><br>🟡 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">28 Feb</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> |
| 23 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 24 | 🟡 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF Winter</a><br>🟡 <a href="https://csf2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">papers 28 Jan</a> | 🔵 <a href="https://conf.laas.fr/esorics" target="_blank" rel="noopener noreferrer">ESORICS C2</a> / <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS</a> | — |
| 25 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/cfp.html" target="_blank" rel="noopener noreferrer">CCS 2027 (dates TBD)</a> |
| 26 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/cfp.html" target="_blank" rel="noopener noreferrer">CCS 2027 (dates TBD)</a> |
| 27 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://www.blackhat.com/" target="_blank" rel="noopener noreferrer">Black Hat / Arsenal</a> | 🔵 <a href="https://www.defcon.org/" target="_blank" rel="noopener noreferrer">DEF CON Demo Labs</a> |
| 28 | 🟢 <a href="https://www2027.thewebconf.org/demos/" target="_blank" rel="noopener noreferrer">WWW demo track</a> | 🔵 <a href="https://www.defcon.org/" target="_blank" rel="noopener noreferrer">DEF CON</a><br>🔵 <a href="https://www.defcon.org/" target="_blank" rel="noopener noreferrer">~1 May 2027</a> | 🔵 <a href="https://www.blackhat.com/" target="_blank" rel="noopener noreferrer">Black Hat Arsenal</a> |
| 29 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10206" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 30 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10206" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> |
| 31 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 32 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2 SoK</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/csur" target="_blank" rel="noopener noreferrer">ACM CSUR</a> | 🔵 <a href="https://www.comsoc.org/publications/journals/ieee-comst" target="_blank" rel="noopener noreferrer">IEEE COMST</a> |
| 33 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2 SoK</a> | 🔵 <a href="https://www.comsoc.org/publications/journals/ieee-comst" target="_blank" rel="noopener noreferrer">IEEE COMST</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=5" target="_blank" rel="noopener noreferrer">Proc. IEEE</a> |
| 34 | 🟠 <a href="https://cvpr.thecvf.com/Conferences/2027/CallForPapers" target="_blank" rel="noopener noreferrer">CVPR</a><br>🟠 <a href="https://cvpr.thecvf.com/Conferences/2027/Dates" target="_blank" rel="noopener noreferrer">enroll 10 Nov · papers 16 Nov</a> | 🔵 <a href="https://www.computer.org/csdl/journal/tp" target="_blank" rel="noopener noreferrer">IEEE TPAMI</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 35 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://jmlr.org/" target="_blank" rel="noopener noreferrer">JMLR</a> |
| 36 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://www.nature.com/natmachintell/" target="_blank" rel="noopener noreferrer">Nature MI</a> | 🔵 <a href="https://www.cell.com/patterns" target="_blank" rel="noopener noreferrer">Patterns</a> |
| 37 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10206" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 38 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🔵 <a href="https://academic.oup.com/cybersecurity" target="_blank" rel="noopener noreferrer">J. Cybersecurity</a> | 🔵 <a href="https://dl.acm.org/journal/jrc" target="_blank" rel="noopener noreferrer">ACM JRC</a> |
| 39 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🔵 <a href="https://www.computer.org/csdl/magazine/sp" target="_blank" rel="noopener noreferrer">S&P Magazine</a> | 🔵 <a href="https://cacm.acm.org/" target="_blank" rel="noopener noreferrer">CACM Practice</a> |
| 40 | 🔵 <a href="https://www.nature.com/sdata/" target="_blank" rel="noopener noreferrer">Scientific Data</a> | 🔵 <a href="https://www.sciencedirect.com/journal/data-in-brief" target="_blank" rel="noopener noreferrer">Data in Brief</a> / <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS D&B</a> / <a href="https://data.mlr.press" target="_blank" rel="noopener noreferrer">DMLR</a> | — |
| 41 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://cacm.acm.org/" target="_blank" rel="noopener noreferrer">CACM</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/cfp.html" target="_blank" rel="noopener noreferrer">CCS 2027 (dates TBD)</a> |
| 42 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32" target="_blank" rel="noopener noreferrer">IEEE TSE</a> |
| 43 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://www.aies-conference.com/" target="_blank" rel="noopener noreferrer">AIES</a> | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 44 | 🟠 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a><br>🟠 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">reg 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://www.ndss-symposium.org/" target="_blank" rel="noopener noreferrer">NDSS (next cycle)</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS</a> |
| 45 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 46 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 47 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 48 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> |
| 49 | 🟡 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF Winter</a><br>🟡 <a href="https://csf2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">papers 28 Jan</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/cfp.html" target="_blank" rel="noopener noreferrer">CCS 2027 (dates TBD)</a> / <a href="https://csf2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">CSF 2028 (unconfirmed)</a> |
| 50 | 🟡 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF Winter</a><br>🟡 <a href="https://csf2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">papers 28 Jan</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> / <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/cfp.html" target="_blank" rel="noopener noreferrer">CCS 2027 (dates TBD)</a> |
| 51 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT 2028 (call unpublished)</a> |
| 52 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://www.ifaamas.org/" target="_blank" rel="noopener noreferrer">AAMAS 2028 (call unpublished)</a> |
| 53 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 54 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/cfp.html" target="_blank" rel="noopener noreferrer">CCS 2027 (dates TBD)</a> / <a href="https://satml.org/" target="_blank" rel="noopener noreferrer">SaTML 2028 (call unpublished)</a> |
| 55 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT 2028 (call unpublished)</a> |
| 56 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 57 | 🔵 <a href="https://cscw.acm.org/rolling.html" target="_blank" rel="noopener noreferrer">CSCW</a> | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT 2028 (call unpublished)</a> | 🔵 <a href="https://chi.acm.org/" target="_blank" rel="noopener noreferrer">CHI 2028 (call unpublished)</a> |
| 58 | 🟡 <a href="https://2027.ijcai.org/" target="_blank" rel="noopener noreferrer">IJCAI</a><br>🟡 <a href="https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/" target="_blank" rel="noopener noreferrer">abs 4 Jan · papers 11 Jan</a> | 🟡 <a href="https://neurips.cc/Conferences/FutureMeetings" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> | 🔵 <a href="https://cscw.acm.org/rolling.html" target="_blank" rel="noopener noreferrer">ACM CSCW rolling</a> |
| 59 | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT 2028 (call unpublished)</a> | 🔵 <a href="https://cscw.acm.org/rolling.html" target="_blank" rel="noopener noreferrer">CSCW</a> | 🔵 <a href="https://chi.acm.org/" target="_blank" rel="noopener noreferrer">CHI 2028 (call unpublished)</a> |
| 60 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://satml.org/" target="_blank" rel="noopener noreferrer">SaTML 2028 (call unpublished)</a> / <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 61 | 🟡 <a href="https://icml.cc/Conferences/2027/CallForPapers" target="_blank" rel="noopener noreferrer">ICML 2027</a><br>🟡 <a href="https://openreview.net/group?id=ICML.cc/2027/Conference" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://acm-rep.github.io/2027" target="_blank" rel="noopener noreferrer">ACM REP 2028 (call unpublished)</a> |
| 62 | 🟡 <a href="https://educationaldatamining.org/edm2027/call-for-papers/" target="_blank" rel="noopener noreferrer">EDM 2027</a><br>🟡 <a href="https://educationaldatamining.org/edm2027/important-dates/" target="_blank" rel="noopener noreferrer">abs 8 Feb · papers 15 Feb</a> | 🔵 <a href="https://jedm.educationaldatamining.org/index.php/JEDM" target="_blank" rel="noopener noreferrer">JEDM</a> | 🔵 <a href="https://aied-conference.org/" target="_blank" rel="noopener noreferrer">AIED 2028 (call unpublished)</a> |
| 63 | 🟡 <a href="https://aied-conference.org/2027/call-for-papers/main-track" target="_blank" rel="noopener noreferrer">AIED 2027</a><br>🟡 <a href="https://aied-conference.org/2027/important-dates" target="_blank" rel="noopener noreferrer">abs 22 Jan · papers 1 Feb</a> | 🔵 <a href="https://pacmhci.acm.org/" target="_blank" rel="noopener noreferrer">CSCW (PACM HCI)</a> | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT 2028 (call unpublished)</a> |
| 64 | 🟡 <a href="https://aied-conference.org/2027/call-for-papers/main-track" target="_blank" rel="noopener noreferrer">AIED 2027</a><br>🟡 <a href="https://aied-conference.org/2027/important-dates" target="_blank" rel="noopener noreferrer">abs 22 Jan · papers 1 Feb</a> | 🔵 <a href="https://jedm.educationaldatamining.org/index.php/JEDM" target="_blank" rel="noopener noreferrer">JEDM</a> | 🔵 <a href="https://educationaldatamining.org/" target="_blank" rel="noopener noreferrer">EDM 2028 (call unpublished)</a> |
| 65 | 🟡 <a href="https://issi2027.ntu.edu.tw/submission-guidelines" target="_blank" rel="noopener noreferrer">ISSI 2027</a><br>🟡 <a href="https://www.conftool.pro/issi2027/" target="_blank" rel="noopener noreferrer">papers 15 Jan</a> | 🔵 <a href="https://link.springer.com/journal/11192" target="_blank" rel="noopener noreferrer">Scientometrics</a> | 🔵 <a href="https://direct.mit.edu/qss" target="_blank" rel="noopener noreferrer">QSS</a> |
| 66 | 🟠 <a href="https://isc-hpc.com/submissions/research-paper/" target="_blank" rel="noopener noreferrer">ISC 2027</a><br>🟠 <a href="https://isc-hpc.com/submissions/research-paper/" target="_blank" rel="noopener noreferrer">abs 14 Dec · papers 21 Dec</a> | 🔵 <a href="https://qce.quantum.ieee.org/" target="_blank" rel="noopener noreferrer">IEEE QCE 2027 (call unpublished)</a> | 🔵 <a href="https://dl.acm.org/journal/tqc" target="_blank" rel="noopener noreferrer">ACM TQC</a> |
| 67 | 🟡 <a href="https://2027.aclweb.org/calls/main/" target="_blank" rel="noopener noreferrer">ACL 2027 (ARR)</a><br>🟡 <a href="https://www.aclweb.org/portal/content/acl-2027-first-call-papers" target="_blank" rel="noopener noreferrer">ARR 4 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://iclr.cc/" target="_blank" rel="noopener noreferrer">ICLR 2028 (call unpublished)</a> |
| 68 | 🟡 <a href="https://www.petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 4</a><br>🟡 <a href="https://www.petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">papers 28 Feb</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://signalprocessingsociety.org/publications-resources/ieee-transactions-information-forensics-and-security" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> |
| 69 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://petsymposium.org/" target="_blank" rel="noopener noreferrer">PoPETs 2028 (call unpublished)</a> |
| 70 | 🔵 <a href="https://computersandsecurity.org/aims-and-scope/" target="_blank" rel="noopener noreferrer">Computers & Security</a><br>🔵 <a href="https://computersandsecurity.org/aims-and-scope/" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> |
| 71 | 🔵 <a href="https://cis.ieee.org/publications/ieee-transactions-on-artificial-intelligence/information-for-authors-tai" target="_blank" rel="noopener noreferrer">IEEE TAI</a><br>🔵 <a href="https://ieee.atyponrex.com/journal/tai-ieee" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 72 | 🔵 <a href="https://dl.acm.org/journal/tist/author-guidelines" target="_blank" rel="noopener noreferrer">ACM TIST</a><br>🔵 <a href="https://dl.acm.org/journal/tist/author-guidelines" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://iclr.cc/" target="_blank" rel="noopener noreferrer">ICLR 2028 (call unpublished)</a> |
| 73 | 🔵 <a href="https://shop.elsevier.com/journals/pattern-recognition/0031-3203" target="_blank" rel="noopener noreferrer">Pattern Recognition</a><br>🔵 <a href="https://shop.elsevier.com/journals/pattern-recognition/0031-3203" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://www.computer.org/csdl/journal/tp" target="_blank" rel="noopener noreferrer">IEEE TPAMI</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 74 | 🔵 <a href="https://cis.ieee.org/publications/t-neural-networks-and-learning-systems/tnnls" target="_blank" rel="noopener noreferrer">IEEE TNNLS</a><br>🔵 <a href="https://ieee.atyponrex.com/journal/tnnls" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 75 | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=69" target="_blank" rel="noopener noreferrer">IEEE TKDE</a><br>🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=69" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 76 | 🔵 <a href="https://www.jair.org/index.php/jair/about" target="_blank" rel="noopener noreferrer">JAIR</a><br>🔵 <a href="https://www.jair.org/index.php/jair/about/submissions" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://iclr.cc/" target="_blank" rel="noopener noreferrer">ICLR 2028 (call unpublished)</a> |
| 77 | 🔵 <a href="https://aij.ijcai.org/call-for-papers/" target="_blank" rel="noopener noreferrer">AIJ</a><br>🔵 <a href="https://aij.ijcai.org/for-authors/" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 78 | 🔵 <a href="https://aaai.org/conference/aaai/" target="_blank" rel="noopener noreferrer">AAAI 2028 (call unpublished)</a><br>🔵 <a href="https://aaai.org/conference/aaai/aaai-27/main-technical-track-call/" target="_blank" rel="noopener noreferrer">AAAI-27 papers closed 28 Jul 2026</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML 2028 (call unpublished)</a> |
| 79 | 🟡 <a href="https://kdd2027.kdd.org/research-track-call-for-papers/" target="_blank" rel="noopener noreferrer">KDD 2027 C2</a><br>🟡 <a href="https://kdd2027.kdd.org/research-track-call-for-papers/" target="_blank" rel="noopener noreferrer">Feb 2027 (exact date UNVERIFIED)</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://iclr.cc/" target="_blank" rel="noopener noreferrer">ICLR 2028 (call unpublished)</a> |
| 80 | 🟡 <a href="https://dl.acm.org/journal/csur" target="_blank" rel="noopener noreferrer">CSUR (call to be re-read)</a> | — | — |
| 81 | 🟡 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS D&B (call to be re-read)</a> | — | — |
| 82 | 🟡 <a href="https://2027.emnlp.org/" target="_blank" rel="noopener noreferrer">EMNLP (call to be re-read)</a> | — | — |
| 83 | 🟡 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P (call to be re-read)</a> | — | — |
| 84 | 🟡 <a href="https://ieeecss.org/committee/ieee-transactions-information-forensics-and-security" target="_blank" rel="noopener noreferrer">TIFS (call to be re-read)</a> | — | — |
| 85 | 🟡 <a href="https://eurosp2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">EuroS&P (call to be re-read)</a> | — | — |
| 86 | 🟡 <a href="https://petsymposium.org/" target="_blank" rel="noopener noreferrer">PoPETs (call to be re-read)</a> | — | — |
| 87 | 🟡 <a href="https://www.sciencedirect.com/journal/computers-and-security" target="_blank" rel="noopener noreferrer">C&S (call to be re-read)</a> | — | — |
| 88 | 🟡 <a href="https://raid-symposium.org/" target="_blank" rel="noopener noreferrer">RAID (call to be re-read)</a> | — | — |
| 89 | 🟡 <a href="https://conf.researchr.org/track/icse-2027/icse-2027-research-papers" target="_blank" rel="noopener noreferrer">FSE/ICSE (call to be re-read)</a> | — | — |

---

## 📖 Citation

If you use this collection in your research, please cite:

```bibtex
@misc{agenticsecuritydemos2026,
  title={Agentic AI Security Demos: A Reproducible Teaching Collection},
  author={{Agentic Security Demos team}},
  year={2026},
  publisher={GitHub},
  journal={GitHub Repository},
  howpublished={\url{https://github.com/jedi-master-council/agentic-security-demos}},
  note={Teaching demos with synthetic fixtures only; no preprints, no datasets deposited yet}
}
```

Individual demo citations available in each subdirectory's `CITATION.cff`.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Core Language** | Python 3.10–3.12 |
| **CLI Framework** | Click 8.x / Typer |
| **Async Runtime** | asyncio, trio |
| **Cryptography** | cryptography, pyca/cryptography |
| **eBPF** | bcc, libbpf, pyroute2 |
| **Statistics** | scipy, statsmodels, pingouin |
| **ML Frameworks** | PyTorch, transformers, vLLM |
| **Testing** | pytest, hypothesis, pytest-benchmark |
| **Packaging** | setuptools, pyproject.toml, hatch |
| **CI/CD** | GitHub Actions, pre-commit |
| **Documentation** | Sphinx, MyST-Parser, Furo theme |

---

## 🤝 Contributing

> 🌟 **Episode V – The Empire Strikes Back.** Every pull request is a trial in the snow:
> the Empire (CI) strikes back with offline tests, safety greps and schema checks. Only
> Padawans who bring evidence survive Hoth. See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- 🐛 Reporting vulnerabilities or reproducibility issues
- 💡 Proposing new demos or venues
- 🔀 Submitting pull requests (evidence-backed changes only)
- 🧪 Extending test suites
- 📝 Improving documentation

**Research Contribution Guidelines (the Jedi Code):**
1. All claims must be backed by frozen evidence packages (no Order-66 surprises)
2. Statistical claims require pre-registered analysis plans
3. New demos must target a top-tier venue with clear scope (choose your training ground)
4. Breaking changes require RFC process (consult the Council first)

---

## 📄 License

Distributed under the **MIT License** — 🌟 *a long time ago in an open-source galaxy…*
free to fork like Rebel plans, no warranty (Alderaan was also uninsured). See [LICENSE](LICENSE) for more information.

Individual demos may have additional licenses for third-party components (see `DEPENDENCIES.md`).

---

## 🙏 Acknowledgments

🌟 **The Rebel Alliance thanks:**

- **Research compute credits** — fuel for the X-wings
- **GitHub Accelerator** — the hidden Rebel base (open-source support)
- **Anonymous reviewers** at SaTML, CCS, NeurIPS, IEEE SP, USENIX, NDSS, RAID, ASIACCS, ESORICS, ACSAC, ICML, ICLR, AAAI, IJCAI, ACL, ICSE, WWW, EuroS&P, PoPETs, DSN, CSF, ACNS, TIFS, TDSC, TOPS, CSUR, COMST, TPAMI, TMLR, Nature MI, Journal of Cybersecurity, Scientific Data, CACM, TSE, FAccT — the Jedi Council: wise, anonymous, occasionally striking back (Episode V)
- **Agentic AI Security community** — the Ewoks who actually help (feedback and replication)

---

<p align="center">
  <strong>Training Padawans in agentic AI security, one reproducible demo at a time — may the Force (of offline, synthetic fixtures) be with you.</strong>
</p>

<p align="center">
  <a href="https://github.com/jedi-master-council/agentic-security-demos/stargazers">⭐ Star</a> •
  <a href="https://github.com/jedi-master-council/agentic-security-demos/fork">🍴 Fork</a> •
  <a href="https://github.com/jedi-master-council/agentic-security-demos/issues">🐛 Report Issue</a> •
  <a href="https://github.com/jedi-master-council/agentic-security-demos/discussions">💬 Discuss</a>
</p>