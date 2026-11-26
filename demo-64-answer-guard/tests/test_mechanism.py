"""Tests for Demo 64: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import guard as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "guard.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "guard_calibration.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-64-answer-guard"


def test_tradeoff():
    d = m.load()
    lo, hi = m.at_threshold(d["replies"], 0.3), m.at_threshold(d["replies"], 0.9)
    assert lo["leak_rate"] < hi["leak_rate"]
    assert lo["over_blocking"] > hi["over_blocking"]
