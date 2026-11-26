"""Demo 65 (Security-Education Bibliometrics): a two-model screen into two communities and the authors they share.

Teaching toy on synthetic fixtures. Standard library only, offline, deterministic.
Run from the demo directory: python3 student/bibliometrics.py
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


def sets(works):
    S = {w["id"] for w in works if w["label_model_a"] == "S"}
    E = {w["id"] for w in works if w["label_model_a"] == "E"}
    return S, E


def authors_of(works, ids):
    return {a for w in works if w["id"] in ids for a in w["authors"]}


def main():
    d = load()
    ws = d["works"]
    S, E = sets(ws)
    sample = [w for w in ws if w["label_model_b"] is not None]
    agree = sum(w["label_model_a"] == w["label_model_b"] for w in sample)
    shared = sorted(authors_of(ws, S) & authors_of(ws, E))
    print(f"set S (agent security) {len(S)} works; set E (AI in education) {len(E)} works")
    print(f"second-model check on {len(sample)} sampled works: agreement {agree}/{len(sample)}")
    print(f"authors in both communities: {', '.join(shared) or 'none'}")
    print("lesson: a bridge author is a measurable link; a screen is only as good as its second check.")
    write("bibliometrics.json", {"demo": "demo-65-community-bibliometrics", "n_S": len(S), "n_E": len(E),
                                 "sample_agree": [agree, len(sample)], "shared_authors": shared})


if __name__ == "__main__":
    main()
