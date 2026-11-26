"""Demo 61 (Re-execution Checks): re-execution, number provenance and reference checks of agent-written analyses.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/reexec.py
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

import statistics

OPS = {"mean": statistics.mean, "median": statistics.median, "max": max, "sum": sum}


def reexecute(run, data):
    """Run the steps in a clean namespace; any unknown name or op stops the run."""
    env = dict(data)
    outputs = []
    for s in run["steps"]:
        if s["op"] == "ratio":
            x, y = s["in"]
            if x not in env or y not in env:
                return False, outputs
            env[s["out"]] = env[x] / env[y]
        elif s["op"] in OPS and s["in"] in env:
            env[s["out"]] = OPS[s["op"]](env[s["in"]])
        else:
            return False, outputs
        outputs.append(env[s["out"]])
    return True, outputs


def traced(numbers, outputs, tol):
    return [any(abs(n - o) <= tol for o in outputs) for n in numbers]


def check(run, data, tol):
    ok, outs = reexecute(run, data)
    tr = traced(run["report_numbers"], outs, tol) if ok else [False] * len(run["report_numbers"])
    correct = abs(run["report_numbers"][-1] - run["reference_answer"]) <= tol
    return {"id": run["id"], "finishes": ok, "traced": sum(tr), "numbers": len(tr), "correct": correct}


def main():
    d = load()
    rows = [check(r, d["data"], d["tolerance"]) for r in d["runs"]]
    print("run  finishes  numbers traced  answer correct  reading")
    for r in rows:
        if not r["finishes"]:
            reading = "steps do not re-run"
        elif r["correct"] and r["traced"] < r["numbers"]:
            reading = "right answer, untraceable number"
        elif r["correct"]:
            reading = "right, and for the right reason"
        elif r["traced"] == r["numbers"]:
            reading = "traceable but wrong"
        else:
            reading = "wrong and untraceable"
        r["reading"] = reading
        print(f"{r['id']:4s} {'yes' if r['finishes'] else 'NO':8s} {r['traced']}/{r['numbers']:<13d} {'yes' if r['correct'] else 'no':14s}  {reading}")
    print("lesson: score the analysis, not only the answer; a report can be right for the wrong reason.")
    write("reexecution.json", {"demo": "demo-61-reexecution-checks", "rows": rows})


if __name__ == "__main__":
    main()
