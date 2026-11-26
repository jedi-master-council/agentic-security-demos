"""Tests for Demo 82: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import transfer as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "transfer.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "transfer.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-82-score-transfer"


def test_spearman_bounds():
    assert m.spearman([1, 2, 3], [1, 2, 3]) == 1
    assert m.spearman([1, 2, 3], [3, 2, 1]) == -1


def test_ranking_inverts():
    ms = m.load()["models"]
    rho = m.spearman([x["benchmark"] for x in ms], [x["replay_block"] for x in ms])
    assert rho < -0.5


def test_crosstab():
    data = m.load()
    assert m.crosstab(data["models"], data["replay_pass"]) == {
        "top|pass": 0, "top|fail": 3, "bottom|pass": 3, "bottom|fail": 0}
