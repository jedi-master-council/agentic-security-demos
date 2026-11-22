"""Demo 87 student exercise: Diff a skill's declared tool access against its statically extractable capability.

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
    raise NotImplementedError("demo-87: implement student/diff.py per INSTRUCTIONS.md")

if __name__ == "__main__":
    main()
