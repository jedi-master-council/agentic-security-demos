"""Demo 88 (The Detection Confusion Matrix): three structural detectors, a 2-of-3 majority and a union, scored on labelled trajectories.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/confusion.py
"""
import json
import os
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURES = os.path.join(DEMO_DIR, "fixtures", "fixtures.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURES):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def provenance_taint(t):
    """Flag when a token of the candidate call's argument appears in untrusted tool output."""
    toks = {w for w in t["target_call"]["args"].replace("?", " ").split() if len(w) > 6}
    return any(any(w in s["output"] for w in toks) for s in t["steps"] if s["untrusted"])


def task_mismatch(t):
    return t["target_call"]["tool"] not in t["task_tools"]


def recency(t):
    return bool(t["steps"]) and t["steps"][-1]["untrusted"]


DETECTORS = {"taint": provenance_taint, "mismatch": task_mismatch, "recency": recency}


def verdicts(t):
    v = {k: f(t) for k, f in DETECTORS.items()}
    v["majority"] = sum(v[k] for k in DETECTORS) >= 2
    v["union"] = any(v[k] for k in DETECTORS)
    return v


def confusion(data, name):
    c = {"tp": 0, "fp": 0, "fn": 0, "tn": 0}
    for t in data["trajectories"]:
        flag, inj = verdicts(t)[name], t["injected"]
        c["tp" if flag and inj else "fp" if flag else "fn" if inj else "tn"] += 1
    c["tpr"] = round(c["tp"] / (c["tp"] + c["fn"]), 3)
    c["fpr"] = round(c["fp"] / (c["fp"] + c["tn"]), 3)
    return c


def main():
    data = load()
    names = list(DETECTORS) + ["majority", "union"]
    print("traj inj  " + " ".join(f"{n:>8s}" for n in names))
    for t in data["trajectories"]:
        v = verdicts(t)
        print(f"{t['id']}  {'Y' if t['injected'] else '-'}   " + " ".join(f"{('FLAG' if v[n] else '-'):>8s}" for n in names))
    table = {n: confusion(data, n) for n in names}
    for n in names:
        c = table[n]
        print(f"{n:9s} tp {c['tp']} fp {c['fp']} fn {c['fn']} tn {c['tn']}  TPR {c['tpr']:.2f}  FPR {c['fpr']:.2f}")
    print("lesson: each structural cue misses a different attack; the union buys sensitivity with false alarms.")
    write("detection.json", {"demo": "demo-88-detection-confusion", "confusion": table})


if __name__ == "__main__":
    main()
