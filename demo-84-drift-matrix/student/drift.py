"""Demo 84 (Longitudinal Drift Matrix): per-release privileged-sink deltas, a review rule, and sink-to-code elasticity.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/drift.py
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

import math

REVIEW_CLASSES = ("shell", "eval")


def transitions(releases):
    rows = []
    for a, b in zip(releases, releases[1:]):
        delta = {k: b["sinks"][k] - a["sinks"][k] for k in a["sinks"]}
        rows.append({"from": a["release"], "to": b["release"], "delta": delta,
                     "flag": any(delta[k] > 0 for k in REVIEW_CLASSES)})
    return rows


def elasticity(releases):
    """Growth of total sinks relative to growth of code, first to last release (log ratio)."""
    s0, s1 = sum(releases[0]["sinks"].values()), sum(releases[-1]["sinks"].values())
    return math.log(s1 / s0) / math.log(releases[-1]["loc"] / releases[0]["loc"])


def main():
    data = load()
    out = {"demo": "demo-84-drift-matrix", "frameworks": {}}
    for fw, rel in sorted(data["frameworks"].items()):
        rows = transitions(rel)
        e = elasticity(rel)
        out["frameworks"][fw] = {"transitions": rows, "elasticity": round(e, 3),
                                 "totals": [sum(r["sinks"].values()) for r in rel],
                                 "releases": [r["release"] for r in rel]}
        print(f"{fw}: elasticity {e:.2f} (sinks grow {'slower' if e < 1 else 'faster'} than code)")
        for r in rows:
            d = " ".join(f"{k}{v:+d}" for k, v in r["delta"].items() if v)
            print(f"  {r['from']} -> {r['to']}: {d or 'no change':32s} {'REVIEW' if r['flag'] else '-'}")
    print("lesson: a release-by-release drift matrix shows where review effort is due; growth alone does not.")
    write("drift.json", out)


if __name__ == "__main__":
    main()
