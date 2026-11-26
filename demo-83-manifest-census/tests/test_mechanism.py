"""Tests for Demo 83: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import census as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "census.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "census.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-83-manifest-census"


def test_edit_distance():
    assert m.edit_distance("github", "gihub") == 1
    assert m.edit_distance("abc", "abc") == 0


def test_snapshot_summaries():
    data = m.load()
    s1 = m.summary(m.scan(data["snapshots"]["t1"], data["markers"]))
    s2 = m.summary(m.scan(data["snapshots"]["t2"], data["markers"]))
    assert s1 == {"servers": 8, "description_flagged": 2, "remote_without_auth": 3, "name_confusable": 0}
    assert s2 == {"servers": 10, "description_flagged": 3, "remote_without_auth": 4, "name_confusable": 2}
