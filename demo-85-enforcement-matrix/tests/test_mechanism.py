"""The mechanism's expected behaviour: the fixtures in, the recorded
verdicts out. The student exercise reproduces this table."""
import json
import os

FIX = os.path.join(os.path.dirname(__file__), "..", "fixtures", "fixtures.json")


def load():
    with open(FIX, encoding="utf-8") as fh:
        return json.load(fh)


def test_fixtures_present():
    data = load()
    assert data, "the fixtures are empty"
