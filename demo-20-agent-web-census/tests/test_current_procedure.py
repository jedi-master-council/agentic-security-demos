"""Tests for the current-procedure step of Demo 20 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import soft404_gate as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "soft404_gate.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "soft404_gate.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-20")


def test_gate():
    assert cp.gate("# Title") == "agent-file"
    assert cp.gate("<!DOCTYPE html><html>") == "soft-404"


def test_naive_overstates_adoption():
    data = cp.load()
    n200 = sum(r["status"] == 200 for r in data["records"])
    files = sum(r["status"] == 200 and cp.gate(r["body"]) == "agent-file" for r in data["records"])
    assert (n200, files) == (10, 4)
