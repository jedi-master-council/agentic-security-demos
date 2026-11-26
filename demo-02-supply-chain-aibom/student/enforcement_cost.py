"""Demo 02, current procedure: what a fail-closed supply-chain gate would block across a census of CI configurations.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/enforcement_cost.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "ci_census.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")

import re

PINNED = re.compile(r"@[0-9a-f]{40}$")


def violations(r):
    v = []
    if not all(PINNED.search(a) for a in r["actions"]):
        v.append("R1")
    if r["permissions"] in ("unset", "write-all"):
        v.append("R2")
    if r["pull_request_target_checks_out_head"]:
        v.append("R3")
    return v


def gate(r, waivers):
    """Fail closed: block until every violation is fixed or covered by an approved waiver."""
    open_v = [x for x in violations(r)
              if not any(w["repo"] == r["id"] and w["rule"] == x and w.get("approved_by") for w in waivers)]
    return ("BLOCK" if open_v else "ALLOW"), open_v


def census(data):
    rows = []
    for r in data["repos"]:
        verdict, open_v = gate(r, data["waivers"])
        rows.append({"id": r["id"], "agent_topic": r["agent_topic"], "violations": violations(r),
                     "open": open_v, "verdict": verdict, "blocking_scanner": r["blocking_scanner"]})
    return rows


def main():
    data = load()
    rows = census(data)
    print("repo  agent  violations   after waivers  verdict  already runs a blocking scanner")
    for r in rows:
        print(f"{r['id']:5s} {'yes' if r['agent_topic'] else 'no':5s}  {','.join(r['violations']) or '-':11s}  {','.join(r['open']) or '-':13s}  {r['verdict']:7s}  {'yes' if r['blocking_scanner'] else 'no'}")
    summary = {}
    for grp, flag in (("agent", True), ("comparison", False)):
        g = [r for r in rows if r["agent_topic"] == flag]
        summary[grp] = {"n": len(g), "blocked": sum(r["verdict"] == "BLOCK" for r in g),
                        "blocked_by_R1_only": sum(r["open"] == ["R1"] for r in g),
                        "blocking_scanner": sum(r["blocking_scanner"] for r in g)}
        s = summary[grp]
        print(f"{grp:10s}: blocked {s['blocked']}/{s['n']} (pinning rule alone {s['blocked_by_R1_only']}); configured blocking scanner {s['blocking_scanner']}/{s['n']}")
    print("lesson: a fail-closed gate is cheap to state and expensive to obey; count what it would block before you switch it on.")
    write("enforcement_cost.json", {"demo": "demo-02-supply-chain-aibom", "rows": rows, "summary": summary})


if __name__ == "__main__":
    main()
