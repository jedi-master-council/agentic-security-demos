"""Tests for Demo 86: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import pii as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "pii.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "pii_census.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-86-pii-census"


def test_shapes():
    rows, _ = m.census(m.load())
    got = {r["id"]: r["shapes"] for r in rows}
    assert got["c01"] == ["email"]
    assert got["c04"] == ["api_key"]
    assert got["c07"] == ["path_username"]
    assert got["c10"] == ["api_key"]


def test_version_string_false_positive():
    rows, _ = m.census(m.load())
    prec = m.precision_by_family(rows)
    assert prec["ip_address"] == {"tp": 1, "fp": 1}
