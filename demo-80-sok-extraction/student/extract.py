"""Demo 80 (SoK Extraction Protocol): double-coded extraction, agreement per field and a systematic map.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/extract.py
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

FLOOR_FIELD = "kappa_floor"


def cohen_kappa(a, b):
    """Cohen's kappa for two nominal codings of the same items."""
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = sorted(set(a) | set(b))
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def agreement(data):
    ids = sorted(data["coder_a"])
    rows = {}
    for j, field in enumerate(data["fields"]):
        a = [data["coder_a"][i][j] for i in ids]
        b = [data["coder_b"][i][j] for i in ids]
        po = sum(x == y for x, y in zip(a, b)) / len(ids)
        k = cohen_kappa(a, b)
        rows[field] = {"percent_agreement": round(po, 3), "kappa": round(k, 3),
                       "meets_floor": k >= data[FLOOR_FIELD],
                       "disagreements": [i for i, x, y in zip(ids, a, b) if x != y]}
    return rows


def systematic_map(data):
    """Layer x adaptive-attack counts on items where both coders agree on both fields."""
    grid = {}
    pending = []
    for i in sorted(data["coder_a"]):
        a, b = data["coder_a"][i], data["coder_b"][i]
        if a[0] != b[0] or a[2] != b[2]:
            pending.append(i)
            continue
        key = f"{a[0]}|{a[2]}"
        grid[key] = grid.get(key, 0) + 1
    return grid, pending


def main():
    data = load()
    rows = agreement(data)
    grid, pending = systematic_map(data)
    print(f"papers {len(data['coder_a'])}  fields {len(data['fields'])}  kappa floor {data[FLOOR_FIELD]}")
    print(f"{'field':18s} {'agree':>6s} {'kappa':>6s}  floor  disagreements")
    for f, r in rows.items():
        print(f"{f:18s} {r['percent_agreement']:6.2f} {r['kappa']:6.2f}  {'pass' if r['meets_floor'] else 'FAIL'}   {','.join(r['disagreements']) or '-'}")
    print("map (layer | adaptive attack tested):")
    for k in sorted(grid):
        print(f"  {k:28s} {grid[k]}")
    print(f"sent to adjudication: {','.join(pending)}")
    print("lesson: high percent agreement can hide a kappa below the floor when one category dominates.")
    write("extraction.json", {"demo": "demo-80-sok-extraction", "fields": rows, "map": grid,
                              "adjudication": pending})


if __name__ == "__main__":
    main()
