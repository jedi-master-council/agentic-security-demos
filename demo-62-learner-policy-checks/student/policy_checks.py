"""Demo 62 (LLM Learner Policy Checks): schema adherence, calibration against a base-rate baseline, and persona sensitivity.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/policy_checks.py
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


def valid(o, req):
    for k, t in req.items():
        if k not in o:
            return False
        v = o[k]
        if t == "bool" and not isinstance(v, bool):
            return False
        if t == "float" and not (isinstance(v, (int, float)) and 0 <= v <= 1):
            return False
        if isinstance(t, list) and v not in t:
            return False
    return True


def brier(ps, ys):
    return sum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ps)


def evaluate(d):
    req = d["required"]
    L = d["learners"]
    adh = [valid(x["output"], req) for x in L]
    usable = [x for x, a in zip(L, adh) if a]
    ys = [1.0 if x["withdrew"] else 0.0 for x in usable]
    ps = [x["output"]["p_withdraw"] for x in usable]
    base = sum(1.0 if x["withdrew"] else 0.0 for x in L) / len(L)
    sens = [abs(x["output"]["p_withdraw"] - x["output_reworded_persona"]["p_withdraw"]) >= 0.2
            for x in usable]
    return {"adherence": sum(adh) / len(L), "invalid": [x["id"] for x, a in zip(L, adh) if not a],
            "brier_policy": round(brier(ps, ys), 3), "brier_base_rate": round(brier([base] * len(ys), ys), 3),
            "persona_sensitive": [x["id"] for x, s in zip(usable, sens) if s]}


def main():
    r = evaluate(load())
    print(f"schema adherence {r['adherence']:.2f}  invalid outputs: {', '.join(r['invalid'])}")
    print(f"Brier score: LLM policy {r['brier_policy']:.3f}  base-rate baseline {r['brier_base_rate']:.3f}  (lower is better)")
    print(f"persona-sensitive learners (|change| >= 0.20 under an equivalent rewording): {', '.join(r['persona_sensitive'])}")
    print("lesson: check the format, then compare with a baseline that costs nothing, then perturb the wording.")
    write("policy_checks.json", dict(r, demo="demo-62-learner-policy-checks"))


if __name__ == "__main__":
    main()
