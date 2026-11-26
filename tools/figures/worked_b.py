"""Figure 2 adapters, demos 31-60."""
import json
import math
import os

import plots as P
from worked_a import J, _gb

W = {}


def F(d, name):
    with open(os.path.join(d, "fixtures", name), encoding="utf-8") as fh:
        return json.load(fh)


def reg(n):
    def deco(f):
        W[n] = f
        return f
    return deco


@reg("31")
def _(d):
    r = J(d, "declarations.json")["rows"]
    ids = [x["id"] for x in r]
    fig, (a,) = P.panels(1, height=2.3, titles=["Declared against exercised authority per integration"])
    P.grouped(a, ids, [("declared", [len(x["declared"]) for x in r], "agent"),
                       ("exercised", [len(x["exercised"]) for x in r], "good")], fmt="{:d}", ylabel="scopes")
    return fig, f"{sum(x['gapped'] for x in r)} of {len(r)} integrations declare more authority than they exercise."


@reg("32")
def _(d):
    r = J(d, "sok_audit.json")
    ch = r["by_channel"]
    ks = list(ch)
    fig, (a,) = P.panels(1, height=2.3, titles=["Published defences that reproduce, by channel"])
    P.grouped(a, ks, [("papers", [ch[k]["n"] for k in ks], "env"), ("reproduces", [ch[k]["reproduces"] for k in ks], "good")],
              fmt="{:d}", ylabel="papers")
    return fig, f"{r['code_data']} of {r['total']} papers release code and data; {r['reproduces']} reproduce, none in the multi-agent channel."


@reg("33")
def _(d):
    r = J(d, "coverage.json")
    els = r["covered_ids"] + r["gap_ids"]
    fig, (a,) = P.panels(1, height=1.5, titles=["Protocol elements: known attack without a stated mitigation"])
    P.strip(a, els, [("status", [("covered", "good")] * len(r["covered_ids"]) + [("GAP", "bad")] * len(r["gap_ids"]))])
    return fig, "Discovery and streaming carry known attacks that neither specification mitigates normatively."


@reg("34")
def _(d):
    r = J(d, "visual.json")
    fig, (a,) = P.panels(1, height=2.3, titles=["Region-trust policy on eight rendered images"])
    P.bars(a, ["injections\nacted on (no policy)", "injections\nblocked", "benign\nblocked"],
           [r["baseline_acted"], r["blocked_injections"], r["blocked_benign"]], kinds=["bad", "good", "agent"],
           fmt="{:d}", ylabel="images")
    return fig, "Treating the untrusted region as data blocks all three typographic injections, at the cost of one benign image."


@reg("35")
def _(d):
    rows = F(d, "results.json")["rows"]
    fig, (a,) = P.panels(1, height=2.5, titles=["Unsafe rate against model size, by benchmark"])
    for b, kind, mk in (("A", "adversary", "s"), ("B", "defender", "o")):
        pts = [x for x in rows if x["benchmark"] == b]
        a.scatter([x["params_B"] for x in pts], [x["unsafe_rate"] for x in pts], marker=mk, s=22,
                  facecolor=P.KIND["bad" if b == "A" else "good"][0], edgecolor=P.KIND["bad" if b == "A" else "good"][1], label=f"benchmark {b}")
    a.set_xscale("log"); a.set_xlabel("parameters (billions, log scale)"); a.set_ylabel("unsafe rate"); a.set_ylim(0, 1)
    a.legend(loc="upper left", frameon=False, ncol=2)
    r = J(d, "meta.json")
    P.note(a, 1.1, 0.5, f"benchmark gap {r['bench_gap']:.2f}; size gap {r['scale_gap']:.3f}")
    return fig, "The rate depends on the benchmark, not on size: within each benchmark the points are flat."


@reg("36")
def _(d):
    cards = F(d, "cards.json")["cards"]
    cards = sorted(cards, key=lambda c: -c["downloads"])
    fig, (a,) = P.panels(1, height=2.4, titles=["Cards ranked by downloads; safety section present or missing"])
    P.bars(a, [c["id"] for c in cards], [c["downloads"] / 1000 for c in cards], kinds=[_gb(c["safety"]) for c in cards],
           fmt="{:.0f}", ylabel="downloads (thousands)")
    P.note(a, 6.5, cards[0]["downloads"] / 1000 * 0.9, "hatched = safety section missing")
    return fig, "Missing safety sections cluster in the long tail; whether that makes the download-weighted rate higher depends on the estimator."


@reg("37")
def _(d):
    r = J(d, "detector_cost.json")
    fig, (a, b) = P.panels(2, titles=["Errors", f"Cost (false positive {r['fp_cost']}, miss {r['fn_cost']})"])
    P.grouped(a, ["strict", "lenient"], [("false positives", [r["strict"]["fp"], r["lenient"]["fp"]], "agent"),
                                         ("misses", [r["strict"]["fn"], r["lenient"]["fn"]], "bad")], fmt="{:d}", ylabel="prompts")
    P.bars(b, ["strict", "lenient"], [r["strict"]["cost"], r["lenient"]["cost"]],
           kinds=["good" if r["winner"] == "strict" else "bad", "good" if r["winner"] == "lenient" else "bad"], fmt="{:d}", ylabel="total cost")
    return fig, "Which detector is better depends on what a false alarm costs relative to a miss; recall alone cannot say."


@reg("38")
def _(d):
    c = J(d, "claims.json")["coverage"]
    po = c["per_obligation"]
    fig, (a,) = P.panels(1, height=2.3, titles=[f"Obligations covered across {c['n']} cards"])
    P.bars(a, list(po), list(po.values()), kinds=["bad" if k == c["weakest"] else "good" for k in po], fmt="{:d}", ylabel="cards")
    return fig, f"Third-party assessment is the weakest obligation; only {c['full_coverage']} cards cover all five."


@reg("39")
def _(d):
    t = J(d, "taxonomy.json")["top_pattern"]["counts"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Incident patterns (ten sketches)"])
    P.hbars(a, list(t), list(t.values()), kinds=["bad"] * len(t), fmt="{:d}", xlabel="incidents")
    return fig, "Prompt injection is the most frequent pattern in the toy; the research version double-codes every incident."


@reg("40")
def _(d):
    r = J(d, "corpus.json")
    fig, (a,) = P.panels(1, height=2.3, titles=["From ingested records to a releasable corpus"])
    P.bars(a, ["ingested", "unique (SHA-256)", "releasable"], [r["n_records"], r["n_unique"], r["n_releasable"]],
           kinds=["env", "env", "good"], fmt="{:d}", ylabel="records")
    return fig, "Deduplication removes three cross-source copies and the licence screen withholds two more."


@reg("41")
def _(d):
    e = J(d, "invariants.json")["evaluation"]
    cols = e["holding"] + e["violated"]
    fig, (a,) = P.panels(1, height=1.6, titles=["Ten invariants checked on one synthetic system"])
    P.strip(a, [c.replace("-", "-\n") for c in cols], [("", [("holds", "good")] * len(e["holding"]) + [("✗", "bad")] * len(e["violated"]))])
    return fig, "Seven invariants hold and three fail: provenance does not travel, memory is not gated, and the run cannot be reconstructed."


@reg("42")
def _(d):
    v = F(d, "vulns.json")["vulns"]
    v = sorted(v, key=lambda x: x["adopt_lag_days"])
    fig, (a,) = P.panels(1, height=2.4, titles=["Adoption lag after the fix, per vulnerability"])
    P.bars(a, [x["id"].replace("vuln", "v") for x in v], [x["adopt_lag_days"] for x in v],
           kinds=["bad" if x["blocked_by_pin"] else "env" for x in v], fmt="{:d}", ylabel="days")
    med = J(d, "lifecycle.json")["median_adopt_lag_days"]
    P.threshold(a, med, f"median {med}")
    return fig, "Lags have a long tail; hatched bars are vulnerabilities whose fix a version pin blocked."


@reg("43")
def _(d):
    r = J(d, "confirmation_gap.json")["rows"]
    cons = [x for x in r if x["state_altering"]]
    fig, (a,) = P.panels(1, height=1.5, titles=["State-altering tools: does the input schema offer a confirmation step?"])
    P.strip(a, [x["tool"].replace("_", "_\n") for x in cons], [("confirm", [("yes" if x["confirmation_param"] else "NO", _gb(x["confirmation_param"])) for x in cons])])
    return fig, "Three of eight state-altering tools expose a confirmation parameter that the keyword rule finds; post_tweet's require_approval is missed by the rule itself."


@reg("44")
def _(d):
    f = F(d, "edges.json")["flows"]
    fig, (a,) = P.panels(1, height=1.7, titles=["Tool output flowing into a sensitive sink: provenance label carried?"])
    P.strip(a, [x["id"] for x in f], [("sink", [(x["sink"], "neutral") for x in f]),
                                     ("label", [("yes" if x["provenance"] else "NO", _gb(x["provenance"])) for x in f])])
    return fig, "Five of eight flows reach a sensitive sink with no provenance label, so no guard could decide by origin."


@reg("45")
def _(d):
    r = J(d, "nulls.json")
    rows = r["rows"]
    fig, (a,) = P.panels(1, height=2.4, titles=["Exact hypergeometric p-value per localisation claim"])
    P.bars(a, [x["id"] for x in rows], [-math.log10(x["p_value"]) for x in rows], kinds=[_gb(x["significant_at_0.01"]) for x in rows],
           fmt="{:.1f}", ylabel="−log10 p", thr=-math.log10(r["alpha"]), thr_label=f"α = {r['alpha']}",
           notes=[f"recall {x['recall']}" for x in rows], rotate=20)
    return fig, "Similar recalls can be significant or not depending on pool, defect count and budget; the exact null decides."


@reg("46")
def _(d):
    r = J(d, "drift.json")
    fig, (a,) = P.panels(1, height=2.2, titles=["Cosine shift of two synthetic vectors after the swap"])
    P.bars(a, [c["id"] for c in r["cases"]], [c["cosine_shift"] for c in r["cases"]],
           kinds=["bad" if c["above_frozen_mean"] else "good" for c in r["cases"]], fmt="{:.3f}", ylabel="1 − cosine",
           thr=r["frozen_mean_cosine_shift"], thr_label=f"study mean {r['frozen_mean_cosine_shift']}")
    return fig, "A small rotation stays under the simulated study's mean shift; an orthogonal swap is far above it."


@reg("47")
def _(d):
    r = J(d, "seals.json")
    fig, (a,) = P.panels(1, height=1.5, titles=["Sealed guesses opened against the answer key"])
    P.strip(a, [x["id"] for x in r], [("verdict", [(x["verdict"].replace("commitment_hash_mismatch", "TAMPERED"),
                                                     "good" if x["verdict"] == "hit" else "neutral" if x["verdict"] == "miss" else "bad") for x in r])])
    return fig, "An edit after sealing is caught as a hash mismatch, whatever the edited guess says."


@reg("48")
def _(d):
    r = J(d, "scopes.json")["rows"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Requested against used scopes per integration"])
    P.grouped(a, [x["id"] for x in r], [("requested", [len(x["requested"]) for x in r], "agent"),
                                        ("used", [len(x["used"]) for x in r], "good")], fmt="{:d}", ylabel="scopes")
    return fig, f"{sum(x['overprivileged'] for x in r)} of {len(r)} integrations request more scopes than they use."


@reg("49")
def _(d):
    r = J(d, "tier_invariance.json")
    rules = ["R1", "R2", "R3"]
    fig, (a,) = P.panels(1, height=1.8, titles=["Traces across a model-tier switch: rule violations"])
    P.strip(a, [x["trace"].replace("_", "\n") for x in r],
            [(rl, [("✗" if any(v["rule"] == rl for v in x["violations"]) else "ok",
                    "bad" if any(v["rule"] == rl for v in x["violations"]) else "good") for x in r]) for rl in rules])
    return fig, "Each failure mode breaks exactly one rule: a tier-dependent decision, a stale plan step, or an unmediated action."


@reg("50")
def _(d):
    r = J(d, "delegation_budget.json")
    fig, (a,) = P.panels(1, height=2.4, titles=["Requested and admitted spend per delegation plan"])
    P.grouped(a, [x["plan"].replace("_", "\n", 1) for x in r],
              [("requested", [x["requested_spend"] / 1000 for x in r], "agent"), ("spent", [x["total_spent"] / 1000 for x in r], "good")],
              fmt="{:.1f}", ylabel="spend (thousands of units)", thr=r[0]["root_budget"] / 1000, thr_label="root budget")
    return fig, "The ledger denies every grant or spend that would break conservation, so no plan exceeds the root budget."


@reg("51")
def _(d):
    v = J(d, "guardrail_equity.json")["variants"]
    ks = list(v)
    fig, (a,) = P.panels(1, height=2.4, titles=["False-positive rate on benign text by surface form"])
    P.bars(a, [k.replace("_", "\n") for k in ks], [v[k]["fpr"] for k in ks], kinds=["good" if v[k]["fpr"] == 0 else "bad" for k in ks],
           fmt="{:.2f}", ylabel="benign text blocked", ylim=(0, 1))
    return fig, "The same benign requests are refused far more often once written as a transcript, with variant spelling or telegraphically."


@reg("52")
def _(d):
    r = J(d, "sim_validation.json")
    ks = list(r)
    fig, (a,) = P.panels(1, height=2.3, titles=["Held-out error of two simulators, and the contamination probe"])
    P.bars(a, ks, [r[k]["heldout"]["pass_mae"] for k in ks], kinds=["bad" if r[k]["probe"]["failed_to_transfer"] else "good" for k in ks],
           fmt="{:.3f}", ylabel="held-out MAE (pass rate)", notes=["probe fails" if r[k]["probe"]["failed_to_transfer"] else "probe passes" for k in ks])
    return fig, "The memorising simulator does worse on held-out years and fails to transfer when the module is renamed."


@reg("53")
def _(d):
    r = J(d, "validation.json")
    fig, (a,) = P.panels(1, height=2.2, titles=["Seeded sample and planted errors"])
    P.bars(a, ["items", "sampled", "planted", "planted found"], [r["n_items"], len(r["sample_ids"]), r["n_planted"], r["coverage"]["planted_in_sample"]],
           kinds=["env", "agent", "bad", "good"], fmt="{:d}", ylabel="items")
    return fig, "Every planted error fell in the sample, so the checker's sensitivity can be stated, not assumed."


@reg("54")
def _(d):
    r = J(d, "transfer.json")
    fig, (a,) = P.panels(1, height=2.3, titles=[f"Detector at threshold {r['threshold']}"])
    P.grouped(a, ["recall", "accuracy"], [("in distribution", [r["in_distribution"]["recall"], r["in_distribution"]["accuracy"]], "good"),
                                          ("shifted", [r["shifted"]["recall"], r["shifted"]["accuracy"]], "bad")], fmt="{:.2f}", ylabel="share", ylim=(0, 1.2))
    return fig, "A detector that is perfect in distribution misses both shifted attacks at the same threshold."


@reg("55")
def _(d):
    p = J(d, "power.json")["power"]
    fig, (a,) = P.panels(1, height=2.3, titles=[f"Power with {p['n_per_arm']} learners per arm"])
    P.bars(a, ["immediate\ndifference", "residual\ndifference"], [p["immediate_power"], p["residual_power"]], kinds=["agent", "bad"],
           fmt="{:.2f}", ylabel="power", ylim=(0, 1), thr=0.8, thr_label="0.8")
    return fig, "The same sample is underpowered for both contrasts, and far more so for the residual one."


@reg("56")
def _(d):
    s = J(d, "meta.json")["summary"]
    fix = F(d, os.listdir(os.path.join(d, "fixtures"))[0])
    rows = fix.get("studies") or fix.get("rows") or []
    fig, (a,) = P.panels(1, height=2.4, titles=["Study effects with 95% intervals, and the fixed-effect mean"])
    for i, r in enumerate(rows):
        se = math.sqrt(r["vi"])
        a.errorbar(r["yi"], i, xerr=1.96 * se, fmt="s", color=P.KIND["env"][1], ms=4, capsize=2, lw=0.8)
    a.errorbar(s["mean"], len(rows), xerr=1.96 * s["se"], fmt="D", color=P.KIND["good"][1], ms=5, capsize=2, lw=1)
    a.set_yticks(range(len(rows) + 1)); a.set_yticklabels([r.get("id", f"s{i+1}") for i, r in enumerate(rows)] + ["pooled"])
    a.axvline(0, color="#555555", lw=0.6); a.set_xlabel("effect size")
    P.note(a, s["mean"] + 0.05, len(rows) - 0.4, f"mean {s['mean']:.2f}, Q = {s['Q']:.2f} on {s['df']} df")
    return fig, "Precise studies pull the pooled mean; Cochran's Q gives no sign that the studies disagree."


@reg("57")
def _(d):
    r = J(d, "coding.json")
    fig, (a,) = P.panels(1, height=2.2, titles=["Two raters on six excerpts"])
    P.bars(a, ["percent agreement", "Cohen's κ"], [r["percent_agreement"], r["kappa"]], kinds=["agent", "bad" if r["kappa"] < 0.6 else "good"],
           fmt="{:.2f}", ylabel="value", ylim=(0, 1), thr=0.6, thr_label="κ floor 0.6")
    return fig, "Two-thirds raw agreement shrinks to a kappa below the floor once chance agreement is removed."


@reg("58")
def _(d):
    r = J(d, "exposure.json")["family_means"]
    fig, (a,) = P.panels(1, height=2.2, titles=["Mean task exposure per work family"])
    P.bars(a, list(r), list(r.values()), kinds=["agent"] * len(r), fmt="{:.2f}", ylabel="mean exposure", ylim=(0, 1))
    return fig, "Learning design is the most exposed family in the toy; exposure says nothing about displacement."


@reg("59")
def _(d):
    r = J(d, "delphi.json")
    fig, (a,) = P.panels(1, height=2.3, titles=["Panel ratings: median and interquartile range"])
    for i, x in enumerate(r):
        k = "good" if x["consensus"] else "bad"
        a.plot([x["q1"], x["q3"]], [i, i], color=P.KIND[k][1], lw=4, solid_capstyle="butt", alpha=0.5)
        a.plot([x["median"]], [i], "D", color=P.KIND[k][1], ms=6)
        a.text(x["q3"] + 0.2, i, f"IQR {x['iqr']} → {'consensus' if x['consensus'] else 'split'}", va="center", fontsize=7)
    a.set_yticks(range(len(r))); a.set_yticklabels([x["id"] for x in r]); a.set_xlim(0, 10); a.set_ylim(-0.6, len(r) - 0.4)
    a.set_xlabel("rating (1–9)")
    return fig, "P1 meets the IQR ≤ 1.5 rule; P2 is split. Both ratings are bound to the same briefing hash."


@reg("60")
def _(d):
    r = J(d, "battery.json")["rows"]
    fig, (a,) = P.panels(1, height=1.5, titles=["Tasks scored against references written before any run"])
    P.strip(a, [x["id"] for x in r], [("result", [("pass" if x["correct"] else "fail", _gb(x["correct"])) for x in r])])
    return fig, "All three synthetic tasks match their predeclared reference answers."
