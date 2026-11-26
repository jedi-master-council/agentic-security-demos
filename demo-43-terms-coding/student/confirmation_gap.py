"""Demo 43, current procedure: state-altering tool schemas checked for a confirmation step.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/confirmation_gap.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "confirmation_gap.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def has_confirmation(params, keywords):
    return any(k in p.lower() for p in params for k in keywords)


def main():
    data = load()
    rows = []
    for t in data["tools"]:
        sa = t["category"] in data["state_altering"]
        rows.append({"tool": t["tool"], "category": t["category"], "state_altering": sa,
                     "confirmation_param": has_confirmation(t["input_params"], data["keywords"])})
    cons = [r for r in rows if r["state_altering"]]
    hooked = sum(r["confirmation_param"] for r in cons)
    for r in rows:
        tag = "state-altering" if r["state_altering"] else "read-only"
        print(f"{r['tool']:16s} {tag:15s} confirmation parameter: {'yes' if r['confirmation_param'] else 'NO' if r['state_altering'] else '-'}")
    print(f"state-altering tools {len(cons)}/{len(rows)}; with a confirmation keyword {hooked}/{len(cons)}; gap {len(cons) - hooked}")
    print("lesson: terms may expect a human to confirm; the schema is where that confirmation would have to live (and a keyword rule misses 'require_approval').")
    write("confirmation_gap.json", {"demo": "demo-43-terms-coding", "rows": rows,
                                    "state_altering": len(cons), "with_confirmation": hooked})


if __name__ == "__main__":
    main()
