"""Run the Demo-69 toy: check that extracted access terms are grounded in their source."""

import json
from pathlib import Path
from grounding import check_extraction, rule_extract

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def main():
    data = json.loads((ROOT / "fixtures" / "terms.json").read_text())
    report = []
    for doc in data["documents"]:
        for label, extraction in (("supplied extraction", doc["extraction"]), ("keyword baseline", rule_extract(doc["source"]))):
            res = check_extraction(extraction, doc["source"], doc["gold"])
            report.append({"document": doc["id"], "extractor": label, **res})
            print(f"{doc['id']:<13} {label:<20} grounded {res['grounded_share']:.2f}  accepted fields {res['accepted']}/5")
            for r in res["rows"]:
                if not (r["grounded"] and r["consistent"]):
                    print(f"    {r['field']:<11} grounded={r['grounded']} consistent={r['consistent']} correct={r['correct']}")
    out = ROOT / "results" / "grounding.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"label": "synthetic teaching output, not evidence", "report": report}, indent=2) + "\n")
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
