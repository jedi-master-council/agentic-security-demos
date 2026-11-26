"""Demo 85 (The Enforcement Matrix): framework x sink x mode enforcement cells, and whether a token label survives the model.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/matrix.py
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


def matrix(data):
    cells = {}
    for p in data["probes"]:
        status = "enforced" if p["blocked"] else ("documented-only" if p["documented"] else "absent")
        cells[f"{p['framework']}|{p['sink']}|{p['mode']}"] = status
    return cells


def token_label_survives(source, sink):
    """A token-level label survives only if the whole source value appears verbatim at the sink."""
    return source in sink


def survival(data):
    rows = []
    for e in data["label_survival"]:
        rows.append({"id": e["id"], "transform": e["transform"],
                     "survives": token_label_survives(e["source_value"], e["sink_value"])})
    return rows


def main():
    data = load()
    cells = matrix(data)
    for mode in data["modes"]:
        print(f"mode = {mode}")
        print("  " + " " * 6 + "".join(f"{s:>17s}" for s in data["sinks"]))
        for fw in data["frameworks"]:
            print(f"  {fw:6s}" + "".join(f"{cells[f'{fw}|{s}|{mode}']:>17s}" for s in data["sinks"]))
    rows = survival(data)
    by = {}
    for r in rows:
        by.setdefault(r["transform"], []).append(r["survives"])
    print("label survival at the sink:", {k: f"{sum(v)}/{len(v)}" for k, v in by.items()})
    print("lesson: a label that is documented is not a label that is enforced, and a token label rarely survives the model.")
    write("matrix.json", {"demo": "demo-85-enforcement-matrix", "cells": cells, "survival": rows,
                          "survival_by_transform": {k: [sum(v), len(v)] for k, v in by.items()}})


if __name__ == "__main__":
    main()
