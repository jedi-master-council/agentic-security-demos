"""Tests for the current-procedure step of Demo 43 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import confirmation_gap as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "confirmation_gap.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "confirmation_gap.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-43")


def test_gap():
    data = cp.load()
    cons = [t for t in data["tools"] if t["category"] in data["state_altering"]]
    hooked = sum(cp.has_confirmation(t["input_params"], data["keywords"]) for t in cons)
    assert (len(cons), hooked) == (8, 3)
    # "require_approval" does not contain the keyword "approve": a keyword rule is brittle
