"""Tests for the current-procedure step of Demo 03 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import leakage_rules as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "leakage_rules.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "leakage_rules.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-03")


def test_containment_recovers_planted_items():
    data = cp.load()
    e = cp.evaluate(data, 240)
    assert e["containment_recall"] == 1.0


def test_threshold_does_not_transport():
    data = cp.load()
    small, large = cp.evaluate(data, 25), cp.evaluate(data, 240)
    assert large["containment_fpr"] > small["containment_fpr"]
