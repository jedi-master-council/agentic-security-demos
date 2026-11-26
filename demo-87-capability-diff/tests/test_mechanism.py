"""Tests for Demo 87: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import diff as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "diff.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "capability_diff.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-87-capability-diff"


def test_directions():
    rows = {r["id"]: r for r in (m.diff(s) for s in m.load()["skills"])}
    assert rows["s1"]["understated"] == [] and rows["s1"]["overstated"] == []
    assert rows["s2"]["understated"] == ["run_shell"]
    assert rows["s4"]["understated"] == ["network_post"]
    assert rows["s3"]["overstated"] == ["read_file"]
    assert rows["s6"]["overstated"] == ["network_post"]


def test_counts():
    rows = [m.diff(s) for s in m.load()["skills"]]
    assert sum(bool(r["understated"]) for r in rows) == 2
    assert sum(bool(r["overstated"]) for r in rows) == 2
