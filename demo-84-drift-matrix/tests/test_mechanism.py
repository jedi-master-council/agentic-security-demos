"""Tests for Demo 84: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import drift as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "drift.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "drift.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-84-drift-matrix"


def test_flags():
    data = m.load()["frameworks"]
    assert [r["flag"] for r in m.transitions(data["fw-a"])] == [False, True, False]
    assert [r["flag"] for r in m.transitions(data["fw-b"])] == [True, False, False]
    assert [r["flag"] for r in m.transitions(data["fw-c"])] == [False, True, False]


def test_elasticity():
    data = m.load()["frameworks"]
    assert m.elasticity(data["fw-a"]) < 1.0 and m.elasticity(data["fw-c"]) < 1.0
    assert m.elasticity(data["fw-b"]) > 1.0
