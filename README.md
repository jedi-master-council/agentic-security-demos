<p align="center">
  <img src="https://raw.githubusercontent.com/jedi-master-council/agentic-security-demos/main/assets/logo.svg" alt="Agentic Security Demos Logo" width="200">
</p>

<h1 align="center">Agentic AI Security Demos</h1>
<p align="center">
  <strong>93 reproducible teaching demos for agentic AI security: prompt injection, tool authority, supply chains, memory, provenance and evaluation. Research prototypes target venues including IEEE S&amp;P, USENIX Security, CCS, NDSS, EuroS&amp;P and DSN. All scenarios, numbers and verdicts are synthetic coursework — not publications.</strong>
</p>

> **Teaching demos, not publications.** A demo may later become a paper; none is a publication claim. Venue names are intended targets only. Fixtures are synthetic and run offline.

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
| 01 | **Blind Verification** | Blind, pre-reveal commitments; whether a typed output schema changes where an assessor looks | 🟢 <a href="https://dl.acm.org/journal/tosem" target="_blank" rel="noopener noreferrer">ACM TOSEM</a> |
| 02 | **Supply Chain AIBOM Drift** | Fail-closed supply-chain gate across CI configurations; AIBOM drift | 🟢 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32" target="_blank" rel="noopener noreferrer">IEEE TSE</a> |
| 03 | **Eval Design Invariants** | Pre-publication invariants; leakage rules tested with planted items | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 04 | **Prompt Injection & Tool Authority** | Tool-authority confinement; a zero attack rate read against its denominator and utility | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> |
| 05 | **Evidence Release Assurance** | Witnessed, omission-resistant evidence chains for release gating | 🟢 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> |
| 06 | **Network Recon** | Provenance-aware recon; text heuristics versus a transport-layer oracle | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a> |
| 07 | **Malware Triage** | Statistical reconstruction of malware triage decisions | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 08 | **File Inclusion** | Provenance-tracked file inclusion for agent workflows | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a> |
| 09 | **MITM Interception** | Ephemeral buffer interception for credential extraction detection | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> |
| 10 | **Vulnerability Assessment** | Scope-bounded scanning; blocked is not contained under a fail-closed denominator | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 11 | **Degenerate Reporting** | Meta-science audit: evaluations that cannot rule out do-nothing policies | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 12 | **Provenance-Bound Authorization** | Provenance-aware authorization for untrusted calendar content | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 13 | **Typed Commitments & Coverage Cues** | Wrong coverage cues and agreement-gate failures in LLM assessors | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 14 | **Conformal Action Gating** | Distribution-free risk control for tool execution and how it fails under benchmark shift | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a> |
| 15 | **Hijack Probes** | Hidden-state signatures of instruction hijack in open-weight agents | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 16 | **Infection Spread** | Relay of injected instructions along an agent chain, against an uninstructed control code | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a> |
| 17 | **Report Fidelity** | Claims-versus-logs fidelity of coding agents | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 18 | **Cross-lingual Gap** | Cross-lingual transfer of injections and the detector language gap | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> |
| 19 | **Lineage Risk** | Inherited risk along fine-tune lineages on the model hub | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> |
| 20 | **Agent Web Census** | Agent-facing files on the web: HTTP 200 checked byte by byte for soft-404s | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> |
| 21 | **MCP Ecosystem Census** | MCP registry census: tool-poisoning markers, hosting, versions, endpoints | 🟢 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">DSN 2027</a> |
| 22 | **Memory Leakage** | Contextual-integrity leakage via agent memory stores | 🟠 <a href="https://petsymposium.org/2027" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 3</a> |
| 23 | **Fault Injection** | Dependability of agent pipelines under pipeline faults | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a> |
| 24 | **Delegation Checks** | Authorization and agent-to-agent delegation properties | 🟡 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF Winter</a> |
| 25 | **Attestation Verifier** | Install-time provenance verification for agent supply chains | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a> |
| 26 | **Sandbox Probes** | Agent sandbox isolation and exfiltration controls | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> |
| 27 | **CI Trigger Scan** | Injection surface of coding agents wired to CI | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> |
| 28 | **Memory Poisoning** | Persistent memory poisoning and the MemScope auditor toy | 🟢 <a href="https://www2027.thewebconf.org/demos/" target="_blank" rel="noopener noreferrer">WWW demo track</a> |
| 29 | **Provenance Graphs** | Tamper-evident provenance for post-incident reconstruction | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> |
| 30 | **Default Configs** | Insecure defaults in self-hosted LLM stacks | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> |
| 31 | **Declaration Gap** | MCP registry declared-versus-exercised authority in agent integrations | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 32 | **Reproducibility Audit** | Artefact audit of the agent-security literature | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2 SoK</a> |
| 33 | **Protocol Coverage** | Agent protocol element × threat coverage map | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2 SoK</a> |
| 34 | **Visual Injection** | Typographic injection against vision-language agents | 🟢 <a href="https://cvpr.thecvf.com/Conferences/2027/CallForPapers" target="_blank" rel="noopener noreferrer">CVPR</a> |
| 35 | **Scaling Meta-regression** | Agent misbehaviour versus scale across benchmarks | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 36 | **Card Debt** | Documentation debt across open model cards | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> |
| 37 | **Detector Cost** | Injection-detector comparison with false-positive cost | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 38 | **Assurance Claims** | System-card assurance claims versus obligations | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 39 | **Incident Taxonomy** | Agentic-AI threat taxonomy for practitioners | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 40 | **Corpus Union** | License-audited unified agentic-security corpus | 🔵 <a href="https://www.nature.com/sdata/" target="_blank" rel="noopener noreferrer">Scientific Data</a> |
| 41 | **Ten Invariants** | Security invariants checklist synthesis | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 42 | **Patch Lifecycle** | Vulnerability lifecycle and patch adoption lag | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a> |
| 43 | **Terms Coding** | Accountability in platform terms; confirmation steps missing from state-altering tool schemas | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> |
| 44 | **Toolflow Taint** | Cross-tool dataflow integrity tracking | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> |
| 45 | **Exact Nulls for Localisation Claims** | Exact nulls for localisation claims; code in the private `demo-45-localisation-nulls` repo | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 46 | **Embedding-swap Cosine Shift** | `1 − cosine` shift against the frozen mean 0.1222; code in the private `demo-46-simulated-embedding-drift-aibom` repo | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a> |
| 47 | **Pre-reveal Seal** | Pre-reveal hash of a localisation commitment; code in the private `demo-47-blind-verification-eval-sais` repo | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 48 | **OAuth Over-privilege** | OAuth scope over-privilege and scope creep; code in the private `demo-48-scope-creep-oauth-overprivilege-tops` repo | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 49 | **Tier Fallback** | Authority invariance when an orchestrator changes model tier mid-task | 🟡 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF Winter</a> |
| 50 | **Budget Delegation** | Token and cost budgets conserved across a multi-agent delegation tree | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a> |
| 51 | **Guardrail Equity** | Accessibility-related false-positive disparity in input guardrails | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 52 | **Simulation V&V** | Held-out and contamination-probe checks for toy cohort simulators | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a> |
| 53 | **Human Validation** | Sampled validation of agent outputs with planted errors | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 54 | **Stress Transfer** | A detector that passes in-distribution stress items fails under shift | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 55 | **Scaffolding Retention** | Analytic power for an immediate versus residual two-arm contrast | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 56 | **Learning Meta-analysis** | Inverse-variance fixed-effect summary of synthetic study rows | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a> |
| 57 | **Governance Corpus** | Codebook validation and rater agreement on synthetic HE policy excerpts | 🔵 <a href="https://cscw.acm.org/rolling.html" target="_blank" rel="noopener noreferrer">CSCW</a> |
| 58 | **Work Exposure** | Task-level exposure and an agentic-action share for synthetic HE roles | 🟡 <a href="https://2027.ijcai.org/" target="_blank" rel="noopener noreferrer">IJCAI</a> |
| 59 | **Foresight Delphi** | Median, IQR and consensus on synthetic ratings bound to a briefing hash | 🔵 <a href="https://www.sciencedirect.com/journal/technological-forecasting-and-social-change" target="_blank" rel="noopener noreferrer">Technological Forecasting &amp; Social Change</a> |
| 60 | **EngBio Battery** | Score three synthetic analysis tasks against predeclared references | 🟡 <a href="https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/" target="_blank" rel="noopener noreferrer">IJCAI</a> |
| 61 | **Re-execution Checks** | Re-execution and number-provenance checks of agent-written analyses | 🟡 <a href="https://icml.cc/Conferences/2027/CallForPapers" target="_blank" rel="noopener noreferrer">ICML 2027</a> |
| 62 | **LLM Learner Policy** | Schema adherence, persona sensitivity and calibration of an LLM learner policy against baselines | 🟡 <a href="https://educationaldatamining.org/edm2027/call-for-papers/" target="_blank" rel="noopener noreferrer">EDM 2027</a> |
| 63 | **Policy-Coding Reliability** | How reliably two model families code public institutional AI policies across two archive waves | 🔵 <a href="https://link.springer.com/journal/11948" target="_blank" rel="noopener noreferrer">Science and Engineering Ethics</a> |
| 64 | **Socratic Answer Guard** | Calibration of an answer guard on scripted adversarial learner dialogues | 🟡 <a href="https://aied-conference.org/2027/call-for-papers/main-track" target="_blank" rel="noopener noreferrer">AIED 2027</a> |
| 65 | **Security–Education Bibliometrics** | Registered bibliometric screen of UK agentic-security and AI-education co-authorship, 2023–2026 | 🟡 <a href="https://issi2027.ntu.edu.tw/submission-guidelines" target="_blank" rel="noopener noreferrer">ISSI 2027</a> |
| 66 | **QPU Budget Arms** | Accepted results per simulated QPU-second across three workflow arms | 🟠 <a href="https://isc-hpc.com/submissions/research-paper/" target="_blank" rel="noopener noreferrer">ISC 2027</a> |
| 67 | **Multi-Table Memorisation Probe** | Row and cross-table completion against a remapped-table null | 🟠 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 3</a> |
| 68 | **Identifier Filter** | Span recall, residue and k = 1 re-identification after redaction | 🟠 <a href="https://www.petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 3</a> |
| 69 | **Grounded Terms Extraction** | Verbatim-quote grounding and value consistency for extracted contract terms | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a> |
| 70 | **SoD Conflicts** | Deterministic detection of mutually exclusive permission pairs in effective RBAC assignments | 🔵 <a href="https://computersandsecurity.org/aims-and-scope/" target="_blank" rel="noopener noreferrer">Computers & Security</a> |
| 71 | **Feature-Erasure Search** | Complete heuristic search for the cheapest feature erasures that flip a linear score | 🔵 <a href="https://cis.ieee.org/publications/ieee-transactions-on-artificial-intelligence/information-for-authors-tai" target="_blank" rel="noopener noreferrer">IEEE TAI</a> |
| 72 | **Control Mapping** | Set-based alignment of public technique catalogues to public control catalogues | 🔵 <a href="https://dl.acm.org/journal/tist/author-guidelines" target="_blank" rel="noopener noreferrer">ACM TIST</a> |
| 73 | **Open-Set NCM** | Nearest-class-mean classification with a distance threshold that can reject unknowns | 🔵 <a href="https://shop.elsevier.com/journals/pattern-recognition/0031-3203" target="_blank" rel="noopener noreferrer">Pattern Recognition</a> |
| 74 | **Lipschitz Bound** | Exact two-by-two spectral norms and the product Lipschitz bound of a two-layer linear map | 🔵 <a href="https://cis.ieee.org/publications/t-neural-networks-and-learning-systems/tnnls" target="_blank" rel="noopener noreferrer">IEEE TNNLS</a> |
| 75 | **Advisory Linkage** | Exact-identifier linkage of public advisories and measurement of severity-string disagreement | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=69" target="_blank" rel="noopener noreferrer">IEEE TKDE</a> |
| 76 | **Patrol Search** | Exhaustive and greedy search for a k-node patrol set that covers attacker paths | 🔵 <a href="https://www.jair.org/index.php/jair/about" target="_blank" rel="noopener noreferrer">JAIR</a> |
| 77 | **Horn Repair** | Smallest clause-deletion set that stops forward chaining from deriving false | 🔵 <a href="https://aij.ijcai.org/call-for-papers/" target="_blank" rel="noopener noreferrer">AIJ</a> |
| 78 | **Sequential Covering** | Greedy sequential covering that learns an ordered list of single-feature rules | 🔵 <a href="https://aaai.org/conference/aaai/" target="_blank" rel="noopener noreferrer">AAAI 2028</a> |
| 79 | **Contrast Sets** | Item support in two windows and the growth rate that marks an emerging contrast set | 🟡 <a href="https://kdd2027.kdd.org/research-track-call-for-papers/" target="_blank" rel="noopener noreferrer">KDD 2027 C2</a> |
| 80 | **SoK: Injection Defences** | Systematised review of indirect prompt-injection defences, double-coded | 🔵 <a href="https://dl.acm.org/journal/csur" target="_blank" rel="noopener noreferrer">ACM CSUR</a> |
| 81 | **The Agent-Security Benchmark** | Frozen gates, pinned corpora and registered falsification as a re-runnable benchmark | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 E&D</a> |
| 82 | **Guardrail Score Transfer** | Whether guardrail benchmark scores predict tool-attack behaviour | 🔵 <a href="https://aclrollingreview.org/" target="_blank" rel="noopener noreferrer">EMNLP 2027 (ARR)</a> |
| 83 | **MCP Registry Census** | Description-injection and authorisation gaps across MCP manifests, two snapshots | 🟡 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS 2027 C1</a> |
| 84 | **Longitudinal Security Drift** | Ten-framework, multi-release census of security-relevant surface drift | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a> |
| 85 | **The Enforcement Matrix** | Whether provenance labels are enforced at the sink, by framework and mode | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a> |
| 86 | **Personal-Data Exposure Census** | Personal-data shapes in agent tool arguments, by tool class and sink | 🟠 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 3</a> |
| 87 | **The Skill-Plugin Supply Chain** | Declared versus extractable tool capability per marketplace skill | 🟡 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS 2027 C1</a><br>🟡 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">~mid-Jan 2027 (call unpublished)</a> |
| 88 | **Detection Benchmark: Injected Actions** | A labelled injected-action detection benchmark with baseline detectors and per-stratum metrics | 🔵 <a href="https://raid2027.org/" target="_blank" rel="noopener noreferrer">RAID 2027</a> |
| 89 | **Tool-Schema Interpretation Divergence** | Where frameworks interpret the same tool schema differently | 🔵 <a href="https://conf.researchr.org/track/icse-2028/icse-2028-papers" target="_blank" rel="noopener noreferrer">ICSE 2028</a> |
| 90 | **The Unread Manual** | Whether coding agents read the repository guidance they can see | 🟡 <a href="https://link.springer.com/journal/10664" target="_blank" rel="noopener noreferrer">EMSE</a> |
| 91 | **Tutor Feedback Fidelity** | LLM-generated tutor replies against authentic tutor replies on OULAD forum threads: moves, personalisation, safety | 🔵 <a href="https://www.sciencedirect.com/journal/computers-and-education-artificial-intelligence" target="_blank" rel="noopener noreferrer">Computers &amp; Education: AI</a> |
| 92 | **Adversarial Testimony** | Epistemic trust and deference for agent reports whose information channels can be corrupted | 🔵 <a href="https://link.springer.com/journal/11023" target="_blank" rel="noopener noreferrer">Minds and Machines</a> |
| 93 | **Pipeline Reliability** | Failure-mode taxonomy, hazard rates and Bayesian fault trees from public execution traces | 🔵 <a href="https://www.sciencedirect.com/journal/reliability-engineering-and-system-safety" target="_blank" rel="noopener noreferrer">Reliability Eng. &amp; System Safety</a> |

Each demo is self-contained and reproducible. Its README has a **How it works** section: a procedure figure, a step-by-step list mapped to files, and a worked example from the demo's own output. Figures rebuild with `python3 tools/figures/build.py` (see `tools/figures/README.md`). Each demo also has:

- 📦 Frozen dependencies and environment specs
- 📊 Pre-computed evidence (JSON)
- 🧪 Test suites (≥90% coverage)
- 📄 Claim ledgers and venue notes
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

# Run one demo's suite (folders demo-01 … demo-93)
make test DEMO=01
```

---

## 🚀 Quick Start

All demos run offline from the repository root — no API keys, no network.
Each demo folder also has step-by-step `INSTRUCTIONS.md` with expected outputs.

```bash
# Run a teaching demo (folders demo-01 … demo-93)
make demo DEMO=01   # Blind Verification
make demo DEMO=04   # Prompt Injection & Tool Authority
make demo DEMO=07   # Malware Triage
make demo DEMO=90   # The Unread Manual

# Run a demo's test suite
make test DEMO=01

# Run every demo sequentially
make all-demos

# Check offline-safety constraints (no network imports, no credentials)
make verify-safety
```

All demos follow the same pattern: replace `DEMO=01` with any folder number.

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

> Venue names link to the venue; dates link to the call or portal.

| Demo | Option A | Option B | Option C |
|:---:|---|---|---|
| 01 | 🟢 <a href="https://dl.acm.org/journal/tosem" target="_blank" rel="noopener noreferrer">ACM TOSEM</a> | 🔵 <a href="https://link.springer.com/journal/10664" target="_blank" rel="noopener noreferrer">EMSE</a> | 🔵 <a href="https://conf.researchr.org/track/icse-2028/icse-2028-papers" target="_blank" rel="noopener noreferrer">ICSE 2028</a> |
| 02 | 🟢 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32" target="_blank" rel="noopener noreferrer">IEEE TSE</a> | 🔵 <a href="https://www.sciencedirect.com/journal/journal-of-systems-and-software" target="_blank" rel="noopener noreferrer">JSS</a> | 🔵 <a href="https://www.sciencedirect.com/journal/information-and-software-technology" target="_blank" rel="noopener noreferrer">IST</a> |
| 03 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/" target="_blank" rel="noopener noreferrer">JMLR</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 04 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://www.ieee-security.org/TC/SP-Index.html" target="_blank" rel="noopener noreferrer">IEEE S&P 2028 (call unpublished)</a> |
| 05 | 🟢 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://www.usenix.org/conference/usenixsecurity28" target="_blank" rel="noopener noreferrer">USENIX Sec 2028 (call unpublished)</a> | 🔵 <a href="https://www.acsac.org/" target="_blank" rel="noopener noreferrer">ACSAC 2027 (call unpublished)</a> |
| 06 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://www.usenix.org/conference/usenixsecurity28" target="_blank" rel="noopener noreferrer">USENIX Sec 2028 (call unpublished)</a> |
| 07 | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> | 🔵 <a href="https://raid2027.org/" target="_blank" rel="noopener noreferrer">RAID 2027 (call unpublished)</a> | 🔵 <a href="https://www.acsac.org/" target="_blank" rel="noopener noreferrer">ACSAC 2027 (call unpublished)</a> |
| 08 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://conf.laas.fr/esorics" target="_blank" rel="noopener noreferrer">ESORICS C2</a> | 🔵 <a href="https://raid2027.org/" target="_blank" rel="noopener noreferrer">RAID</a> |
| 09 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=90" target="_blank" rel="noopener noreferrer">IEEE/ACM ToN</a> | 🔵 <a href="https://www.dsn.org/" target="_blank" rel="noopener noreferrer">DSN 2028 (call unpublished)</a> |
| 10 | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS</a> | 🔵 <a href="https://www.ieee-security.org/TC/SP-Index.html" target="_blank" rel="noopener noreferrer">IEEE S&P 2028 (call unpublished)</a> |
| 11 | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> | 🔵 <a href="https://raid2027.org/" target="_blank" rel="noopener noreferrer">RAID 2027 (call unpublished)</a> | 🔵 <a href="https://conf.laas.fr/esorics" target="_blank" rel="noopener noreferrer">ESORICS</a> |
| 12 | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> | 🔵 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS</a> | 🔵 <a href="https://www.ndss-symposium.org/" target="_blank" rel="noopener noreferrer">NDSS</a> |
| 13 | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> | 🔵 <a href="https://satml.org/" target="_blank" rel="noopener noreferrer">SaTML 2028 (call unpublished)</a> | 🔵 <a href="https://aaai.org/conference/aaai/" target="_blank" rel="noopener noreferrer">AAAI-28 (call unpublished)</a> |
| 14 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=24" target="_blank" rel="noopener noreferrer">IEEE Trans. Reliability</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 (call unpublished)</a> |
| 15 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://iclr.cc/" target="_blank" rel="noopener noreferrer">ICLR 2028 (call unpublished)</a> |
| 16 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://www.ifaamas.org/" target="_blank" rel="noopener noreferrer">AAMAS 2028 (call unpublished)</a> | 🔵 <a href="https://link.springer.com/journal/10458" target="_blank" rel="noopener noreferrer">JAAMAS</a> |
| 17 | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> | 🔵 <a href="https://dl.acm.org/journal/tosem" target="_blank" rel="noopener noreferrer">ACM TOSEM</a> | 🔵 <a href="https://www.ifaamas.org/" target="_blank" rel="noopener noreferrer">AAMAS 2028 (call unpublished)</a> |
| 18 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://aclrollingreview.org/" target="_blank" rel="noopener noreferrer">ACL (ARR)</a> | 🔵 <a href="https://aclanthology.org/venues/emnlp/" target="_blank" rel="noopener noreferrer">EMNLP</a> |
| 19 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://conf.researchr.org/track/icse-2028/icse-2028-papers" target="_blank" rel="noopener noreferrer">ICSE 2028</a><br>🔵 <a href="https://conf.researchr.org/track/icse-2028/icse-2028-papers" target="_blank" rel="noopener noreferrer">abs 24 Jun · papers 1 Jul 2027</a> | 🔵 <a href="https://www.esec-fse.org/" target="_blank" rel="noopener noreferrer">FSE</a> |
| 20 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://conferences.sigcomm.org/imc/2027/" target="_blank" rel="noopener noreferrer">IMC 2027 C2</a><br>🔵 <a href="https://conferences.sigcomm.org/imc/2027/" target="_blank" rel="noopener noreferrer">abs 31 Mar · papers 7 Apr 2027</a> | 🔵 <a href="https://dl.acm.org/journal/tweb" target="_blank" rel="noopener noreferrer">ACM TWEB</a> |
| 21 | 🟢 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">DSN 2027</a> | 🔵 <a href="https://conferences.sigcomm.org/imc/" target="_blank" rel="noopener noreferrer">IMC</a> | 🔵 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS</a> |
| 22 | 🟠 <a href="https://petsymposium.org/2027" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 3</a><br>🟠 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">Issue 3: 30 Nov</a> | 🟡 <a href="https://petsymposium.org/2027" target="_blank" rel="noopener noreferrer">PoPETs Issue 4</a><br>🟡 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">28 Feb (Quick/Desk Reject only)</a> | 🔵 <a href="https://www.ieee-security.org/TC/SP-Index.html" target="_blank" rel="noopener noreferrer">IEEE S&P 2028 (call unpublished)</a> |
| 23 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=24" target="_blank" rel="noopener noreferrer">IEEE Trans. Reliability</a> | 🔵 <a href="https://conf.researchr.org/home/ase-2027" target="_blank" rel="noopener noreferrer">ASE 2027 (call unpublished)</a> |
| 24 | 🟡 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF Winter</a><br>🟡 <a href="https://csf2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">papers 28 Jan</a> | 🔵 <a href="https://conf.laas.fr/esorics" target="_blank" rel="noopener noreferrer">ESORICS 2027 C2 (call unpublished)</a> | 🔵 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF 2028 (call unpublished)</a> |
| 25 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/tosem" target="_blank" rel="noopener noreferrer">ACM TOSEM</a> | 🔵 <a href="https://conf.researchr.org/track/icse-2028/icse-2028-papers" target="_blank" rel="noopener noreferrer">ICSE 2028</a> |
| 26 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://www.acsac.org/" target="_blank" rel="noopener noreferrer">ACSAC 2027 (call unpublished)</a> |
| 27 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://www.blackhat.com/" target="_blank" rel="noopener noreferrer">Black Hat / Arsenal</a> | 🔵 <a href="https://www.defcon.org/" target="_blank" rel="noopener noreferrer">DEF CON Demo Labs</a> |
| 28 | 🟢 <a href="https://www2027.thewebconf.org/demos/" target="_blank" rel="noopener noreferrer">WWW demo track</a> | 🔵 <a href="https://www.defcon.org/" target="_blank" rel="noopener noreferrer">DEF CON</a><br>🔵 <a href="https://www.defcon.org/" target="_blank" rel="noopener noreferrer">~1 May 2027</a> | 🔵 <a href="https://www.blackhat.com/" target="_blank" rel="noopener noreferrer">Black Hat Arsenal</a> |
| 29 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10206" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> | 🔵 <a href="https://www.sciencedirect.com/journal/forensic-science-international-digital-investigation" target="_blank" rel="noopener noreferrer">FSI: Digital Investigation</a> |
| 30 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS 2028 (call unpublished)</a> |
| 31 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🔵 <a href="https://petsymposium.org/" target="_blank" rel="noopener noreferrer">PoPETs 2028 (call unpublished)</a> | 🔵 <a href="https://www.iw3c2.org/" target="_blank" rel="noopener noreferrer">WWW 2028 (call unpublished)</a> |
| 32 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2 SoK</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/csur" target="_blank" rel="noopener noreferrer">ACM CSUR</a> | 🔵 <a href="https://www.comsoc.org/publications/journals/ieee-comst" target="_blank" rel="noopener noreferrer">IEEE COMST</a> |
| 33 | 🟢 <a href="https://sp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">IEEE S&P C2 SoK</a> | 🔵 <a href="https://www.comsoc.org/publications/journals/ieee-comst" target="_blank" rel="noopener noreferrer">IEEE COMST</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=5" target="_blank" rel="noopener noreferrer">Proc. IEEE</a> |
| 34 | 🟢 <a href="https://cvpr.thecvf.com/Conferences/2027/CallForPapers" target="_blank" rel="noopener noreferrer">CVPR</a> | 🔵 <a href="https://www.computer.org/csdl/journal/tp" target="_blank" rel="noopener noreferrer">IEEE TPAMI</a> | 🔵 <a href="https://iccv.thecvf.com/" target="_blank" rel="noopener noreferrer">ICCV 2027 (call unpublished)</a> |
| 35 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://jmlr.org/" target="_blank" rel="noopener noreferrer">JMLR</a> |
| 36 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://www.nature.com/natmachintell/" target="_blank" rel="noopener noreferrer">Nature MI</a> | 🔵 <a href="https://www.cell.com/patterns" target="_blank" rel="noopener noreferrer">Patterns</a> |
| 37 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10206" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> | 🔵 <a href="https://satml.org/" target="_blank" rel="noopener noreferrer">SaTML 2028 (call unpublished)</a> |
| 38 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🔵 <a href="https://academic.oup.com/cybersecurity" target="_blank" rel="noopener noreferrer">J. Cybersecurity</a> | 🔵 <a href="https://dl.acm.org/journal/jrc" target="_blank" rel="noopener noreferrer">ACM JRC</a> |
| 39 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🔵 <a href="https://www.computer.org/csdl/magazine/sp" target="_blank" rel="noopener noreferrer">S&P Magazine</a> | 🔵 <a href="https://cacm.acm.org/" target="_blank" rel="noopener noreferrer">CACM Practice</a> |
| 40 | 🔵 <a href="https://www.nature.com/sdata/" target="_blank" rel="noopener noreferrer">Scientific Data</a> | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 D&B (call unpublished)</a> | 🔵 <a href="https://data.mlr.press/" target="_blank" rel="noopener noreferrer">DMLR</a> |
| 41 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://cacm.acm.org/" target="_blank" rel="noopener noreferrer">CACM</a> | 🔵 <a href="https://www.computer.org/csdl/magazine/sp" target="_blank" rel="noopener noreferrer">S&P Magazine</a> |
| 42 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://link.springer.com/journal/10664" target="_blank" rel="noopener noreferrer">EMSE</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32" target="_blank" rel="noopener noreferrer">IEEE TSE</a> |
| 43 | 🟢 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW</a> | 🔵 <a href="https://www.aies-conference.com/" target="_blank" rel="noopener noreferrer">AIES</a> | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> |
| 44 | 🟢 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P</a> | 🔵 <a href="https://www.ndss-symposium.org/" target="_blank" rel="noopener noreferrer">NDSS (next cycle)</a> | 🔵 <a href="https://dl.acm.org/journal/tosem" target="_blank" rel="noopener noreferrer">ACM TOSEM</a> |
| 45 | 🟢 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT</a> | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://link.springer.com/journal/10664" target="_blank" rel="noopener noreferrer">EMSE</a> |
| 46 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://www.dsn.org/" target="_blank" rel="noopener noreferrer">DSN 2028 (call unpublished)</a> | 🔵 <a href="https://dl.acm.org/journal/dtrap" target="_blank" rel="noopener noreferrer">ACM DTRAP</a> |
| 47 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF 2028 (call unpublished)</a> | 🔵 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS 2028 (call unpublished)</a> |
| 48 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://petsymposium.org/" target="_blank" rel="noopener noreferrer">PoPETs 2028 (call unpublished)</a> |
| 49 | 🟡 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF Winter</a><br>🟡 <a href="https://csf2027.ieee-security.org/cfp.html" target="_blank" rel="noopener noreferrer">papers 28 Jan</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://csf2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">CSF 2028 (call unpublished)</a> |
| 50 | 🟠 <a href="https://asiaccs2027.cityu.edu.mo/" target="_blank" rel="noopener noreferrer">AsiaCCS R2</a><br>🟠 <a href="https://asiaccs2027.cityu.edu.mo/call-for-papers/index.html" target="_blank" rel="noopener noreferrer">papers 11 Dec</a> | 🔵 <a href="https://dl.acm.org/journal/dtrap" target="_blank" rel="noopener noreferrer">ACM DTRAP</a> | 🔵 <a href="https://aaai.org/conference/aaai/" target="_blank" rel="noopener noreferrer">AAAI-28 (call unpublished)</a> |
| 51 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://www.aies-conference.com/" target="_blank" rel="noopener noreferrer">AIES 2027 (call unpublished)</a> | 🔵 <a href="https://chi.acm.org/" target="_blank" rel="noopener noreferrer">CHI 2028 (call unpublished)</a> |
| 52 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=24" target="_blank" rel="noopener noreferrer">IEEE Trans. Reliability</a> | 🔵 <a href="https://www.ifaamas.org/" target="_blank" rel="noopener noreferrer">AAMAS 2028 (call unpublished)</a> |
| 53 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://aistats.org/" target="_blank" rel="noopener noreferrer">AISTATS 2028 (call unpublished)</a> | 🔵 <a href="https://www.nature.com/natmachintell/" target="_blank" rel="noopener noreferrer">Nature MI</a> |
| 54 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://satml.org/" target="_blank" rel="noopener noreferrer">SaTML 2028 (call unpublished)</a> |
| 55 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://www.sciencedirect.com/journal/computers-and-education" target="_blank" rel="noopener noreferrer">Computers & Education</a> | 🔵 <a href="https://link.springer.com/journal/40593" target="_blank" rel="noopener noreferrer">IJAIED</a> |
| 56 | 🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">ICML</a><br>🟡 <a href="https://icml.cc/" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://www.sciencedirect.com/journal/educational-research-review" target="_blank" rel="noopener noreferrer">Educational Research Review</a> | 🔵 <a href="https://bera-journals.onlinelibrary.wiley.com/journal/14678535" target="_blank" rel="noopener noreferrer">BJET</a> |
| 57 | 🔵 <a href="https://cscw.acm.org/rolling.html" target="_blank" rel="noopener noreferrer">CSCW</a> | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT 2028 (call unpublished)</a> | 🔵 <a href="https://chi.acm.org/" target="_blank" rel="noopener noreferrer">CHI 2028 (call unpublished)</a> |
| 58 | 🟡 <a href="https://2027.ijcai.org/" target="_blank" rel="noopener noreferrer">IJCAI</a><br>🟡 <a href="https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/" target="_blank" rel="noopener noreferrer">abs 4 Jan · papers 11 Jan</a> | 🔵 <a href="https://www.aies-conference.com/" target="_blank" rel="noopener noreferrer">AIES 2027 (call unpublished)</a> | 🔵 <a href="https://cscw.acm.org/rolling.html" target="_blank" rel="noopener noreferrer">ACM CSCW rolling</a> |
| 59 | 🔵 <a href="https://www.sciencedirect.com/journal/technological-forecasting-and-social-change" target="_blank" rel="noopener noreferrer">Technological Forecasting &amp; Social Change</a> | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT 2028 (call unpublished)</a> | 🔵 <a href="https://cscw.acm.org/rolling.html" target="_blank" rel="noopener noreferrer">CSCW</a> |
| 60 | 🟡 <a href="https://2027.ijcai.org/" target="_blank" rel="noopener noreferrer">IJCAI</a><br>🟡 <a href="https://2027.ijcai.org/ijcai-2027-call-for-papers-main-track/" target="_blank" rel="noopener noreferrer">abs 4 Jan · papers 11 Jan</a> | 🔵 <a href="https://www.nature.com/natmachintell/" target="_blank" rel="noopener noreferrer">Nature MI</a> | 🔵 <a href="https://www.cell.com/patterns" target="_blank" rel="noopener noreferrer">Patterns</a> |
| 61 | 🟡 <a href="https://icml.cc/Conferences/2027/CallForPapers" target="_blank" rel="noopener noreferrer">ICML 2027</a><br>🟡 <a href="https://openreview.net/group?id=ICML.cc/2027/Conference" target="_blank" rel="noopener noreferrer">abs 14 Jan · papers 22 Jan</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> | 🔵 <a href="https://acm-rep.github.io/2027" target="_blank" rel="noopener noreferrer">ACM REP 2028 (call unpublished)</a> |
| 62 | 🟡 <a href="https://educationaldatamining.org/edm2027/call-for-papers/" target="_blank" rel="noopener noreferrer">EDM 2027</a><br>🟡 <a href="https://educationaldatamining.org/edm2027/important-dates/" target="_blank" rel="noopener noreferrer">abs 8 Feb · papers 15 Feb</a> | 🔵 <a href="https://jedm.educationaldatamining.org/index.php/JEDM" target="_blank" rel="noopener noreferrer">JEDM</a> | 🔵 <a href="https://aied-conference.org/" target="_blank" rel="noopener noreferrer">AIED 2028 (call unpublished)</a> |
| 63 | 🔵 <a href="https://link.springer.com/journal/11948" target="_blank" rel="noopener noreferrer">Science and Engineering Ethics</a><br>🔵 rolling | 🟡 <a href="https://aied-conference.org/2027/call-for-papers/main-track" target="_blank" rel="noopener noreferrer">AIED 2027</a><br>🟡 <a href="https://aied-conference.org/2027/important-dates" target="_blank" rel="noopener noreferrer">abs 22 Jan · papers 1 Feb</a> | 🔵 <a href="https://facctconference.org/" target="_blank" rel="noopener noreferrer">FAccT 2028 (call unpublished)</a> |
| 64 | 🟡 <a href="https://aied-conference.org/2027/call-for-papers/main-track" target="_blank" rel="noopener noreferrer">AIED 2027</a><br>🟡 <a href="https://aied-conference.org/2027/important-dates" target="_blank" rel="noopener noreferrer">abs 22 Jan · papers 1 Feb</a> | 🔵 <a href="https://jedm.educationaldatamining.org/index.php/JEDM" target="_blank" rel="noopener noreferrer">JEDM</a> | 🔵 <a href="https://educationaldatamining.org/" target="_blank" rel="noopener noreferrer">EDM 2028 (call unpublished)</a> |
| 65 | 🟡 <a href="https://issi2027.ntu.edu.tw/submission-guidelines" target="_blank" rel="noopener noreferrer">ISSI 2027</a><br>🟡 <a href="https://www.conftool.pro/issi2027/" target="_blank" rel="noopener noreferrer">papers 15 Jan</a> | 🔵 <a href="https://link.springer.com/journal/11192" target="_blank" rel="noopener noreferrer">Scientometrics</a> | 🔵 <a href="https://direct.mit.edu/qss" target="_blank" rel="noopener noreferrer">QSS</a> |
| 66 | 🟠 <a href="https://isc-hpc.com/submissions/research-paper/" target="_blank" rel="noopener noreferrer">ISC 2027</a><br>🟠 <a href="https://isc-hpc.com/submissions/research-paper/" target="_blank" rel="noopener noreferrer">abs 14 Dec · papers 21 Dec</a> | 🔵 <a href="https://qce.quantum.ieee.org/" target="_blank" rel="noopener noreferrer">IEEE QCE 2027 (call unpublished)</a> | 🔵 <a href="https://dl.acm.org/journal/tqc" target="_blank" rel="noopener noreferrer">ACM TQC</a> |
| 67 | 🟠 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 3</a><br>🟠 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">Issue 3: 30 Nov</a> | 🟡 <a href="https://2027.aclweb.org/calls/main/" target="_blank" rel="noopener noreferrer">ACL 2027 (ARR)</a><br>🟡 <a href="https://www.aclweb.org/portal/content/acl-2027-first-call-papers" target="_blank" rel="noopener noreferrer">ARR 4 Jan</a><br>🔵 <a href="https://transacl.org/index.php/tacl" target="_blank" rel="noopener noreferrer">TACL</a> | 🔵 <a href="https://jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">TMLR</a> |
| 68 | 🟠 <a href="https://www.petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 3</a><br>🟠 <a href="https://www.petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">papers 30 Nov</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=4620076" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> |
| 69 | 🟡 <a href="https://www.usenix.org/conference/usenixsecurity27" target="_blank" rel="noopener noreferrer">USENIX Sec C2</a><br>🟡 <a href="https://www.usenix.org/conference/usenixsecurity27/call-for-papers" target="_blank" rel="noopener noreferrer">papers 26 Jan (reg 19 Jan)</a> | 🔵 <a href="https://dl.acm.org/journal/jrc" target="_blank" rel="noopener noreferrer">ACM JRC</a> | 🔵 <a href="https://petsymposium.org/" target="_blank" rel="noopener noreferrer">PoPETs 2028 (call unpublished)</a> |
| 70 | 🔵 <a href="https://computersandsecurity.org/aims-and-scope/" target="_blank" rel="noopener noreferrer">Computers & Security</a><br>🔵 <a href="https://computersandsecurity.org/aims-and-scope/" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://www.sacmat.org/" target="_blank" rel="noopener noreferrer">SACMAT 2027 (call unpublished)</a> | 🔵 <a href="https://www.iospress.com/catalog/journals/journal-of-computer-security" target="_blank" rel="noopener noreferrer">J. Computer Security</a> |
| 71 | 🔵 <a href="https://cis.ieee.org/publications/ieee-transactions-on-artificial-intelligence/information-for-authors-tai" target="_blank" rel="noopener noreferrer">IEEE TAI</a><br>🔵 <a href="https://ieee.atyponrex.com/journal/tai-ieee" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://link.springer.com/journal/10994" target="_blank" rel="noopener noreferrer">Machine Learning (Springer)</a> | 🔵 <a href="https://aistats.org/" target="_blank" rel="noopener noreferrer">AISTATS 2028 (call unpublished)</a> |
| 72 | 🔵 <a href="https://dl.acm.org/journal/tist/author-guidelines" target="_blank" rel="noopener noreferrer">ACM TIST</a><br>🔵 <a href="https://dl.acm.org/journal/tist/author-guidelines" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=69" target="_blank" rel="noopener noreferrer">IEEE TKDE</a> | 🔵 <a href="https://www.ijcai.org/future_conferences" target="_blank" rel="noopener noreferrer">IJCAI 2028 (call unpublished)</a> |
| 73 | 🔵 <a href="https://shop.elsevier.com/journals/pattern-recognition/0031-3203" target="_blank" rel="noopener noreferrer">Pattern Recognition</a><br>🔵 <a href="https://shop.elsevier.com/journals/pattern-recognition/0031-3203" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://www.computer.org/csdl/journal/tp" target="_blank" rel="noopener noreferrer">IEEE TPAMI</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=5962385" target="_blank" rel="noopener noreferrer">IEEE TNNLS</a> |
| 74 | 🔵 <a href="https://cis.ieee.org/publications/t-neural-networks-and-learning-systems/tnnls" target="_blank" rel="noopener noreferrer">IEEE TNNLS</a><br>🔵 <a href="https://ieee.atyponrex.com/journal/tnnls" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://www.sciencedirect.com/journal/neural-networks" target="_blank" rel="noopener noreferrer">Neural Networks</a> | 🔵 <a href="https://link.springer.com/journal/10994" target="_blank" rel="noopener noreferrer">Machine Learning (Springer)</a> |
| 75 | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=69" target="_blank" rel="noopener noreferrer">IEEE TKDE</a><br>🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=69" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://link.springer.com/journal/10618" target="_blank" rel="noopener noreferrer">DAMI</a> | 🔵 <a href="https://dl.acm.org/journal/tkdd" target="_blank" rel="noopener noreferrer">ACM TKDD</a> |
| 76 | 🔵 <a href="https://www.jair.org/index.php/jair/about" target="_blank" rel="noopener noreferrer">JAIR</a><br>🔵 <a href="https://www.jair.org/index.php/jair/about/submissions" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://link.springer.com/journal/10458" target="_blank" rel="noopener noreferrer">JAAMAS</a> | 🔵 <a href="https://www.ijcai.org/" target="_blank" rel="noopener noreferrer">IJCAI 2028 (call unpublished)</a> |
| 77 | 🔵 <a href="https://aij.ijcai.org/call-for-papers/" target="_blank" rel="noopener noreferrer">AIJ</a><br>🔵 <a href="https://aij.ijcai.org/for-authors/" target="_blank" rel="noopener noreferrer">rolling</a> | 🔵 <a href="https://dl.acm.org/journal/tocl" target="_blank" rel="noopener noreferrer">ACM TOCL</a> | 🔵 <a href="https://kr.org/" target="_blank" rel="noopener noreferrer">KR 2028 (call unpublished)</a> |
| 78 | 🔵 <a href="https://aaai.org/conference/aaai/" target="_blank" rel="noopener noreferrer">AAAI 2028 (call unpublished)</a> | 🔵 <a href="https://ecmlpkdd.org/" target="_blank" rel="noopener noreferrer">ECML-PKDD 2028 journal track</a> | 🔵 <a href="https://www.computer.org/csdl/proceedings/icdm" target="_blank" rel="noopener noreferrer">ICDM 2028 (call unpublished)</a> |
| 79 | 🟡 <a href="https://kdd2027.kdd.org/research-track-call-for-papers/" target="_blank" rel="noopener noreferrer">KDD 2027 C2</a><br>🟡 <a href="https://kdd2027.kdd.org/research-track-call-for-papers/" target="_blank" rel="noopener noreferrer">Feb 2027 (date unpublished)</a> | 🔵 <a href="https://www.computer.org/csdl/proceedings/icdm" target="_blank" rel="noopener noreferrer">ICDM 2027 (call unpublished)</a> | 🔵 <a href="https://link.springer.com/journal/10618" target="_blank" rel="noopener noreferrer">DAMI</a> |
| 80 | 🔵 <a href="https://dl.acm.org/journal/csur" target="_blank" rel="noopener noreferrer">ACM CSUR</a><br>🔵 rolling | 🔵 <a href="https://eurosp2027.ieee-security.org/" target="_blank" rel="noopener noreferrer">EuroS&P 2028 SoK (call unpublished)</a> | 🔵 <a href="https://www.comsoc.org/publications/journals/ieee-comst" target="_blank" rel="noopener noreferrer">IEEE COMST</a> |
| 81 | 🔵 <a href="https://neurips.cc/" target="_blank" rel="noopener noreferrer">NeurIPS 2027 E&D</a><br>🔵 May 2027 (call unpublished) | 🔵 <a href="https://iclr.cc/" target="_blank" rel="noopener noreferrer">ICLR 2028 (call unpublished)</a> | 🔵 <a href="https://data.mlr.press/" target="_blank" rel="noopener noreferrer">DMLR</a> |
| 82 | 🔵 <a href="https://aclrollingreview.org/" target="_blank" rel="noopener noreferrer">EMNLP 2027 (ARR)</a><br>🔵 ~May 2027 (call unpublished) | 🔵 <a href="https://aclrollingreview.org/" target="_blank" rel="noopener noreferrer">ACL 2028 (ARR)</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10206" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> |
| 83 | 🟡 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS 2027 C1</a><br>🟡 ~mid-Jan 2027 (call unpublished) | 🔵 <a href="https://www.ndss-symposium.org/" target="_blank" rel="noopener noreferrer">NDSS 2028 summer (call unpublished)</a> | 🔵 <a href="https://www2027.thewebconf.org/" target="_blank" rel="noopener noreferrer">WWW 2028 (call unpublished)</a> |
| 84 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10206" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32" target="_blank" rel="noopener noreferrer">IEEE TSE</a> |
| 85 | 🟠 <a href="https://dsn2027-berlin.github.io/" target="_blank" rel="noopener noreferrer">DSN 2027</a><br>🟠 <a href="https://dsn2027-berlin.github.io/call-for-contributions/" target="_blank" rel="noopener noreferrer">abs 25 Nov · papers 2 Dec</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8858" target="_blank" rel="noopener noreferrer">IEEE TDSC</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> |
| 86 | 🟠 <a href="https://petsymposium.org/cfp27.php" target="_blank" rel="noopener noreferrer">PoPETs 2027 Issue 3</a><br>🟠 papers 30 Nov 2026 | 🔵 <a href="https://www.usenix.org/conference/usenixsecurity28" target="_blank" rel="noopener noreferrer">USENIX Sec 2028 C1 (call unpublished)</a> | 🔵 <a href="https://dl.acm.org/journal/tops" target="_blank" rel="noopener noreferrer">ACM TOPS</a> |
| 87 | 🟡 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">CCS 2027 C1</a><br>🟡 <a href="https://www.sigsac.org/ccs/CCS2027/" target="_blank" rel="noopener noreferrer">~mid-Jan 2027 (call unpublished)</a> | 🔵 <a href="https://conf.researchr.org/home/ase-2027" target="_blank" rel="noopener noreferrer">ASE 2027 (call unpublished)</a> | 🔵 <a href="https://www.ndss-symposium.org/" target="_blank" rel="noopener noreferrer">NDSS 2028 fall (call unpublished)</a> |
| 88 | 🔵 <a href="https://raid2027.org/" target="_blank" rel="noopener noreferrer">RAID 2027</a><br>🔵 ~Apr 2027 (call unpublished) | 🔵 <a href="https://aaai.org/" target="_blank" rel="noopener noreferrer">AAAI-28 (call unpublished)</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10206" target="_blank" rel="noopener noreferrer">IEEE TIFS</a> |
| 89 | 🔵 <a href="https://conf.researchr.org/track/icse-2028/icse-2028-papers" target="_blank" rel="noopener noreferrer">ICSE 2028</a><br>🔵 abs 24 Jun · papers 1 Jul 2027 | 🔵 <a href="https://dl.acm.org/journal/tosem" target="_blank" rel="noopener noreferrer">ACM TOSEM</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32" target="_blank" rel="noopener noreferrer">IEEE TSE</a> |
| 90 | 🟡 <a href="https://link.springer.com/journal/10664" target="_blank" rel="noopener noreferrer">EMSE</a><br>🟡 rolling | 🔵 <a href="https://www.sciencedirect.com/journal/journal-of-systems-and-software" target="_blank" rel="noopener noreferrer">JSS</a> | 🔵 <a href="https://www.sciencedirect.com/journal/information-and-software-technology" target="_blank" rel="noopener noreferrer">IST</a> |
| 91 | 🔵 <a href="https://www.sciencedirect.com/journal/computers-and-education-artificial-intelligence" target="_blank" rel="noopener noreferrer">Computers &amp; Education: AI</a> | 🔵 <a href="https://link.springer.com/journal/41055" target="_blank" rel="noopener noreferrer">IJETHE</a> | 🔵 <a href="https://link.springer.com/journal/10639" target="_blank" rel="noopener noreferrer">Education &amp; Information Technologies</a> |
| 92 | 🔵 <a href="https://link.springer.com/journal/11023" target="_blank" rel="noopener noreferrer">Minds and Machines</a> | 🔵 <a href="https://link.springer.com/journal/10676" target="_blank" rel="noopener noreferrer">Ethics &amp; Information Technology</a> | 🔵 <a href="https://link.springer.com/journal/13347" target="_blank" rel="noopener noreferrer">Philosophy &amp; Technology</a> |
| 93 | 🔵 <a href="https://www.sciencedirect.com/journal/reliability-engineering-and-system-safety" target="_blank" rel="noopener noreferrer">Reliability Eng. &amp; System Safety</a> | 🔵 <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=11" target="_blank" rel="noopener noreferrer">IEEE Trans. Reliability</a> | 🔵 <a href="https://www.sciencedirect.com/journal/safety-science" target="_blank" rel="noopener noreferrer">Safety Science</a> |
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

See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- 🐛 Reporting vulnerabilities or reproducibility issues
- 💡 Proposing new demos or venues
- 🔀 Submitting pull requests (evidence-backed changes only)
- 🧪 Extending test suites
- 📝 Improving documentation

**Contribution rules:**
1. Claims need frozen evidence packages.
2. Statistical claims need pre-registered analysis plans.
3. New demos target a top-tier venue with a clear scope.
4. Breaking changes go through an RFC.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE). Some demos include third-party components under their own licences (see `DEPENDENCIES.md`).

---

## 🙏 Acknowledgments

Thanks to research compute providers, the GitHub Accelerator, anonymous reviewers, and the agentic AI security community.

---

<p align="center">
  <strong>Offline, reproducible teaching demos for agentic AI security.</strong>
</p>

<p align="center">
  <a href="https://github.com/jedi-master-council/agentic-security-demos/stargazers">⭐ Star</a> •
  <a href="https://github.com/jedi-master-council/agentic-security-demos/fork">🍴 Fork</a> •
  <a href="https://github.com/jedi-master-council/agentic-security-demos/issues">🐛 Report Issue</a> •
  <a href="https://github.com/jedi-master-council/agentic-security-demos/issues">💬 Discuss</a>
</p>