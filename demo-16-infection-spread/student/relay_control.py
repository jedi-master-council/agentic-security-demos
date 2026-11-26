"""Demo 16, current procedure: instructed markers against uninstructed control codes along a three-agent chain.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/relay_control.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "relay_control.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def effect(c, n):
    """Instruction effect: reach of the instructed marker minus reach of the uninstructed code."""
    return (c["instructed_reached"] - c["control_reached"]) / n


def main():
    data = load()
    n = data["chains_per_cell"]
    rows = []
    print("model arm        instructed  control  instruction effect")
    for c in data["cells"]:
        e = effect(c, n)
        rows.append(dict(c, effect=round(e, 2)))
        print(f"{c['model']:5s} {c['arm']:9s} {c['instructed_reached']:7d}/{n} {c['control_reached']:5d}/{n} {e:+12.2f}")
    print("lesson: compare with an uninstructed code in the same position; most of the 'spread' is ordinary copying, and a boundary mechanism can push the instructed reach below it.")
    write("relay_control.json", {"demo": "demo-16-infection-spread", "rows": rows})


if __name__ == "__main__":
    main()
