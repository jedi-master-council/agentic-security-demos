"""Tests for the current-procedure step of Demo 02 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import enforcement_cost as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "enforcement_cost.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "enforcement_cost.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-02")


def test_rules():
    rows = {r["id"]: r for r in cp.census(cp.load())}
    assert rows["a02"]["verdict"] == "ALLOW"
    assert rows["a05"]["violations"] == ["R1", "R2", "R3"]
    assert rows["a04"]["violations"] == ["R2"] and rows["a04"]["verdict"] == "ALLOW"


def test_summary():
    rows = cp.census(cp.load())
    agent = [r for r in rows if r["agent_topic"]]
    assert sum(r["verdict"] == "BLOCK" for r in agent) == 3
