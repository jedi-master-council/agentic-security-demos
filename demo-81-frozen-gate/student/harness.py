"""Demo 81 student exercise: Explain why a benchmark harness must be deterministic (the same inputs, the same verdicts, twice).

Fill the marked TODOs; the tests in tests/ encode the expected behaviour."""
import json
import os

FIXTURES = os.path.join(os.path.dirname(__file__), "..", "fixtures", "fixtures.json")


def load():
    with open(FIXTURES, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    data = load()
    # TODO: implement the mechanism per INSTRUCTIONS.md
    raise NotImplementedError("demo-81: implement student/harness.py per INSTRUCTIONS.md")

if __name__ == "__main__":
    main()
