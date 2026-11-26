"""Tests for Demo 63: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import reliability as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "reliability.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "reliability.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-63-coding-reliability"


def test_alpha_identity():
    assert m.kripp_alpha_nominal([0, 1, 1], [0, 1, 1]) == 1.0


def test_dimensions():
    a = m.per_dimension(m.load())
    assert a["permits_use"] == 1.0 and a["staff_guidance"] == 1.0
    assert a["assessment_rules"] < 0.667


def test_drift():
    assert m.drift(m.load()) == ["u3"]
