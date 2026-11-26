"""Demo 63 (Policy-Coding Reliability): Krippendorff's alpha per dimension for two model coders, and code drift on unchanged text.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/reliability.py
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


def kripp_alpha_nominal(a, b):
    """Krippendorff's alpha, nominal data, two coders, no missing values."""
    vals = a + b
    n = len(vals)
    cats = sorted(set(vals))
    nc = {c: vals.count(c) for c in cats}
    do = sum(x != y for x, y in zip(a, b)) * 2 / n
    de = sum(nc[c] * nc[k] for c in cats for k in cats if c != k) / (n * (n - 1))
    return 1.0 if de == 0 else 1 - do / de


def per_dimension(d):
    ids = sorted(d["wave1"]["model_a"])
    out = {}
    for j, dim in enumerate(d["dimensions"]):
        a = [d["wave1"]["model_a"][i][j] for i in ids]
        b = [d["wave1"]["model_b"][i][j] for i in ids]
        out[dim] = round(kripp_alpha_nominal(a, b), 3)
    return out


def drift(d):
    """Codes that changed between waves although the text did not."""
    return [i for i in d["unchanged_text"] if d["wave1"]["model_a"][i] != d["wave2"]["model_a"][i]]


def main():
    d = load()
    alpha = per_dimension(d)
    for dim, a in alpha.items():
        print(f"{dim:20s} alpha = {a:+.2f}  {'acceptable (>= 0.667)' if a >= 0.667 else 'unreliable'}")
    print(f"model A changed its codes on unchanged text: {', '.join(drift(d)) or 'none'}")
    print("lesson: report reliability per dimension; and re-code unchanged text to see whether a model is stable.")
    write("reliability.json", {"demo": "demo-63-coding-reliability", "alpha": alpha, "drift": drift(d)})


if __name__ == "__main__":
    main()
