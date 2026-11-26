"""Tests for the current-procedure step of Demo 01 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import format_effect as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "format_effect.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "format_effect.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-01")


def test_typed_lowers_hit_rate_in_every_configuration():
    data = cp.load()
    for fmts in data["commitments"].values():
        assert cp.hit_rate(fmts["typed"], data["gold"], 3) < cp.hit_rate(fmts["free"], data["gold"], 3)


def test_p_value_floor():
    assert cp.sign_flip_p([-0.2, -0.3, -0.1]) == 0.25


def test_seal_is_order_independent():
    assert cp.seal(["b.py", "a.py"]) == cp.seal(["a.py", "b.py"])
