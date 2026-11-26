"""Demo 82 (Guardrail Score Transfer): rank correlation and a cross-tabulation of benchmark score against replay outcome.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/transfer.py
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


def ranks(values):
    order = sorted(range(len(values)), key=lambda i: -values[i])
    r = [0] * len(values)
    for pos, i in enumerate(order, start=1):
        r[i] = pos
    return r


def spearman(x, y):
    """Spearman rank correlation without ties: 1 - 6 sum d^2 / (n (n^2 - 1))."""
    rx, ry = ranks(x), ranks(y)
    n = len(x)
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - 6 * d2 / (n * (n * n - 1))


def crosstab(models, cut):
    """Benchmark half (top or bottom) against replay verdict (pass if block share >= cut)."""
    med = sorted(m["benchmark"] for m in models)[len(models) // 2]
    tab = {"top|pass": 0, "top|fail": 0, "bottom|pass": 0, "bottom|fail": 0}
    for m in models:
        half = "top" if m["benchmark"] >= med else "bottom"
        tab[f"{half}|{'pass' if m['replay_block'] >= cut else 'fail'}"] += 1
    return tab


def main():
    data = load()
    ms = data["models"]
    rho = spearman([m["benchmark"] for m in ms], [m["replay_block"] for m in ms])
    rb, rr = ranks([m["benchmark"] for m in ms]), ranks([m["replay_block"] for m in ms])
    tab = crosstab(ms, data["replay_pass"])
    print(f"{'model':5s} {'family':15s} bench rank  replay rank")
    for m, a, b in zip(ms, rb, rr):
        print(f"{m['id']:5s} {m['family']:15s} {m['benchmark']:.2f}  {a}    {m['replay_block']:.2f}   {b}")
    print(f"Spearman rho = {rho:+.2f}")
    print(f"cross-tab (replay pass at block share >= {data['replay_pass']}): {tab}")
    print("lesson: the benchmark ranking inverts on replay; the families split, not the scores.")
    write("transfer.json", {"demo": "demo-82-score-transfer", "spearman": round(rho, 3),
                            "bench_rank": rb, "replay_rank": rr, "crosstab": tab})


if __name__ == "__main__":
    main()
