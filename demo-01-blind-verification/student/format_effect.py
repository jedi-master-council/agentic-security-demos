"""Demo 01, current procedure: free-text versus typed-schema commitments, sealed before reveal, compared per configuration.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/format_effect.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "format_effect.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")

import hashlib
import itertools


def seal(files):
    """Commit before reveal: the sealed bytes are the sorted file list; the hash is published."""
    return hashlib.sha256(",".join(sorted(files)).encode()).hexdigest()


def hit_rate(cells, gold, budget):
    hits = 0
    for inst, files in cells.items():
        assert len(files) <= budget, "commitment exceeds the budget"
        hits += gold[inst] in files
    return hits / len(cells)


def sign_flip_p(diffs):
    """Exact two-sided sign-flip test over configurations (the unit of analysis)."""
    obs = abs(sum(diffs) / len(diffs))
    count = total = 0
    for signs in itertools.product((1, -1), repeat=len(diffs)):
        total += 1
        count += abs(sum(s * d for s, d in zip(signs, diffs)) / len(diffs)) >= obs - 1e-12
    return count / total


def main():
    data = load()
    rows = {}
    for cfg, fmts in sorted(data["commitments"].items()):
        seals = {f: seal([x for v in fmts[f].values() for x in v]) for f in fmts}
        free = hit_rate(fmts["free"], data["gold"], data["budget"])
        typed = hit_rate(fmts["typed"], data["gold"], data["budget"])
        rows[cfg] = {"free": round(free, 3), "typed": round(typed, 3), "diff": round(typed - free, 3),
                     "seal_free": seals["free"][:12], "seal_typed": seals["typed"][:12]}
    diffs = [r["diff"] for r in rows.values()]
    p = sign_flip_p(diffs)
    floor = 2 / 2 ** len(diffs)
    print("config  free-text hit  typed-schema hit  difference  (sealed before reveal)")
    for cfg, r in rows.items():
        print(f"{cfg:7s} {r['free']:13.2f} {r['typed']:17.2f} {r['diff']:+11.2f}  {r['seal_free']}/{r['seal_typed']}")
    mean = sum(diffs) / len(diffs)
    print(f"mean paired difference {mean:+.2f}; exact sign-flip p = {p:.2f} (floor with {len(diffs)} configurations = {floor:.2f})")
    print("lesson: the output format can move where a model looks; with few configurations no test can be significant.")
    write("format_effect.json", {"demo": "demo-01-blind-verification", "rows": rows,
                                 "mean_diff": round(mean, 3), "sign_flip_p": p, "p_floor": floor})


if __name__ == "__main__":
    main()
