import json, subprocess, sys, random
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "student"))
from qpu_budget import attenuation, fits_device, plan_b1, plan_simulate_first, run_arm, run_job, zne


def _data():
    return json.loads((ROOT / "fixtures" / "battery.json").read_text())


def _inst(data, iid):
    return next(i for i in data["instances"] if i["id"] == iid)


def test_fixture_is_labelled_synthetic():
    assert "SYNTHETIC" in _data()["_label"]


def test_too_deep_job_fails_but_is_charged():
    d = _data()
    job = run_job(_inst(d, "ising-8q-toodeep"), d["device"], 1000, 1, random.Random(0))
    assert job["ok"] is False and job["seconds"] > 0


def test_zne_removes_most_bias_without_shot_noise():
    d = _data()
    inst, dev = _inst(d, "known-8q-mirror"), d["device"]
    e1 = inst["reference"] * attenuation(inst, dev, 1)
    e3 = inst["reference"] * attenuation(inst, dev, 3)
    assert abs(zne(e1, e3) - inst["reference"]) < abs(e1 - inst["reference"])


def test_b1_skips_what_cannot_fit_at_scale_three():
    d = _data()
    assert plan_b1(_inst(d, "ising-8q-deep"), d["device"], d["policy"])["submit"] is False
    assert fits_device(_inst(d, "ising-8q-deep"), d["device"], 1) is True


def test_stand_in_prefers_unmitigated_when_good_enough():
    d = _data()
    plan = plan_simulate_first(_inst(d, "known-4q-ghz"), d["device"], d["policy"])
    assert plan == {"submit": True, "mitigate": False, "shots": d["policy"]["shots"]}


def test_budget_is_never_exceeded():
    d = _data()
    for arm in ("B0", "B1", "A2-stand-in"):
        res = run_arm(arm, d["instances"], d["device"], d["policy"], 66)
        assert res["seconds_spent"] <= d["policy"]["budget_s"]


def test_b0_loses_seconds_to_failed_jobs():
    d = _data()
    res = run_arm("B0", d["instances"], d["device"], d["policy"], 66)
    assert any(r["failed"] for r in res["rows"]) and res["seconds_lost"] > 0


def test_run_writes_results():
    r = subprocess.run([sys.executable, "student/run_qpu_budget.py"], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    out = json.loads((ROOT / "results" / "qpu_budget.json").read_text())
    assert set(out["arms"]) == {"B0", "B1", "A2-stand-in"}
