"""Figure 2 adapters, demos 01-30. Each returns (figure, caption) from the demo's own results."""
import json
import os

import plots as P

W = {}


def J(d, name):
    with open(os.path.join(d, "results", name), encoding="utf-8") as fh:
        return json.load(fh)


def reg(n):
    def deco(f):
        W[n] = f
        return f
    return deco


def _gb(v):
    return "good" if v else "bad"


@reg("01")
def _(d):
    r = J(d, "format_effect.json")
    cfgs = list(r["rows"])
    fig, (a, b) = P.panels(2, widths=[1.6, 1], titles=["File-level hit by output format", "Paired difference"])
    P.grouped(a, cfgs, [("free text", [r["rows"][c]["free"] for c in cfgs], "env"),
                        ("typed schema", [r["rows"][c]["typed"] for c in cfgs], "agent")],
              fmt="{:.2f}", ylabel="hit rate (6 instances)", ylim=(0, 1.25))
    P.bars(b, cfgs, [r["rows"][c]["diff"] for c in cfgs], kinds=["bad"] * 3, fmt="{:+.2f}",
           ylabel="typed − free", ylim=(-0.7, 0.15))
    b.axhline(0, color="#222222", lw=0.6)
    P.note(b, -0.5, 0.06, f"exact sign-flip p = {r['sign_flip_p']:.2f} (floor {r['p_floor']:.2f})")
    return fig, ("In the toy, the typed schema lowers the hit rate in every configuration, yet with three configurations "
                 "the exact sign-flip p-value cannot fall below its floor of 0.25.")


@reg("02")
def _(d):
    r = J(d, "enforcement_cost.json")
    rows = r["rows"]
    cols = [x["id"] for x in rows]
    rules = ["R1", "R2", "R3"]
    grid = [(rl, [("✗" if rl in x["violations"] else "·", "bad" if rl in x["violations"] else "neutral") for x in rows]) for rl in rules]
    grid.append(("waived →", [("BLOCK" if x["verdict"] == "BLOCK" else "ALLOW", _gb(x["verdict"] == "ALLOW")) for x in rows]))
    fig, (a,) = P.panels(1, height=1.9, titles=["Rule violations and the fail-closed verdict per repository (a01–a06 agent topics; b01–b04 comparison)"])
    P.strip(a, cols, grid)
    s = r["summary"]
    return fig, (f"The gate would block {s['agent']['blocked']} of {s['agent']['n']} agent repositories and "
                 f"{s['comparison']['blocked']} of {s['comparison']['n']} comparison repositories; an approved waiver turns a04's block into an allow, "
                 "and the violation is still reported.")


@reg("03")
def _(d):
    r = J(d, "leakage_rules.json")["by_size"]
    xs = [str(x["size"]) for x in r]
    fig, (a, b) = P.panels(2, titles=["Recall of planted copies", "False-positive rate (containment)"])
    P.grouped(a, xs, [("whole-corpus Jaccard", [x["jaccard_recall"] for x in r], "bad"),
                      ("per-item containment", [x["containment_recall"] for x in r], "good")],
              fmt="{:.1f}", ylabel="recall", ylim=(0, 1.3))
    a.set_xlabel("reference size (documents)")
    P.bars(b, xs, [x["containment_fpr"] for x in r], kinds=["agent"] * 4, fmt="{:.1f}", ylabel="false-positive rate", ylim=(0, 1))
    b.set_xlabel("reference size (documents)")
    return fig, ("The whole-corpus Jaccard rule finds the planted copies only while the reference is tiny; per-item containment keeps "
                 "finding them, but at a fixed threshold its false-positive rate rises as the reference grows.")


@reg("04")
def _(d):
    r = J(d, "zero_audit.json")["rows"]
    ks = list(r)
    fig, (a, b) = P.panels(2, titles=["Reported attack success", "Exercised denominator and utility"])
    P.bars(a, ks, [r[k]["asr"] for k in ks], kinds=["good"] * len(ks), fmt="{:.2f}", ylabel="attack-success rate", ylim=(0, 1))
    P.grouped(b, ks, [("exercised cases / 10", [r[k]["exercised"] / r[k]["n"] for k in ks], "env"),
                      ("utility", [r[k]["utility"] for k in ks], "agent")], fmt="{:.1f}", ylabel="share", ylim=(0, 1.3))
    return fig, ("Every release reports a zero, but rel-B exercised no case, rel-D exercised one, and rel-C kept no utility: "
                 "only rel-A and rel-E support the reading that the defence worked.")


@reg("05")
def _(d):
    r = J(d, "benchmark.json")["benchmarks"]
    xs = [str(x["trace_size"]) for x in r]
    fig, (a, b) = P.panels(2, titles=["Verification proof length", "Build and verify time (machine-dependent)"])
    P.bars(a, xs, [x["proof_length"] for x in r], kinds=["good"] * len(r), fmt="{:d}", ylabel="hashes in proof")
    a.set_xlabel("trace size (steps)")
    P.grouped(b, xs, [("build chain", [x["chain_build_ms"] for x in r], "env"),
                      ("verify", [x["verify_time_ms"] for x in r], "good")], fmt="{:.2f}", ylabel="milliseconds")
    b.set_xlabel("trace size (steps)")
    return fig, ("Proof length grows logarithmically with the trace while build and verification time grow roughly linearly; "
                 "the verdicts on tampered and incomplete traces do not depend on the machine.")


@reg("06")
def _(d):
    r = J(d, "label_vs_oracle.json")
    ms = sorted(r["rates"])
    fig, (a, b) = P.panels(2, widths=[1.5, 1], titles=["Same trials, two labels", "Rank by each label"])
    P.grouped(a, ms, [("text label", [r["rates"][m]["text"] for m in ms], "agent"),
                      ("execution oracle", [r["rates"][m]["oracle"] for m in ms], "good")], fmt="{:.2f}", ylabel="success rate", ylim=(0, 1.2))
    for m in ms:
        b.plot([0, 1], [r["rank_text"][m], r["rank_oracle"][m]], color="#555555", lw=0.9, marker="o", ms=4)
        b.text(-0.06, r["rank_text"][m], m, ha="right", va="center", fontsize=7)
        b.text(1.06, r["rank_oracle"][m], m, ha="left", va="center", fontsize=7)
    b.set_xticks([0, 1]); b.set_xticklabels(["text", "oracle"]); b.set_ylim(4.5, 0.5); b.set_xlim(-0.4, 1.4)
    b.set_ylabel("rank (1 = most attacks)")
    P.note(b, 0.05, 4.4, f"Kendall τ = {r['kendall_tau']:+.2f}")
    return fig, "The text heuristic ranks m1 as most vulnerable; the socket oracle ranks m2 first, and the two orderings are uncorrelated."


@reg("07")
def _(d):
    r = J(d, "triage_results.json")["results"]
    cols = [x["artifact_id"].replace("art-", "a") for x in r]
    fig, (a,) = P.panels(1, height=1.7, titles=["Verdict per artefact: naive triage against provenance-gated triage"])
    P.strip(a, cols, [("naive", [(x["baseline_verdict"], "bad" if x["baseline_verdict"] != x["expected"]["provenance_aware"] else "good") for x in r]),
                      ("gated", [(x["verdict"], _gb(x["ok"])) for x in r])])
    return fig, "Where artefact text tries to clear its own artefact, the naive triage follows it and the provenance-gated triage does not."


@reg("08")
def _(d):
    r = J(d, "inclusion_results.json")
    v, g = r["vulnerable_host_call_counts"], r["guarded_host_call_counts"]
    keys = sorted(set(v) | set(g))
    fig, (a,) = P.panels(1, height=2.3, titles=["Host calls made by each agent on the simulated range"])
    P.grouped(a, keys, [("vulnerable agent", [v.get(k, 0) for k in keys], "bad"),
                        ("guarded agent", [g.get(k, 0) for k in keys], "good")], fmt="{:d}", ylabel="calls")
    return fig, "The guarded agent never executes or sends what an included file asks for; its remaining calls are in-scope reads."


@reg("09")
def _(d):
    s = J(d, "intercept_results.json")["summary"]
    fig, (a,) = P.panels(1, height=2.2, titles=["Actions proposed from intercepted frames"])
    P.bars(a, ["baseline acted", "guarded allowed", "guarded blocked", "credentials still live"],
           [s["baseline_actions"], s["guarded_allowed"], s["guarded_blocked"], s["buffer"]["live_entries_after_run"]],
           kinds=["bad", "good", "good", "good"], fmt="{:d}", ylabel="count")
    return fig, (f"Of {s['baseline_actions']} actions the baseline takes on {s['frames']} frames, the guard allows {s['guarded_allowed']} "
                 "and blocks the rest; no credential remains in the buffer after the run.")


@reg("10")
def _(d):
    r = J(d, "blocked_vs_contained.json")
    rows = [x for x in r["rows"] if x["out_of_scope"]]
    cols = [x["id"] for x in rows]
    fig, (a, b) = P.panels(2, widths=[1.6, 1], titles=["Out-of-scope proposals", "Totals"])
    P.strip(a, cols, [("guardrail", [(x["verdict"], _gb(x["verdict"] == "BLOCK")) for x in rows]),
                      ("contained", [("yes" if x["contained"] else "no", _gb(x["contained"])) for x in rows])])
    P.bars(b, ["violations", "blocked", "contained"], [r["violations"], r["blocked"], r["contained"]],
           kinds=["neutral", "good", "good"], fmt="{:d}", ylabel="proposals")
    return fig, (f"The guardrail blocks {r['blocked']} of {r['violations']} out-of-scope proposals but contains only {r['contained']}: "
                 "two destinations pass the resolver and two blocks are undone by the next rewrite.")


@reg("11")
def _(d):
    r = [x for x in J(d, "audit_results.json")["results"] if "audit_verdict" in x]
    cols = [x["paper_id"] for x in r]
    fig, (a,) = P.panels(1, height=1.7, titles=["Naive review against the degenerate-reporting audit"])
    P.strip(a, cols, [("naive", [(x["naive_reviewer"], "neutral") for x in r]),
                      ("audit", [(x["audit_verdict"][:6], "good" if x["audit_verdict"] == "PASS" else "neutral" if x["audit_verdict"].startswith("INCON") else "bad") for x in r])])
    return fig, "A naive reviewer accepts seven of eight papers; the audit fails four that never rule out a do-nothing policy and leaves two inconclusive."


@reg("12")
def _(d):
    r = J(d, "provenance_results.json")["results"]
    cols = [x["case"].replace("cal_", "c") for x in r]
    def cell(x):
        dec = x["decision"]
        return (dec.replace("not_requested", "no action"), "neutral" if dec == "not_requested" else "good" if dec == "allow" else "agent")
    fig, (a,) = P.panels(1, height=1.7, titles=["Calendar cases: provenance and the authorisation decision"])
    P.strip(a, cols, [("trusted?", [("yes" if x["trusted"] else "no", "env" if x["trusted"] else "neutral") for x in r]),
                      ("decision", [cell(x) for x in r])])
    return fig, "Only content whose originator is identifiable and trusted may trigger an action; everything else is blocked or never acts."


@reg("13")
def _(d):
    rows = J(d, "toy_eval.json")["rows"]
    cues = ["none", "true", "wrong"]
    f = [sum(x["follower_correct"] for x in rows if x["cue"] == c) / max(1, sum(x["cue"] == c for x in rows)) for c in cues]
    ag = [sum(x["agree"] for x in rows if x["cue"] == c) / max(1, sum(x["cue"] == c for x in rows)) for c in cues]
    fig, (a,) = P.panels(1, height=2.3, titles=["Cue-following assessor: localisation and agreement by cue"])
    P.grouped(a, cues, [("hit rate", f, "good"), ("agreement", ag, "agent")], fmt="{:.2f}", ylabel="share", ylim=(0, 1.3))
    return fig, "A wrong cue drives the cue-following assessor to the decoy; agreement is no evidence that the localisation is right."


@reg("14")
def _(d):
    r = J(d, "gating_eval.json")
    keys = [("conformal_same", "conformal\nsame"), ("conformal_shifted", "conformal\nshifted"),
            ("baseline_same", "fixed 0.5\nsame"), ("baseline_shifted", "fixed 0.5\nshifted")]
    keys = [(k, l) for k, l in keys if k in r]
    fig, (a,) = P.panels(1, height=2.4, titles=["Realised risk among executed calls"])
    P.bars(a, [l for _, l in keys], [r[k]["risk"] for k, _ in keys],
           kinds=["bad" if r[k]["risk"] > r["alpha"] else "good" for k, _ in keys], fmt="{:.2f}",
           ylabel="share of executed calls injected", ylim=(0, 1.2), thr=r["alpha"], thr_label=f"α = {r['alpha']}")
    return fig, f"On the calibration corpus the conformal gate keeps risk under α = {r['alpha']}; on the shifted corpus the same threshold fails."


@reg("15")
def _(d):
    r = J(d, "probe_eval.json")
    rows = r["rows"]
    cols = [x["id"] for x in rows]
    fig, (a,) = P.panels(1, height=1.7, titles=[f"Probe at threshold {r['threshold']}: truth against flag"])
    P.strip(a, cols, [("hijacked", [("yes" if x["hijacked"] else "no", "bad" if x["hijacked"] else "neutral") for x in rows]),
                      ("flagged", [("FLAG" if x["flagged"] else "-", "good" if x["flagged"] == x["hijacked"] else "bad") for x in rows])])
    return fig, f"The probe catches {r['catches']} of {r['n_hijacked']} hijacked episodes with {r['false_positives']} false alarms at this operating point."


@reg("16")
def _(d):
    r = J(d, "relay_control.json")["rows"]
    labels = [f"{x['model']}\n{x['arm']}" for x in r]
    fig, (a,) = P.panels(1, height=2.4, titles=["Instruction effect at agent 3 (instructed minus uninstructed reach)"])
    P.bars(a, labels, [x["effect"] for x in r], kinds=["bad" if x["effect"] > 0 else "good" for x in r],
           fmt="{:+.2f}", ylabel="difference in reach", ylim=(-0.5, 0.6))
    a.axhline(0, color="#222222", lw=0.6)
    return fig, ("Without a boundary mechanism only m3 relays the instructed marker more than an ordinary code; with one, "
                 "every model relays it less than the control.")


@reg("17")
def _(d):
    r = J(d, "fidelity.json")
    rows = r["rows"]
    fig, (a, b) = P.panels(2, widths=[1.4, 1], titles=["Report against log, per run", "Violations by claim type"])
    P.strip(a, [x["id"] for x in rows], [("verdict", [("ok" if x["faithful"] else "✗", _gb(x["faithful"])) for x in rows])])
    v = r["violations_by_type"]
    P.bars(b, list(v), list(v.values()), kinds=["bad"] * len(v), fmt="{:d}", ylabel="runs", rotate=20)
    return fig, f"{r['n_violations']} of {r['n_runs']} completion reports claim something the action log contradicts."


@reg("18")
def _(d):
    r = J(d, "lang_gap.json")
    langs = {}
    for x in r["rows"]:
        a = langs.setdefault(x["lang"], [0, 0])
        a[0] += x["caught"]
        a[1] += x["injected"]
    ks = list(langs)
    fig, (a,) = P.panels(1, height=2.3, titles=["Detector recall by language of the payload"])
    P.bars(a, ks, [langs[k][0] / langs[k][1] for k in ks], kinds=["good" if langs[k][0] == langs[k][1] else "bad" for k in ks],
           fmt="{:.2f}", ylabel="recall", ylim=(0, 1.25), notes=[f"{langs[k][0]}/{langs[k][1]}" for k in ks])
    return fig, "Every English payload is caught; translated payloads are caught inconsistently, three of six in total."


@reg("19")
def _(d):
    r = J(d, "lineage.json")
    k = r["by_kind"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Models by source of risk"])
    P.bars(a, list(k), list(k.values()), kinds=["good", "bad", "bad", "bad"][: len(k)], fmt="{:d}", ylabel="models")
    return fig, f"{r['n_risky']} of {r['n_models']} models carry risk, most of it inherited from a parent rather than introduced."


@reg("20")
def _(d):
    t = J(d, "soft404_gate.json")["tiers"]
    ks = sorted(t)
    fig, (a,) = P.panels(1, height=2.3, titles=["Adoption of /llms.txt: status 200 against the byte gate"])
    P.grouped(a, ks, [("naive (HTTP 200)", [t[k]["status_200"] / t[k]["n"] for k in ks], "bad"),
                      ("gated (agent file)", [t[k]["agent_file"] / t[k]["n"] for k in ks], "good")],
              fmt="{:.2f}", ylabel="share of hosts", ylim=(0, 1.2))
    return fig, "Counting HTTP 200s overstates adoption; many 200s are HTML soft-404s, more so among unranked hosts."


@reg("21")
def _(d):
    r = J(d, "registry_hosting.json")
    plat = round(r["platform_share"] * r["endpoints"])
    fig, (a, b) = P.panels(2, titles=["Where latest-version endpoints are hosted", "Version cadence"])
    P.bars(a, ["shared platform\nsuffix", "own domain"], [plat, r["endpoints"] - plat], kinds=["agent", "env"], fmt="{:d}", ylabel="endpoints")
    P.bars(b, ["≤ 24 h", "> 24 h"], [r["within_24h"], r["transitions"] - r["within_24h"]], kinds=["agent", "neutral"],
           fmt="{:d}", ylabel="version transitions")
    return fig, ("Endpoints sit under a few platform suffixes, most new versions follow within a day, and both endpoint "
                 "changes in the toy arrive under a patch bump.")


@reg("22")
def _(d):
    r = J(d, "memory_leak.json")
    fig, (a,) = P.panels(1, height=2.3, titles=["Memory entries by leakage regime"])
    P.bars(a, ["kept high-risk\ncontent", "resurfaced\nelsewhere", "survived\nerasure"],
           [len(r["persists_high"]), len(r["resurfaced"]), len(r["erasure_failures"])], kinds=["bad"] * 3,
           fmt="{:d}", ylabel=f"entries (of {r['n_entries']})")
    return fig, f"The three regimes are separate failures; one of {r['n_deleted']} deletions left its content behind."


@reg("23")
def _(d):
    r = J(d, "faults.json")
    outs = ["graceful", "cascade", "silent-wrong", "cost-blowup"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Outcome of six injected faults"])
    P.grouped(a, outs, [("no retry", [r["no_retry"]["counts"].get(o, 0) for o in outs], "bad"),
                        ("with retry budget", [r["with_retry"]["counts"].get(o, 0) for o in outs], "good")],
              fmt="{:d}", ylabel="faults")
    return fig, "A bounded retry budget turns most faults into graceful outcomes; a permanent fault still cascades."


@reg("24")
def _(d):
    r = J(d, "authz.json")["rows"]
    fig, (a,) = P.panels(1, height=1.5, titles=["Delegation chains: both properties checked hop by hop"])
    P.strip(a, [x["id"] for x in r], [("verdict", [("holds" if x["clean"] else ("audience" if "audience" in x["violations"][0] else "scope ↑"), _gb(x["clean"])) for x in r])])
    return fig, "One chain changes audience and one widens its scope; each is caught at the hop where it happens."


@reg("25")
def _(d):
    r = J(d, "attest.json")
    cols = [f"p{i+1}" for i in range(r["n_packages"])]
    fig, (a,) = P.panels(1, height=1.7, titles=["Install decision per package (first four attested)"])
    P.strip(a, cols, [("fail-closed", [(x[:5], _gb(x == "allow")) for x in r["closed_decisions"]]),
                      ("fail-open", [("warn" if "warn" in x else x[:5], "neutral" if "warn" in x else "good") for x in r["open_decisions"]])])
    return fig, f"Fail-closed blocks all {r['fail_closed_blocked']} unattested packages; fail-open installs them with a warning."


@reg("26")
def _(d):
    r = J(d, "sandbox.json")["rows"]
    ks = list(r)
    fig, (a,) = P.panels(1, height=2.3, titles=["Escape rate per isolation configuration"])
    P.bars(a, ks, [r[k]["rate"] for k in ks], kinds=["bad" if r[k]["rate"] > 0 else "good" for k in ks], fmt="{:.2f}",
           ylabel="probes that escaped", ylim=(0, 1.25), notes=[f"{r[k]['escaped']}/{r[k]['total']}" for k in ks])
    return fig, "Only the strict configuration contains every probe; the default subprocess setting still leaks network and environment."


@reg("27")
def _(d):
    r = J(d, "ci_scan.json")["rows"]
    fig, (a,) = P.panels(1, height=1.5, titles=["Repositories: public trigger, no identity gate, write permission"])
    P.strip(a, [x["id"] for x in r], [("exposed", [("YES" if x["vulnerable"] else "no", "bad" if x["vulnerable"] else "good") for x in r])])
    return fig, "Three repositories let an outside account start an agent run that can write."


@reg("28")
def _(d):
    r = J(d, "memascope.json")
    ids = [f"e{i}" for i in range(1, r["n_entries"] + 1)]
    fig, (a,) = P.panels(1, height=1.5, titles=["Memory entries scored for instruction-likeness (read-only audit)"])
    P.strip(a, ids, [("audit", [("FLAG" if e in r["flagged"] else "ok", "bad" if e in r["flagged"] else "good") for e in ids])])
    return fig, f"The auditor flags {r['n_flagged']} of {r['n_entries']} stored entries and changes none of them."


@reg("29")
def _(d):
    r = J(d, "provenance.json")
    ids = [f"a{i}" for i in range(1, r["total"] + 1)]
    fig, (a,) = P.panels(1, height=1.5, titles=["Actions traced back to a trusted root"])
    P.strip(a, ids, [("attributable", [("no" if i in r["unattributable"] else "yes", "bad" if i in r["unattributable"] else "good") for i in ids])])
    return fig, (f"{r['attributable']} of {r['total']} actions trace to their cause; the hash chain verifies and a tampered copy is detected.")


@reg("30")
def _(d):
    r = J(d, "defaults.json")["rows"]
    reasons = {}
    for x in r:
        for z in x["reasons"]:
            reasons[z] = reasons.get(z, 0) + 1
    fig, (a, b) = P.panels(2, widths=[1.4, 1], titles=["Stacks flagged by the codebook", "Reasons"])
    P.strip(a, [x["id"] for x in r], [("verdict", [("✗" if x["insecure"] else "ok", "bad" if x["insecure"] else "good") for x in r])])
    P.hbars(b, list(reasons), list(reasons.values()), kinds=["bad"] * len(reasons), fmt="{:d}", xlabel="stacks")
    top = max(reasons, key=reasons.get)
    return fig, f"{sum(x['insecure'] for x in r)} of {len(r)} stacks ship an insecure default; the most frequent reason in the toy is {top.replace('-', ' ')}."
