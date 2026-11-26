"""Tests for Demo 61: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import reexec as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "reexec.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "reexecution.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-61-reexecution-checks"


def test_readings():
    d = m.load()
    rows = {r["id"]: m.check(r, d["data"], d["tolerance"]) for r in d["runs"]}
    assert rows["r1"]["finishes"] is False
    assert rows["r2"]["correct"] and rows["r2"]["traced"] == 3
    assert rows["r3"]["correct"] is False and rows["r3"]["traced"] == 2
    assert rows["r4"]["correct"] and rows["r4"]["traced"] < 3
    assert rows["r6"]["traced"] == 3 and not rows["r6"]["correct"]
