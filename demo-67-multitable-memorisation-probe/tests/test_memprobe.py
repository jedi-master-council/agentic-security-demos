import json, subprocess, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "student"))
from memprobe import FrequencyGuesser, Memoriser, null_threshold, probe, remap


def _data():
    return json.loads((ROOT / "fixtures" / "linked_tables.json").read_text())


def test_fixture_is_labelled_synthetic():
    assert "SYNTHETIC" in _data()["_label"]


def test_remap_keeps_frequencies_and_joins():
    t = _data()["tables"]
    r = remap(t, 1)
    assert sorted(Counter(x["final_result"] for x in t["registrations"]).values()) == \
        sorted(Counter(x["final_result"] for x in r["registrations"]).values())
    left = {x["student_id"] for x in r["students"]}
    assert all(x["student_id"] in left for x in r["registrations"])


def test_frequency_guesser_is_not_flagged():
    d = _data()
    for test in d["tests"]:
        res = probe(lambda shown: FrequencyGuesser(shown), d["tables"], test, 40, 0.05, 67)
        assert res["flagged"] is False


def test_heavily_exposed_memoriser_is_flagged_on_both_tests():
    d = _data()
    pub = d["tables"]
    for test in d["tests"]:
        res = probe(lambda shown: Memoriser(pub, 10, shown), pub, test, 40, 0.05, 67)
        assert res["flagged"] is True


def test_unexposed_memoriser_is_not_flagged():
    d = _data()
    pub = d["tables"]
    res = probe(lambda shown: Memoriser(pub, 0, shown), pub, d["tests"][1], 40, 0.05, 67)
    assert res["flagged"] is False


def test_null_threshold_quantile():
    assert null_threshold([i / 100 for i in range(100)], 0.05) == 0.94


def test_run_writes_results():
    r = subprocess.run([sys.executable, "student/run_memprobe.py"], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert len(json.loads((ROOT / "results" / "memprobe.json").read_text())["rows"]) == 8
