"""Tests for the current-procedure step of Demo 10 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import blocked_vs_contained as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "blocked_vs_contained.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "blocked_vs_contained.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-10")


def test_blocked_exceeds_contained():
    rows = cp.evaluate(cp.load())
    viol = [r for r in rows if r["out_of_scope"]]
    assert sum(r["verdict"] == "BLOCK" for r in viol) == 4
    assert sum(r["contained"] for r in viol) == 2
    assert {r["id"] for r in rows if r["missed"]} == {"p04", "p09"}
