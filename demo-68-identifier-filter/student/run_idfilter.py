"""Run the Demo-68 toy: filter scripted learner messages and measure the residue."""

import json
from pathlib import Path
from idfilter import find_spans, redact, score, singles_out

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def main():
    data = json.loads((ROOT / "fixtures" / "messages.json").read_text())
    names = [p["name"] for p in data["roster"]]
    res = score(data["messages"], names)
    for kind, t in sorted(res["per_type"].items()):
        print(f"{kind:<15} gold {t['gold']:>2}  caught {t['caught']:>2}  recall {t['recall']}  precision {t['precision']}")
    print(f"residue (identifiers that got through): {len(res['residue'])}")
    for r in res["residue"]:
        print(f"  {r['id']}  {r['type']:<15} {r['text']!r}")
    single = [m["id"] for m in data["messages"] if singles_out(m["quasi_identifiers_left"], data["roster"])]
    print(f"messages whose remaining quasi-identifiers single out one roster entry: {', '.join(single) or '(none)'}")
    redacted = {m["id"]: redact(m["text"], find_spans(m["text"], names)) for m in data["messages"]}
    out = ROOT / "results" / "idfilter.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"label": "synthetic teaching output, not evidence", **res,
                               "singled_out": single, "redacted": redacted}, indent=2) + "\n")
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
