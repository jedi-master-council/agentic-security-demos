import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "student"))
from grounding import check_extraction, consistent, grounded, rule_extract


def _docs():
    return json.loads((ROOT / "fixtures" / "terms.json").read_text())["documents"]


def test_fixture_is_labelled_synthetic():
    assert "SYNTHETIC" in json.loads((ROOT / "fixtures" / "terms.json").read_text())["_label"]


def test_whitespace_is_normalised():
    assert grounded("Data   export is available", "Data export is available on request.")


def test_fabricated_quote_is_not_grounded():
    beta = _docs()[1]
    assert grounded(beta["extraction"]["data_use"]["quote"], beta["source"]) is False


def test_number_not_in_quote_is_inconsistent():
    assert consistent("£2 per user per month", "Pricing is negotiated per institution.") is False


def test_clean_extraction_is_fully_accepted():
    alpha = _docs()[0]
    res = check_extraction(alpha["extraction"], alpha["source"], alpha["gold"])
    assert res["accepted"] == 5 and res["grounded_share"] == 1.0


def test_baseline_quotes_are_always_grounded():
    for doc in _docs():
        res = check_extraction(rule_extract(doc["source"]), doc["source"], doc["gold"])
        assert all(r["grounded"] for r in res["rows"] if r["present"])


def test_run_writes_results():
    r = subprocess.run([sys.executable, "student/run_grounding.py"], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert len(json.loads((ROOT / "results" / "grounding.json").read_text())["report"]) == 4
