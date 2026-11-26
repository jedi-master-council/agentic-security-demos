"""Tests for the current-procedure step of Demo 16 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import relay_control as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "relay_control.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "relay_control.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-16")


def test_effects():
    data = cp.load()
    e = {(c["model"], c["arm"]): cp.effect(c, 10) for c in data["cells"]}
    assert e[("m3", "none")] > 0.3
    assert e[("m2", "none")] == 0
    assert all(v < 0 for (m, a), v in e.items() if a == "boundary")
