"""Tests for Demo 81: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import harness as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "harness.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "frozen_gate.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-81-frozen-gate"


def test_pin_detects_tampering():
    data = m.load()
    assert m.verify_pin(data)
    data["corpus"][0]["calls"][0] = "read_inbox(all=True)"
    assert not m.verify_pin(data)


def test_rerun_is_byte_identical():
    data = m.load()
    assert m.run_once(data)[1] == m.run_once(data)[1]


def test_confusion():
    data = m.load()
    rows, _ = m.run_once(data)
    assert m.score(data, rows) == {"tp": 3, "fp": 1, "fn": 1, "tn": 3}


def test_benign_with_override_word_not_flagged():
    data = m.load()
    rows, _ = m.run_once(data)
    t6 = [r for r in rows if r["id"] == "t6"][0]
    assert not t6["flag"]
