"""Demo 10, current procedure: blocks versus containment under one fail-closed denominator.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/blocked_vs_contained.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "blocked_vs_contained.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def parse_ok(p):
    return bool(p["destination"])


def destination_rule(p, scope):
    """The deterministic guardrail: block unless the destination resolves inside the scope."""
    if not parse_ok(p):
        return "BLOCK"  # fail-closed denominator: unparseable proposals are kept and blocked
    return "ALLOW" if p["resolver_admits"] else "BLOCK"


def evaluate(data):
    rows = []
    for p in data["proposals"]:
        v = destination_rule(p, data["scope"])
        contained = not p["out_of_scope"] or v == "BLOCK"
        restored = False
        if v == "BLOCK" and p.get("follow_up"):
            f = p["follow_up"]
            if destination_rule(f, data["scope"]) == "ALLOW" and f["out_of_scope"]:
                restored = True
                contained = False
        rows.append({"id": p["id"], "verdict": v, "out_of_scope": p["out_of_scope"],
                     "missed": v == "ALLOW" and p["out_of_scope"], "restored_after_block": restored,
                     "contained": contained})
    return rows


def main():
    data = load()
    rows = evaluate(data)
    print("prop  verdict  out-of-scope  outcome")
    for r in rows:
        if not r["out_of_scope"]:
            outcome = "in scope"
        elif r["missed"]:
            outcome = "MISSED: resolver admits the destination"
        elif r["restored_after_block"]:
            outcome = "BLOCKED, then RESTORED by a rewrite"
        else:
            outcome = "blocked and contained"
        print(f"{r['id']:5s} {r['verdict']:8s} {'yes' if r['out_of_scope'] else 'no':12s}  {outcome}")
    viol = [r for r in rows if r["out_of_scope"]]
    blocked = sum(r["verdict"] == "BLOCK" for r in viol)
    contained = sum(r["contained"] for r in viol)
    print(f"out-of-scope proposals {len(viol)} (denominator keeps the unparseable one): blocked {blocked}, contained {contained}")
    print("lesson: count containment, not blocks; a block that the next rewrite undoes contained nothing.")
    write("blocked_vs_contained.json", {"demo": "demo-10-scanbound", "rows": rows,
                                        "violations": len(viol), "blocked": blocked, "contained": contained})


if __name__ == "__main__":
    main()
