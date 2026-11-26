"""Demo 64 (Socratic Answer Guard): calibrating an answer guard: answers let through against helpful hints blocked.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/guard.py
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


def at_threshold(replies, tau):
    leaks = [r for r in replies if r["leaks_answer"]]
    hints = [r for r in replies if not r["leaks_answer"]]
    passed_leaks = sum(r["leak_score"] < tau for r in leaks)
    blocked_hints = sum(r["leak_score"] >= tau for r in hints)
    return {"tau": tau, "leak_rate": round(passed_leaks / len(leaks), 3),
            "over_blocking": round(blocked_hints / len(hints), 3)}


def main():
    d = load()
    rows = [at_threshold(d["replies"], t) for t in d["thresholds"]]
    print("threshold  answers let through  helpful hints blocked")
    for r in rows:
        print(f"{r['tau']:9.1f} {r['leak_rate']:20.2f} {r['over_blocking']:22.2f}")
    print("lesson: no threshold gives both zero leaks and zero over-blocking; choose the operating point on purpose.")
    write("guard_calibration.json", {"demo": "demo-64-answer-guard", "rows": rows})


if __name__ == "__main__":
    main()
