"""Demo 06, current procedure: text-heuristic labels against a transport-layer execution oracle on the same trials.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/label_vs_oracle.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "label_vs_oracle.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def rates(trials):
    by = {}
    for t in trials:
        r = by.setdefault(t["model"], {"n": 0, "text": 0, "oracle": 0})
        r["n"] += 1
        r["text"] += bool(t["text_names_target"] or t["text_proposes_call"])
        r["oracle"] += bool(t["nonce_at_sink"])
    return {m: {"text": v["text"] / v["n"], "oracle": v["oracle"] / v["n"]} for m, v in sorted(by.items())}


def rank(scores):
    order = sorted(scores, key=lambda m: (-scores[m], m))
    return {m: i + 1 for i, m in enumerate(order)}


def kendall_tau(r1, r2):
    ms = sorted(r1)
    conc = disc = 0
    for i in range(len(ms)):
        for j in range(i + 1, len(ms)):
            a = r1[ms[i]] - r1[ms[j]]
            b = r2[ms[i]] - r2[ms[j]]
            conc += a * b > 0
            disc += a * b < 0
    return (conc - disc) / (conc + disc)


def main():
    data = load()
    r = rates(data["trials"])
    rt = rank({m: v["text"] for m, v in r.items()})
    ro = rank({m: v["oracle"] for m, v in r.items()})
    print("model  text-label rate  rank   execution-oracle rate  rank")
    for m, v in r.items():
        print(f"{m:6s} {v['text']:15.2f} {rt[m]:5d} {v['oracle']:22.2f} {ro[m]:5d}")
    tau = kendall_tau(rt, ro)
    print(f"Kendall tau between the two rankings = {tau:+.2f}")
    print("lesson: a lenient text label is not a monotone proxy for what reached the socket; rank by the oracle.")
    write("label_vs_oracle.json", {"demo": "demo-06-reconscope", "rates": r, "rank_text": rt,
                                   "rank_oracle": ro, "kendall_tau": round(tau, 3)})


if __name__ == "__main__":
    main()
