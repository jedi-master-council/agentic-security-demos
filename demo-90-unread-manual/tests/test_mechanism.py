"""Tests for Demo 90: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import acquisition as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "acquisition.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "context_acquisition.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-90-unread-manual"


def test_exposure_exceeds_acquisition():
    ea = m.exposure_acquisition(m.load())
    assert ea["README"] == {"exposed": 12, "acquired": 3}
    assert ea["AGENTS"]["exposed"] == 6 and ea["AGENTS"]["acquired"] == 2
    assert all(v["acquired"] <= v["exposed"] for v in ea.values())


def test_naive_association_is_negative():
    naive, _, _ = m.outcome(m.load())
    assert naive["readers"] < naive["non_readers"]


def test_within_task_difference_vanishes():
    _, within, pooled = m.outcome(m.load())
    assert pooled == 0.0
    assert within["T2"]["diff"] is None


def test_edit_before_prose():
    data = m.load()
    assert sum(m.edited_before_prose(r, data) for r in data["runs"]) == 8
