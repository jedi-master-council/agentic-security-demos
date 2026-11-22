"""Demo 86 student exercise: Count personal-data shapes in tool arguments against a registered shape lexicon.

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
    raise NotImplementedError("demo-86: implement student/pii.py per INSTRUCTIONS.md")

if __name__ == "__main__":
    main()
