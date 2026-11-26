"""Demo 03, current procedure: two leakage rules checked against planted items as the reference corpus grows.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/leakage_rules.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "leakage_rules.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def jaccard_whole_corpus(item, reference):
    """Item tokens against the union of all reference tokens (the field's cheap rule)."""
    a, b = set(item), set(t for d in reference for t in d)
    return len(a & b) / len(a | b)


def containment(item, reference):
    """Best per-document share of the item's tokens found in one reference document."""
    a = set(item)
    return max(len(a & set(d)) / len(a) for d in reference)


def evaluate(data, size):
    ref = data["reference"][:size]
    rows = []
    for it in data["items"]:
        j = jaccard_whole_corpus(it["tokens"], ref)
        c = containment(it["tokens"], ref)
        rows.append({"id": it["id"], "planted": it["planted"], "jaccard": round(j, 3),
                     "containment": round(c, 3)})
    planted = [r for r in rows if r["planted"]]
    clean = [r for r in rows if not r["planted"]]
    return {"size": size,
            "jaccard_recall": sum(r["jaccard"] >= data["tau_jaccard"] for r in planted) / len(planted),
            "containment_recall": sum(r["containment"] >= data["tau_containment"] for r in planted) / len(planted),
            "containment_fpr": sum(r["containment"] >= data["tau_containment"] for r in clean) / len(clean),
            "rows": rows}


def main():
    data = load()
    out = []
    print(f"thresholds: whole-corpus Jaccard >= {data['tau_jaccard']}, per-item containment >= {data['tau_containment']}")
    print("reference size  Jaccard recall  containment recall  containment false-positive rate")
    for size in data["reference_sizes"]:
        e = evaluate(data, size)
        out.append({k: v for k, v in e.items() if k != "rows"})
        print(f"{size:14d} {e['jaccard_recall']:15.2f} {e['containment_recall']:19.2f} {e['containment_fpr']:32.2f}")
    print("lesson: a leakage rule must be validated against planted items, and its threshold re-checked when the reference grows.")
    write("leakage_rules.json", {"demo": "demo-03-eval-invariants", "by_size": out})


if __name__ == "__main__":
    main()
