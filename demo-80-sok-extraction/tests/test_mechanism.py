"""Tests for Demo 80: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import extract as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "extract.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "extraction.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-80-sok-extraction"


def test_kappa_identity_and_known_value():
    assert m.cohen_kappa(["a", "b"], ["a", "b"]) == 1.0
    assert abs(m.cohen_kappa(["y", "y", "n", "n"], ["y", "n", "n", "n"]) - 0.5) < 1e-9


def test_field_verdicts():
    rows = m.agreement(m.load())
    assert rows["layer"]["disagreements"] == ["p03"]
    assert rows["layer"]["meets_floor"] is True
    assert rows["adaptive_attack"]["disagreements"] == ["p02", "p07", "p12"]
    assert rows["adaptive_attack"]["meets_floor"] is False
    assert rows["formal_guarantee"]["meets_floor"] is True


def test_low_kappa_despite_high_agreement():
    rows = m.agreement(m.load())
    r = rows["adaptive_attack"]
    assert r["percent_agreement"] >= 0.75 and r["kappa"] < 0.6


def test_map_excludes_unadjudicated():
    grid, pending = m.systematic_map(m.load())
    assert pending == ["p02", "p03", "p07", "p12"]
    assert sum(grid.values()) == 8
