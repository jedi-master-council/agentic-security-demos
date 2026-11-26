"""Demo 04, current procedure: what a reported zero attack-success rate means, read against its exercised denominator and utility.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/zero_audit.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "zero_audit.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def audit(cases, near_zero):
    n = len(cases)
    asr = sum(c["def_hijacked"] for c in cases) / n
    exercised = [c for c in cases if c["undef_hijacked"]]
    util = sum(c["utility"] for c in cases) / n
    if not exercised:
        reading = "nothing to defend: the undefended agent was never hijacked"
    elif len(exercised) <= 1:
        reading = "cannot show a reduction: one exercised case"
    elif util < 0.5:
        reading = "agent stopped doing user tasks: zero reflects lost utility"
    else:
        reading = "defence plausibly worked on the exercised cases"
    return {"n": n, "asr": round(asr, 3), "near_zero": asr <= near_zero,
            "exercised": len(exercised), "utility": round(util, 3), "reading": reading}


def main():
    data = load()
    rows = {k: audit(v, data["near_zero"]) for k, v in sorted(data["releases"].items())}
    print("release  reported ASR  exercised denominator  utility  reading")
    for k, r in rows.items():
        print(f"{k:7s} {r['asr']:12.2f} {r['exercised']:10d}/{r['n']:<10d} {r['utility']:7.2f}  {r['reading']}")
    print("lesson: print the exercised denominator and the utility beside every zero; otherwise a zero has four meanings.")
    write("zero_audit.json", {"demo": "demo-04-authoritybound", "rows": rows})


if __name__ == "__main__":
    main()
