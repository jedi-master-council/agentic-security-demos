"""Demo 81 (The Frozen Gate Benchmark): a SHA-256-pinned corpus, a frozen two-lexicon gate, and a byte-identical re-run.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/harness.py
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

import hashlib


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def verify_pin(data):
    """Fail closed: the gate refuses to run on a corpus whose hash differs from the manifest."""
    return hashlib.sha256(canon(data["corpus"])).hexdigest() == data["manifest"]["corpus_sha256"]


def gate(traj, lex_a, lex_b):
    """Frozen two-lexicon gate: flag when one call matches the override lexicon and any call
    matches the sink lexicon. Pure function of the text; no model, no randomness."""
    text = [c.lower() for c in traj["calls"]]
    a = any(any(p in c for p in lex_a) for c in text)
    b = any(any(p in c for p in lex_b) for c in text)
    return {"id": traj["id"], "override": a, "sink": b, "flag": a and b}


def run_once(data):
    rows = [gate(t, data["lexicon_override"], data["lexicon_sink"]) for t in data["corpus"]]
    table = canon(rows)
    return rows, hashlib.sha256(table).hexdigest()


def score(data, rows):
    lab = {t["id"]: t["label"] == "injected" for t in data["corpus"]}
    tp = sum(r["flag"] and lab[r["id"]] for r in rows)
    fp = sum(r["flag"] and not lab[r["id"]] for r in rows)
    fn = sum((not r["flag"]) and lab[r["id"]] for r in rows)
    tn = len(rows) - tp - fp - fn
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn}


def main():
    data = load()
    if not verify_pin(data):
        print("REFUSED: corpus hash does not match the manifest (fail closed)")
        sys.exit(2)
    rows1, h1 = run_once(data)
    rows2, h2 = run_once(data)
    print("pin check: corpus SHA-256 matches the manifest")
    print(f"{'traj':5s} override sink  flag")
    for r in rows1:
        print(f"{r['id']:5s} {str(r['override']):8s} {str(r['sink']):5s} {'FLAG' if r['flag'] else '-'}")
    s = score(data, rows1)
    print(f"run 1 table {h1[:16]}  run 2 table {h2[:16]}  byte-identical {h1 == h2}")
    print(f"tp {s['tp']} fp {s['fp']} fn {s['fn']} tn {s['tn']}")
    print("lesson: a frozen gate is reproducible byte for byte; reproducible is not the same as correct.")
    write("frozen_gate.json", {"demo": "demo-81-frozen-gate", "pin_ok": True, "rows": rows1,
                               "table_sha256": h1, "rerun_identical": h1 == h2, "confusion": s})


if __name__ == "__main__":
    main()
