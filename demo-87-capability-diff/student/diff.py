"""Demo 87 (Declared versus Actual Capability): static capability extraction from skill handlers, diffed against the declaration in both directions.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/diff.py
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

PATTERNS = {
    "read_file": re.compile(r"open\([^)]*\)\.read\(|open\([^,)]*\)(?!\.write)"),
    "write_file": re.compile(r"open\([^)]*,\s*'[wa]'\)"),
    "run_shell": re.compile(r"subprocess\.|os\.system\("),
    "network_get": re.compile(r"requests\.get\("),
    "network_post": re.compile(r"requests\.post\("),
    "web_search": re.compile(r"requests\.get\('https://search"),
}


def extract(source):
    return sorted(k for k, rx in PATTERNS.items() if rx.search(source))


def diff(skill):
    got = set(extract(skill["source"]))
    dec = set(skill["declared"])
    # A search call is also a network GET; credit the declared name rather than double counting.
    if "web_search" in got:
        got.discard("network_get")
    return {"id": skill["id"], "declared": sorted(dec), "extracted": sorted(got),
            "understated": sorted(got - dec), "overstated": sorted(dec - got)}


def main():
    data = load()
    rows = [diff(s) for s in data["skills"]]
    for r in rows:
        print(f"{r['id']}: declared={r['declared']} extracted={r['extracted']}")
        print(f"     hidden (extracted, not declared) = {r['understated'] or '-'}   unused (declared, not found) = {r['overstated'] or '-'}")
    n_under = sum(bool(r["understated"]) for r in rows)
    n_over = sum(bool(r["overstated"]) for r in rows)
    print(f"skills with hidden capability {n_under}/{len(rows)}; with unused declaration {n_over}/{len(rows)}")
    print("lesson: both directions matter; a hidden capability is a risk, an unused declaration erodes the manifest's meaning.")
    write("capability_diff.json", {"demo": "demo-87-capability-diff", "rows": rows,
                                   "n_understated": n_under, "n_overstated": n_over})


if __name__ == "__main__":
    main()
