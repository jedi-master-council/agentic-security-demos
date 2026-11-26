"""Demo 90 (The Unread Manual): exposure versus acquisition of repository guidance, and a within-task outcome comparison.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/acquisition.py
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


def cls_of(path, classes):
    for c, prefixes in classes.items():
        if any(path == p or path.startswith(p) for p in prefixes):
            return c
    return None


def exposure_acquisition(data):
    """Exposure: the class appears in what the agent saw. Acquisition: the agent opened it."""
    classes = data["classes"]
    out = {c: {"exposed": 0, "acquired": 0} for c in classes}
    for r in data["runs"]:
        seen, opened = set(), set()
        for s in r["steps"]:
            if s["act"] == "ls":
                seen |= {cls_of(p, classes) for p in s["out"]} - {None}
            if s["act"] == "open":
                c = cls_of(s["path"], classes)
                if c:
                    opened.add(c)
                    seen.add(c)
        for c in seen:
            out[c]["exposed"] += 1
        for c in opened:
            out[c]["acquired"] += 1
    return out


def read_prose(run, data):
    return any(s["act"] == "open" and cls_of(s["path"], data["classes"]) in data["prose_classes"]
               for s in run["steps"])


def edited_before_prose(run, data):
    for s in run["steps"]:
        if s["act"] == "edit":
            return True
        if s["act"] == "open" and cls_of(s["path"], data["classes"]) in data["prose_classes"]:
            return False
    return True


def outcome(data):
    """Naive comparison of resolution by prose reading, then the same comparison within each task."""
    rd = [r for r in data["runs"] if read_prose(r, data)]
    nr = [r for r in data["runs"] if not read_prose(r, data)]
    rate = lambda xs: sum(r["resolved"] for r in xs) / len(xs) if xs else None
    naive = {"readers": rate(rd), "non_readers": rate(nr), "n_readers": len(rd), "n_non": len(nr)}
    within = {}
    for t in sorted({r["task"] for r in data["runs"]}):
        a = [r for r in rd if r["task"] == t]
        b = [r for r in nr if r["task"] == t]
        within[t] = {"readers": rate(a), "non_readers": rate(b),
                     "diff": None if not a or not b else rate(a) - rate(b)}
    diffs = [v["diff"] for v in within.values() if v["diff"] is not None]
    pooled = sum(diffs) / len(diffs) if diffs else None
    return naive, within, pooled


def main():
    data = load()
    ea = exposure_acquisition(data)
    print(f"{'class':13s} exposed acquired  rate")
    for c, v in ea.items():
        rate = v["acquired"] / v["exposed"] if v["exposed"] else 0
        print(f"{c:13s} {v['exposed']:7d} {v['acquired']:8d}  {rate:.2f}")
    ebp = sum(edited_before_prose(r, data) for r in data["runs"])
    print(f"runs that edited before reading any prose guidance: {ebp}/{len(data['runs'])}")
    naive, within, pooled = outcome(data)
    print(f"naive: resolved {naive['readers']:.2f} among prose readers vs {naive['non_readers']:.2f} among non-readers")
    for t, v in within.items():
        f = lambda x: "  n/a" if x is None else f"{x:5.2f}"
        print(f"  {t}: readers {f(v['readers'])}  non-readers {f(v['non_readers'])}  difference {f(v['diff'])}")
    print(f"within-task difference (tasks with both groups): {pooled:+.2f}")
    print("lesson: count reads, not mentions; and compare runs on the same task before reading anything into the association.")
    write("context_acquisition.json", {"demo": "demo-90-unread-manual", "exposure_acquisition": ea,
                                       "edited_before_prose": ebp, "n_runs": len(data["runs"]),
                                       "naive": naive, "within_task": within, "within_pooled": pooled})


if __name__ == "__main__":
    main()
