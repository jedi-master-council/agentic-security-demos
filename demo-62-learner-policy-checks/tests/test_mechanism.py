"""Tests for Demo 62: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import policy_checks as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "policy_checks.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "policy_checks.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-62-learner-policy-checks"


def test_checks():
    r = m.evaluate(m.load())
    assert r["invalid"] == ["l04", "l07"]
    assert r["persona_sensitive"] == ["l03", "l08"]
    assert r["brier_policy"] < r["brier_base_rate"] + 0.2
