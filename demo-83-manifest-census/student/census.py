"""Demo 83 (Manifest Census at Registry Scale): description markers, authorisation-metadata gaps and confusable names across two snapshots.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/census.py
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


def edit_distance(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def scan(servers, markers):
    rows = []
    names = [s["name"] for s in servers]
    for s in servers:
        d = s["description"].lower()
        hits = sorted(k for k, pats in markers.items() if any(p in d for p in pats))
        auth_gap = s["remote"] and not s["auth_declared"]
        confusable = sorted(n for n in names if n != s["name"] and edit_distance(n, s["name"]) <= 1)
        rows.append({"id": s["id"], "name": s["name"], "markers": hits, "auth_gap": auth_gap,
                     "confusable_with": confusable})
    return rows


def summary(rows):
    return {"servers": len(rows), "description_flagged": sum(bool(r["markers"]) for r in rows),
            "remote_without_auth": sum(r["auth_gap"] for r in rows),
            "name_confusable": sum(bool(r["confusable_with"]) for r in rows)}


def main():
    data = load()
    out = {"demo": "demo-83-manifest-census", "snapshots": {}}
    for snap, servers in sorted(data["snapshots"].items()):
        rows = scan(servers, data["markers"])
        s = summary(rows)
        out["snapshots"][snap] = {"summary": s, "rows": rows}
        print(f"snapshot {snap}: {s}")
        for r in rows:
            flags = ",".join(r["markers"]) or "-"
            print(f"  {r['id']} {r['name']:15s} markers={flags:28s} auth_gap={'yes' if r['auth_gap'] else 'no':3s} confusable={','.join(r['confusable_with']) or '-'}")
    print("lesson: the description is the only text a client sees before install; scan it, and read auth metadata as a signal, not a guarantee.")
    write("census.json", out)


if __name__ == "__main__":
    main()
