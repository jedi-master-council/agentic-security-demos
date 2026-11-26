"""Tests for Demo 88: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import confusion as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "confusion.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "detection.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-88-detection-confusion"


def test_confusions():
    data = m.load()
    assert m.confusion(data, "taint")["tp"] == 3
    assert m.confusion(data, "mismatch")["fp"] == 0
    u, maj = m.confusion(data, "union"), m.confusion(data, "majority")
    assert u["tpr"] == 1.0 and u["fpr"] > maj["fpr"]


def test_no_detector_alone_is_perfect():
    data = m.load()
    for n in ("taint", "mismatch", "recency"):
        c = m.confusion(data, n)
        assert c["fn"] + c["fp"] > 0
