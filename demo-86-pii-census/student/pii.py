"""Demo 86 (Personal-Data Exposure Census): a closed five-family shape lexicon over tool-call arguments, per tool class.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/pii.py
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

import re

LEXICON = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone": re.compile(r"\+\d{1,3}(?:[ -]?\d{2,4}){2,4}"),
    "ip_address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "api_key": re.compile(r"\b(?:key-test-[A-Za-z0-9-]{16,}|tok_[A-Za-z0-9]{30,})"),
    "path_username": re.compile(r"(?:/home/|/Users/|C:\\Users\\)[A-Za-z0-9_.-]+"),
}


def classify(args):
    found = sorted(k for k, rx in LEXICON.items() if rx.search(args))
    # The API-key shape contains an @host suffix in c10; an email match inside a token URL is not an address.
    if "api_key" in found and "email" in found and "tok_" in args:
        found.remove("email")
    return found


def census(data):
    rows, per_class = [], {}
    for c in data["calls"]:
        f = classify(c["args"])
        rows.append({"id": c["id"], "tool_class": c["tool_class"], "shapes": f,
                     "truth": data["truth"][c["id"]]})
        for s in f:
            per_class.setdefault(c["tool_class"], {}).setdefault(s, 0)
            per_class[c["tool_class"]][s] += 1
    return rows, per_class


def precision_by_family(rows):
    out = {}
    for fam in LEXICON:
        tp = sum(fam in r["shapes"] and fam in r["truth"] for r in rows)
        fp = sum(fam in r["shapes"] and fam not in r["truth"] for r in rows)
        out[fam] = {"tp": tp, "fp": fp}
    return out


def main():
    data = load()
    rows, per_class = census(data)
    for r in rows:
        mark = "" if r["shapes"] == r["truth"] else "   <- differs from truth"
        print(f"{r['id']} {r['tool_class']:8s} {','.join(r['shapes']) or '-'}{mark}")
    prec = precision_by_family(rows)
    print("per family (tp/fp):", {k: f"{v['tp']}/{v['fp']}" for k, v in prec.items()})
    print("per tool class:", per_class)
    print("lesson: a closed shape lexicon is auditable and reproducible; it still mistakes a version string for an address.")
    write("pii_census.json", {"demo": "demo-86-pii-census", "rows": rows, "per_class": per_class,
                              "per_family": prec})


if __name__ == "__main__":
    main()
