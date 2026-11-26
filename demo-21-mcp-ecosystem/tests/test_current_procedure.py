"""Tests for the current-procedure step of Demo 21 (synthetic fixture)."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import registry_hosting as cp  # noqa: E402


def _run():
    return subprocess.run([sys.executable, os.path.join("student", "registry_hosting.py")], cwd=DEMO_DIR,
                          capture_output=True, text=True)


def test_current_procedure_runs_deterministically():
    a, b = _run(), _run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout
    with open(os.path.join(DEMO_DIR, "results", "registry_hosting.json"), encoding="utf-8") as fh:
        assert json.load(fh)["demo"].startswith("demo-21")


def test_analysis():
    a = cp.analyse(cp.load())
    assert a["transitions"] == 7 and a["within_24h"] == 4
    assert [c["bump"] for c in a["url_changes"]] == ["patch", "patch"]
    assert [c["cross_domain"] for c in a["url_changes"]] == [True, False]
