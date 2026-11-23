"""Demo 83 student exercise: Explain how a registry-scale census classifies manifests against a registered lexicon.

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
    raise NotImplementedError("demo-83: implement student/census.py per INSTRUCTIONS.md")

if __name__ == "__main__":
    main()
