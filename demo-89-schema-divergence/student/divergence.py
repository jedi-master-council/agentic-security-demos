"""Demo 89 (Tool-Schema Interpretation Divergence): one schema, two validators, and the boundary payloads on which they disagree.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/divergence.py
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


def lenient(schema, args):
    """Framework A: coerces numeric strings and strings, ignores bounds and case, drops unknown keys silently."""
    props = schema["properties"]
    out = {}
    for k, spec in props.items():
        if k not in args:
            if k in schema.get("required", []):
                return "reject", None
            continue
        v = args[k]
        if spec["type"] == "integer":
            if v is None:
                continue
            try:
                v = int(v)
            except (TypeError, ValueError):
                return "reject", None
        if spec["type"] == "string":
            v = str(v)
            if "enum" in spec and v.upper() not in spec["enum"]:
                return "reject", None
            v = v.upper() if "enum" in spec else v
        out[k] = v
    return ("accept-coerced" if out != args else "accept"), out


def strict(schema, args):
    """Framework B: exact types, bounds, enum case and nullability; unknown keys are an error."""
    props = schema["properties"]
    if set(args) - set(props):
        return "reject", None
    for k in schema.get("required", []):
        if k not in args:
            return "reject", None
    for k, v in args.items():
        spec = props[k]
        if v is None:
            return "reject", None
        if spec["type"] == "integer" and (type(v) is not int or v < spec.get("minimum", v)):
            return "reject", None
        if spec["type"] == "string" and (type(v) is not str or ("enum" in spec and v not in spec["enum"])):
            return "reject", None
    return "accept", dict(args)


def probe(data):
    rows = []
    for p in data["payloads"]:
        sc = data["schemas"][p["schema"]]
        a, _ = lenient(sc, p["args"])
        b, _ = strict(sc, p["args"])
        diverge = (a.startswith("accept")) != (b.startswith("accept"))
        rows.append({"id": p["id"], "dimension": p["dimension"], "fw_a": a, "fw_b": b, "diverge": diverge})
    return rows


def main():
    data = load()
    rows = probe(data)
    print(f"{'payload':8s} {'dimension':20s} {'fw-a (lenient)':16s} {'fw-b (strict)':14s} divergent")
    for r in rows:
        print(f"{r['id']:8s} {r['dimension']:20s} {r['fw_a']:16s} {r['fw_b']:14s} {'YES' if r['diverge'] else '-'}")
    n = sum(r["diverge"] for r in rows)
    print(f"divergent payloads {n}/{len(rows)}")
    print("lesson: the same schema is a different gate in each framework; test the gate, not the schema.")
    write("divergence.json", {"demo": "demo-89-schema-divergence", "rows": rows, "n_divergent": n})


if __name__ == "__main__":
    main()
