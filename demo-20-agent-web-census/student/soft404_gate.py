"""Demo 20, current procedure: HTTP 200 at an agent-facing path, checked byte by byte for soft-404s.

This step mirrors, in simplified form, how the research procedure for this topic works
today. Synthetic fixture only; standard library; offline; deterministic.
Run from the demo directory: python3 student/soft404_gate.py
"""
import json
import os

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(DEMO_DIR, "fixtures", "soft404_gate.json")
RESULTS = os.path.join(DEMO_DIR, "results")


def load(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(name, obj):
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def gate(body):
    """Byte-level classifier: HTML served at a text path is a soft-404, not an agent file."""
    head = body.lstrip()[:200].lower()
    if head.startswith("<!doctype html") or head.startswith("<html") or "<body" in head:
        return "soft-404"
    if head.startswith("#"):
        return "agent-file"
    return "other"


def main():
    data = load()
    rows, tiers = [], {}
    for r in data["records"]:
        g = gate(r["body"]) if r["status"] == 200 else "no-200"
        rows.append({"host": r["host"], "tier": r["tier"], "status": r["status"], "gate": g})
        t = tiers.setdefault(r["tier"], {"n": 0, "status_200": 0, "agent_file": 0, "soft_404": 0})
        t["n"] += 1
        t["status_200"] += r["status"] == 200
        t["agent_file"] += g == "agent-file"
        t["soft_404"] += g == "soft-404"
    for r in rows:
        print(f"{r['host']} {r['tier']:8s} status {r['status']}  -> {r['gate']}")
    for k, t in sorted(tiers.items()):
        print(f"{k:8s}: naive adoption (200s) {t['status_200']}/{t['n']}  gated adoption {t['agent_file']}/{t['n']}  soft-404 share of 200s {t['soft_404']}/{t['status_200']}")
    print("lesson: a status code is a claim by the server; read the bytes before counting adoption.")
    write("soft404_gate.json", {"demo": "demo-20-agent-web-census", "rows": rows, "tiers": tiers})


if __name__ == "__main__":
    main()
