"""Figure 2 adapters, demos 61-90."""
import plots as P
from worked_a import J, _gb

W = {}


def reg(n):
    def deco(f):
        W[n] = f
        return f
    return deco


@reg("61")
def _(d):
    r = J(d, "reexecution.json")["rows"]
    cols = [x["id"] for x in r]
    fig, (a,) = P.panels(1, height=2.0, titles=["Machine checks of six agent-written analyses"])
    P.strip(a, cols, [("re-runs", [("yes" if x["finishes"] else "NO", _gb(x["finishes"])) for x in r]),
                      ("numbers traced", [(f"{x['traced']}/{x['numbers']}", _gb(x["traced"] == x["numbers"])) for x in r]),
                      ("answer right", [("yes" if x["correct"] else "no", _gb(x["correct"])) for x in r])])
    return fig, "Answer-only scoring would accept r1 and r4; re-execution and number tracing show one does not re-run and the other states an untraceable number."


@reg("62")
def _(d):
    r = J(d, "policy_checks.json")
    fig, (a, b) = P.panels(2, titles=["Schema adherence", "Calibration (Brier, lower is better)"])
    P.bars(a, ["valid", "invalid"], [r["adherence"] * 10, len(r["invalid"])], kinds=["good", "bad"], fmt="{:.0f}", ylabel="learners")
    P.bars(b, ["LLM policy", "base rate"], [r["brier_policy"], r["brier_base_rate"]], kinds=["agent", "neutral"], fmt="{:.3f}", ylabel="Brier score")
    return fig, f"Two of ten outputs break the schema; the policy beats the base rate, and {len(r['persona_sensitive'])} learners' predictions move under an equivalent persona rewording."


@reg("63")
def _(d):
    r = J(d, "reliability.json")["alpha"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Krippendorff's α between two model families"])
    P.bars(a, [k.replace("_", "\n") for k in r], list(r.values()), kinds=[_gb(v >= 0.667) for v in r.values()], fmt="{:.2f}",
           ylabel="α", ylim=(0, 1.15), thr=0.667, thr_label="0.667")
    return fig, "Agreement is high on three dimensions and near chance on assessment rules; one policy's codes changed although its text did not."


@reg("64")
def _(d):
    r = J(d, "guard_calibration.json")["rows"]
    fig, (a,) = P.panels(1, height=2.4, titles=["Answer guard: the trade-off across thresholds"])
    P.grouped(a, [f"τ = {x['tau']}" for x in r], [("answers let through", [x["leak_rate"] for x in r], "bad"),
                                                  ("hints blocked", [x["over_blocking"] for x in r], "agent")], fmt="{:.2f}", ylabel="share", ylim=(0, 1))
    return fig, "Raising the threshold lets more answers through and blocks fewer hints; τ = 0.5 to 0.7 balances the two in the toy."


@reg("65")
def _(d):
    r = J(d, "bibliometrics.json")
    fig, (a,) = P.panels(1, height=2.2, titles=["Two communities and their overlap"])
    P.bars(a, ["agent-security works", "education works", "shared authors", "second-model agreement"],
           [r["n_S"], r["n_E"], len(r["shared_authors"]), r["sample_agree"][0]], kinds=["env", "env", "good", "agent"], fmt="{:d}",
           ylabel="count", notes=["", "", ", ".join(r["shared_authors"]), f"of {r['sample_agree'][1]}"])
    return fig, "One author bridges the two sets; the second model disagrees with the first on one sampled work."


@reg("66")
def _(d):
    a_ = J(d, "qpu_budget.json")["arms"]
    ks = list(a_)
    fig, (a,) = P.panels(1, height=2.3, titles=["Accepted results per simulated QPU-second"])
    P.bars(a, ks, [a_[k]["accepted_per_qpu_second"] for k in ks], kinds=["neutral", "agent", "good"][: len(ks)], fmt="{:.3f}",
           ylabel="accepted per second", notes=[f"{a_[k]['accepted']} accepted" for k in ks])
    return fig, "The arm that simulates first spends hardware seconds only on jobs likely to pass, and returns the most accepted results per second."


@reg("67")
def _(d):
    r = J(d, "memprobe.json")["rows"]
    fig, (a,) = P.panels(1, height=2.6, titles=["Probe score against the remapped-table null"])
    P.bars(a, [f"{x['model'].replace('frequency-guesser', 'freq').replace('memoriser-', 'm').replace('-exposures', '')}\n{'row' if x['test'].startswith('row') else 'link'}" for x in r],
           [x["observed"] for x in r], kinds=["bad" if x["flagged"] else "neutral" for x in r], fmt="{:.2f}", ylabel="score", ylim=(0, 1.2))
    for i, x in enumerate(r):
        a.plot([i - 0.31, i + 0.31], [x["null_max"]] * 2, color=P.KIND["bad"][1], lw=0.9, ls=(0, (4, 2)))
    P.note(a, -0.5, 1.1, "dashed red = maximum score on remapped tables (the null)")
    return fig, "Only models exposed to the release score above the remapped null; a frequency guesser never does."


@reg("68")
def _(d):
    r = J(d, "idfilter.json")["per_type"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Span-level recall of the identifier filter"])
    P.bars(a, [k.replace("_", "\n") for k in r], [v["recall"] for v in r.values()], kinds=[_gb(v["recall"] == 1) for v in r.values()],
           fmt="{:.2f}", ylabel="recall", ylim=(0, 1.2), notes=[f"{v['caught']}/{v['gold']}" for v in r.values()])
    return fig, "Names are caught; obfuscated e-mail addresses, student numbers and postcodes get through."


@reg("69")
def _(d):
    r = J(d, "grounding.json")["report"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Extracted clauses that are grounded and correct"])
    labels = [f"{x['document'].replace('vendor-', '')}\n{x['extractor'].split()[0]}" for x in r]
    P.grouped(a, labels, [("grounded", [x["grounded_share"] for x in r], "good"),
                          ("correct", [sum(y["correct"] for y in x["rows"]) / len(x["rows"]) for x in r], "agent")], fmt="{:.2f}", ylabel="share", ylim=(0, 1.2))
    return fig, "A keyword baseline can quote the source verbatim and still extract the wrong value; grounding is necessary, not sufficient."


@reg("70")
def _(d):
    r = J(d, "sod.json")["rows"]
    fig, (a,) = P.panels(1, height=1.5, titles=["Users after expanding roles into effective permissions"])
    P.strip(a, [x["user"] for x in r], [("SoD", [("CONFLICT" if x["gapped"] else "ok", "bad" if x["gapped"] else "good") for x in r])])
    return fig, "One user holds both approve-payment and post-payment once roles are expanded."


@reg("71")
def _(d):
    r = J(d, "erasure.json")["rows"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Features erased to flip the score: exhaustive against greedy"])
    P.grouped(a, [x["id"] for x in r], [("exhaustive", [x["exhaustive_size"] for x in r], "good"),
                                        ("greedy", [x["greedy_size"] for x in r], "agent")], fmt="{:d}", ylabel="features erased")
    return fig, "Greedy search matches the exhaustive minimum on these instances; the exhaustive answer is the certificate."


@reg("72")
def _(d):
    r = J(d, "mapping.json")["rows"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Techniques covered and uncovered per control profile"])
    P.grouped(a, [x["id"] for x in r], [("covered", [len(x["covered"]) for x in r], "good"),
                                        ("uncovered", [len(x["uncovered"]) for x in r], "bad")], fmt="{:d}", ylabel="techniques")
    return fig, "Set overlap shows which techniques each control profile leaves uncovered."


@reg("73")
def _(d):
    r = J(d, "ncm.json")
    rows = r["rows"]
    fig, (a,) = P.panels(1, height=1.9, titles=[f"Nearest-class-mean with rejection (θ = {r['threshold']}) against forced choice"])
    P.strip(a, [x["id"] for x in rows], [("truth", [(x["true"], "neutral") for x in rows]),
                                        ("open set", [(x["ncm"], _gb(x["ncm_ok"])) for x in rows]),
                                        ("forced", [(x["forced"], _gb(x["forced_ok"])) for x in rows])])
    return fig, "The forced classifier assigns every unknown pattern to a known class; at θ = 1.6 the open-set version rejects q8 but still misassigns q5 and q6."


@reg("74")
def _(d):
    r = J(d, "lipschitz.json")["rows"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Lipschitz bound: spectral product against Frobenius product"])
    P.grouped(a, [x["id"] for x in r], [("spectral", [x["spectral_product"] for x in r], "good"),
                                        ("Frobenius", [x["frobenius_product"] for x in r], "neutral")], fmt="{:.1f}", ylabel="bound")
    return fig, "The spectral product is never looser than the Frobenius product, and is much tighter for some maps."


@reg("75")
def _(d):
    r = J(d, "linkage.json")
    fig, (a,) = P.panels(1, height=2.2, titles=["Advisories linked on exact identifiers"])
    P.bars(a, ["linked", "severity disagrees", "product disagrees"], [r["matched"], r["severity_disagree"], r["product_disagree"]],
           kinds=["good", "bad", "bad"], fmt="{:d}", ylabel="advisories")
    return fig, "Even exactly linked advisories disagree on severity in two of seven cases."


@reg("76")
def _(d):
    r = J(d, "patrol.json")
    rows = r["rows"]
    fig, (a,) = P.panels(1, height=2.3, titles=[f"Uncovered attacker paths with k = {r['k']} patrol nodes"])
    P.grouped(a, [x["id"] for x in rows], [("exhaustive", [x["exhaustive_uncovered"] for x in rows], "good"),
                                           ("greedy", [x["greedy_uncovered"] for x in rows], "agent")], fmt="{:d}", ylabel="uncovered paths")
    return fig, "Greedy matches the exhaustive optimum on these graphs; in g3 and g6 no pair of patrol nodes covers every attacker path."


@reg("77")
def _(d):
    r = J(d, "horn.json")["rows"]
    fig, (a,) = P.panels(1, height=1.7, titles=["Knowledge bases: inconsistent? clauses deleted to repair"])
    P.strip(a, [x["id"] for x in r], [("derives ⊥", [("yes" if x["inconsistent"] else "no", "bad" if x["inconsistent"] else "good") for x in r]),
                                     ("deleted", [(str(x["deletions"]), "neutral") for x in r])])
    return fig, "Each inconsistent knowledge base is repaired by the smallest deletion that stops forward chaining from deriving falsehood."


@reg("78")
def _(d):
    r = J(d, "covering.json")
    fig, (a,) = P.panels(1, height=2.2, titles=["Learned decision list (rule order = priority)"])
    P.bars(a, [f"{i+1}. {x['feature']}" for i, x in enumerate(r["rules"])] + ["default"],
           [x["support"] for x in r["rules"]] + [r["n_rows"] - sum(x["support"] for x in r["rules"])],
           kinds=["good"] * len(r["rules"]) + ["neutral"], fmt="{:d}", ylabel="URLs covered")
    return fig, f"Two single-feature rules and a default classify all {r['n_rows']} URLs (accuracy {r['accuracy']:.2f})."


@reg("79")
def _(d):
    r = J(d, "contrast.json")
    det = r["rows"][0]["detail"]
    fig, (a,) = P.panels(1, height=2.3, titles=[f"Support in two windows ({r['rows'][0]['id']})"])
    P.grouped(a, [x["item"] for x in det], [("window 1", [x["support_a"] for x in det], "neutral"),
                                            ("window 2", [x["support_b"] for x in det], "agent")], fmt="{:.2f}", ylabel="support", ylim=(0, 1))
    return fig, "An item set is emerging when its support grows at least two-fold and passes the minimum support in the later window."


@reg("80")
def _(d):
    r = J(d, "extraction.json")["fields"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Two-coder agreement per extraction field"])
    P.grouped(a, [k.replace("_", " ") for k in r], [("percent agreement", [v["percent_agreement"] for v in r.values()], "agent"),
                                                   ("Cohen's κ", [v["kappa"] for v in r.values()], "good")],
              fmt="{:.2f}", ylabel="value", ylim=(0, 1.1), thr=0.6, thr_label="κ floor")
    return fig, "The adaptive-attack field has 75% raw agreement but a kappa below the floor, so it goes to adjudication before the map is drawn."


@reg("81")
def _(d):
    r = J(d, "frozen_gate.json")
    c = r["confusion"]
    fig, (a,) = P.panels(1, height=2.2, titles=[f"Frozen gate on eight pinned trajectories (table SHA-256 {r['table_sha256'][:12]}… on both runs)"])
    P.bars(a, ["true positive", "false positive", "missed", "true negative"], [c["tp"], c["fp"], c["fn"], c["tn"]],
           kinds=["good", "bad", "bad", "good"], fmt="{:d}", ylabel="trajectories")
    return fig, "The gate's table is byte-identical on every run; it still misses one attack and flags a security-training trajectory."


@reg("82")
def _(d):
    r = J(d, "transfer.json")
    ms = [f"g{i+1}" for i in range(len(r["bench_rank"]))]
    fig, (a,) = P.panels(1, height=2.4, titles=["Rank on the benchmark against rank on tool-attack replays"])
    for m, x, y in zip(ms, r["bench_rank"], r["replay_rank"]):
        a.plot([0, 1], [x, y], color="#555555", lw=0.9, marker="o", ms=4)
        a.text(-0.05, x, m, ha="right", va="center", fontsize=7); a.text(1.05, y, m, ha="left", va="center", fontsize=7)
    a.set_xticks([0, 1]); a.set_xticklabels(["benchmark", "replay"]); a.set_ylim(len(ms) + 0.5, 0.5); a.set_xlim(-0.5, 1.5)
    a.set_ylabel("rank (1 = best)")
    P.note(a, 0.3, len(ms) + 0.3, f"Spearman ρ = {r['spearman']:+.2f}")
    return fig, "The content-safety models that lead the benchmark trail on replays; the ranking inverts by family."


@reg("83")
def _(d):
    s = J(d, "census.json")["snapshots"]
    ks = ["description_flagged", "remote_without_auth", "name_confusable"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Manifest findings at two registry snapshots"])
    P.grouped(a, ["description\nmarkers", "remote without\nauth metadata", "confusable\nnames"],
              [(f"{k} ({s[k]['summary']['servers']} servers)", [s[k]["summary"][x] for x in ks], "neutral" if k == "t1" else "bad") for k in sorted(s)],
              fmt="{:d}", ylabel="servers")
    return fig, "Between snapshots a new look-alike server appears with an exfiltration instruction in its description."


@reg("84")
def _(d):
    f = J(d, "drift.json")["frameworks"]
    fig, (a,) = P.panels(1, height=2.4, titles=["Privileged sink call sites per release (● = transition needs review)"])
    styles = {"fw-a": ("o", "good"), "fw-b": ("s", "agent"), "fw-c": ("^", "env")}
    for k, v in f.items():
        mk, kind = styles.get(k, ("o", "neutral"))
        xs = list(range(len(v["totals"])))
        a.plot(xs, v["totals"], marker=mk, color=P.KIND[kind][1], lw=1, ms=4, label=f"{k} (elasticity {v['elasticity']:.2f})")
        for i, t in enumerate(v["transitions"]):
            if t["flag"]:
                a.plot([i + 1], [v["totals"][i + 1]], "o", ms=9, mfc="none", mec=P.KIND["bad"][1], mew=1.2)
    a.set_xticks(range(4)); a.set_xticklabels(["release 1", "release 2", "release 3", "release 4"]); a.set_ylabel("sink call sites")
    a.legend(loc="upper left", frameon=False, ncol=3)
    a.set_ylim(0, max(max(v["totals"]) for v in f.values()) * 1.35)
    return fig, "Growth alone does not say which upgrade needs review; the circled transitions add a shell or evaluation call site."


@reg("85")
def _(d):
    r = J(d, "matrix.json")
    cells = r["cells"]
    fws, sinks = ["fw-a", "fw-b", "fw-c"], ["shell", "network", "file_write"]
    def lab(s):
        return {"enforced": ("enforced", "good"), "documented-only": ("doc only", "bad"), "absent": ("absent", "neutral")}[s]
    rows = [(f"{fw} native", [lab(cells[f"{fw}|{s}|native"]) for s in sinks]) for fw in fws] + \
           [(f"{fw} monitor", [lab(cells[f"{fw}|{s}|monitor"]) for s in sinks]) for fw in fws]
    fig, (a, b) = P.panels(2, height=2.6, widths=[1.3, 1], titles=["Enforcement at the sink", "Token label survives the model"])
    P.strip(a, sinks, rows)
    sv = r["survival_by_transform"]
    P.bars(b, list(sv), [k / n for k, n in sv.values()], kinds=["good" if k == n else "bad" for k, n in sv.values()], fmt="{:.1f}",
           ylabel="share of episodes", ylim=(0, 1.2))
    return fig, "No framework enforces provenance at a sink natively; a monitor does, but its token label is lost when the model paraphrases or splits the value."


@reg("86")
def _(d):
    r = J(d, "pii_census.json")["per_family"]
    fig, (a,) = P.panels(1, height=2.3, titles=["Matches per shape family, audited against truth"])
    P.grouped(a, [k.replace("_", " ") for k in r], [("true positive", [v["tp"] for v in r.values()], "good"),
                                                   ("false positive", [v["fp"] for v in r.values()], "bad")], fmt="{:d}", ylabel="arguments")
    return fig, "The closed lexicon is auditable: its one error is a four-part version string read as an IP address."


@reg("87")
def _(d):
    r = J(d, "capability_diff.json")["rows"]
    fig, (a,) = P.panels(1, height=1.9, titles=["Declared against extracted capability per skill"])
    P.strip(a, [x["id"] for x in r], [("hidden", [(",".join(x["understated"]) or "-", "bad" if x["understated"] else "good") for x in r]),
                                     ("unused", [(",".join(x["overstated"]) or "-", "agent" if x["overstated"] else "good") for x in r])])
    return fig, "Two skills can do more than they declare (a shell call, a network post); two declare capabilities their code never uses."


@reg("88")
def _(d):
    c = J(d, "detection.json")["confusion"]
    ks = list(c)
    fig, (a,) = P.panels(1, height=2.4, titles=["Detectors before execution: sensitivity against false alarms"])
    P.grouped(a, ks, [("true-positive rate", [c[k]["tpr"] for k in ks], "good"), ("false-positive rate", [c[k]["fpr"] for k in ks], "bad")],
              fmt="{:.2f}", ylabel="rate", ylim=(0, 1.1))
    return fig, "The union catches every injected action but raises false alarms on most benign ones; task mismatch alone raises none."


@reg("89")
def _(d):
    r = J(d, "divergence.json")["rows"]
    fig, (a,) = P.panels(1, height=2.0, titles=["Boundary payloads validated by two frameworks"])
    def k(v):
        return "good" if v == "accept" else "agent" if v == "accept-coerced" else "bad"
    P.strip(a, [f"{x['id']}\n{x['dimension'].split()[0]}" for x in r],
            [("fw-a lenient", [(x["fw_a"].replace("accept-coerced", "coerce"), k(x["fw_a"])) for x in r]),
             ("fw-b strict", [(x["fw_b"], k(x["fw_b"])) for x in r])])
    return fig, "Six of eight payloads are accepted by one framework and rejected by the other; only the controls agree."


@reg("90")
def _(d):
    r = J(d, "context_acquisition.json")
    ea = r["exposure_acquisition"]
    fig, (a, b) = P.panels(2, widths=[1.5, 1], titles=["Exposure against acquisition", "Resolution: naive and within task"])
    P.grouped(a, [k.replace("CONTRIBUTING", "CONTRIB.") for k in ea], [("visible (exposed)", [v["exposed"] for v in ea.values()], "neutral"),
                            ("opened (acquired)", [v["acquired"] for v in ea.values()], "good")], fmt="{:d}", ylabel="runs (of 12)", rotate=25)
    n = r["naive"]
    P.bars(b, ["prose\nreaders", "non-\nreaders", "within-task\ndifference"], [n["readers"], n["non_readers"], r["within_pooled"]],
           kinds=["agent", "neutral", "good"], fmt="{:.2f}", ylabel="resolved share", ylim=(0, 1))
    return fig, ("README is visible in every run and opened in three; the naive comparison says readers resolve less often, "
                 "but within the same task the difference vanishes.")
