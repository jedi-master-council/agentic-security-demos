"""Tests for Demo 65: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import bibliometrics as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "bibliometrics.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "bibliometrics.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-65-community-bibliometrics"


def test_shared_authors():
    ws = m.load()["works"]
    S, E = m.sets(ws)
    assert sorted(m.authors_of(ws, S) & m.authors_of(ws, E)) == ["Cedar"]
