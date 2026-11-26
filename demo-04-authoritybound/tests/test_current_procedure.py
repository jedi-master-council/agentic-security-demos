"""Tests for the current-procedure step of Demo 04 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import zero_audit as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "zero_audit.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "zero_audit.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-04")


def test_every_release_reports_a_zero():
    data = cp.load()
    assert all(cp.audit(v, data["near_zero"])["near_zero"] for v in data["releases"].values())


def test_readings():
    data = cp.load()
    r = {k: cp.audit(v, data["near_zero"])["reading"].split(":")[0] for k, v in data["releases"].items()}
    assert r["rel-A"].startswith("defence plausibly worked")
    assert r["rel-B"] == "nothing to defend"
    assert r["rel-C"] == "agent stopped doing user tasks"
    assert r["rel-D"] == "cannot show a reduction"
