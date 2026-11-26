"""Tests for Demo 89: the mechanism's expected behaviour on the synthetic fixture."""
import json
import os
import subprocess
import sys

DEMO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEMO_DIR, "student"))
import divergence as m  # noqa: E402


def run():
    return subprocess.run([sys.executable, os.path.join("student", "divergence.py")],
                          cwd=DEMO_DIR, capture_output=True, text=True)


def test_runs_and_is_deterministic():
    a, b = run(), run()
    assert a.returncode == 0, a.stderr
    assert a.stdout == b.stdout


def test_results_file_written():
    run()
    with open(os.path.join(DEMO_DIR, "results", "divergence.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["demo"] == "demo-89-schema-divergence"


def test_controls_agree():
    rows = {r["id"]: r for r in m.probe(m.load())}
    assert not rows["p1"]["diverge"] and not rows["p7"]["diverge"]


def test_divergent_dimensions():
    rows = m.probe(m.load())
    assert sorted(r["dimension"] for r in rows if r["diverge"]) == sorted(
        ["type coercion", "bounds", "enum case", "undeclared keyword", "nullability", "type coercion"])
