"""Tests for the current-procedure step of Demo 06 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import label_vs_oracle as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "label_vs_oracle.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "label_vs_oracle.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-06")


def test_rankings_disagree():
    data = cp.load()
    r = cp.rates(data["trials"])
    rt = cp.rank({m: v["text"] for m, v in r.items()})
    ro = cp.rank({m: v["oracle"] for m, v in r.items()})
    assert rt["m1"] == 1 and ro["m2"] == 1
    assert cp.kendall_tau(rt, ro) < 0.5
