import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "student"))
from idfilter import find_spans, redact, score, singles_out


def _data():
    return json.loads((ROOT / "fixtures" / "messages.json").read_text())


def test_fixture_is_labelled_synthetic():
    assert "SYNTHETIC" in _data()["_label"]


def test_plain_identifiers_are_redacted():
    text = "Email alys.p@example.org or call 07700 900123 from ZZ1 1ZZ, number Z1234567."
    out = redact(text, find_spans(text, []))
    assert "[EMAIL]" in out and "[UK_PHONE]" in out and "[UK_POSTCODE]" in out and "[STUDENT_NUMBER]" in out


def test_obfuscated_email_gets_through():
    res = score(_data()["messages"], [p["name"] for p in _data()["roster"]])
    assert any(r["id"] == "m07" and r["type"] == "email" for r in res["residue"])


def test_case_variants_get_through():
    res = score(_data()["messages"], [p["name"] for p in _data()["roster"]])
    leaked = {(r["id"], r["type"]) for r in res["residue"]}
    assert ("m06", "student_number") in leaked and ("m12", "uk_postcode") in leaked


def test_maths_text_is_not_redacted():
    text = "Is the conditional probability 0.25 here? 30 of 120 passed."
    assert find_spans(text, []) == []


def test_quasi_identifiers_single_out_a_unique_learner():
    roster = _data()["roster"]
    assert singles_out({"region": "Scilly", "age_band": "70+"}, roster) is True
    assert singles_out({"region": "North", "age_band": "30-39"}, roster) is False


def test_run_writes_results():
    r = subprocess.run([sys.executable, "student/run_idfilter.py"], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert json.loads((ROOT / "results" / "idfilter.json").read_text())["singled_out"] == ["m09"]
