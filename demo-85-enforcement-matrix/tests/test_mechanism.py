"""Tests for Demo 85: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import matrix as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "matrix.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "matrix.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-85-enforcement-matrix"


def test_no_native_enforcement():
    cells = m.matrix(m.load())
    assert not any(v == "enforced" for k, v in cells.items() if k.endswith("|native"))


def test_monitor_gap():
    cells = m.matrix(m.load())
    assert cells["fw-b|file_write|monitor"] == "documented-only"
    assert sum(v == "enforced" for k, v in cells.items() if k.endswith("|monitor")) == 8


def test_survival():
    rows = {r["id"]: r["survives"] for r in m.survival(m.load())}
    assert rows == {"e1": True, "e2": True, "e3": False, "e4": False, "e5": False, "e6": False}
