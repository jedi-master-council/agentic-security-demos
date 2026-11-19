"""Run the Demo-67 toy: probe three synthetic models against remapped controls."""

import json
from pathlib import Path
from memprobe import FrequencyGuesser, Memoriser, probe

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def models(published):
    return {
        "frequency-guesser": lambda shown: FrequencyGuesser(shown),
        "memoriser-0-exposures": lambda shown: Memoriser(published, 0, shown),
        "memoriser-3-exposures": lambda shown: Memoriser(published, 3, shown),
        "memoriser-10-exposures": lambda shown: Memoriser(published, 10, shown),
    }


def main():
    data = json.loads((ROOT / "fixtures" / "linked_tables.json").read_text())
    pub, s = data["tables"], data["settings"]
    rows = []
    for test in data["tests"]:
        for name, factory in models(pub).items():
            res = probe(factory, pub, test, s["n_remaps"], s["fpr"], s["seed"])
            rows.append({"test": test["name"], "model": name, **res})
            print(f"{test['name']:<36} {name:<24} observed {res['observed']:.3f}  "
                  f"null threshold {res['threshold']:.3f}  flagged {res['flagged']}")
    out = ROOT / "results" / "memprobe.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"label": "synthetic teaching output, not evidence", "rows": rows}, indent=2) + "\n")
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
