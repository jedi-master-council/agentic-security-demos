"""Demo 68 teaching toy: what a rule-based identifier filter lets through.

A filter sits between a study platform and a hosted language model and replaces common
identifiers in typed learner text before the text leaves the institution. This toy
measures, on scripted synthetic messages with hand-labelled identifier spans:

* span-level recall and precision per identifier type;
* the residue: labelled identifiers that survive filtering, by type;
* re-identification risk from what survives: whether the quasi-identifiers left in a
  message single out one person in a synthetic roster (k = 1).

All messages, names, numbers and the roster are invented. The student-number pattern is
a synthetic format chosen for this toy and is not any institution's real format.
"""
from __future__ import annotations

import re

PATTERNS = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "uk_phone": re.compile(r"(?:(?<=\s)|^)(?:\+44\s?7\d{3}|07\d{3})\s?\d{3}\s?\d{3}\b"),
    "uk_postcode": re.compile(r"\b[A-Z]{1,2}\d[A-Z\d]?\s?\d[A-Z]{2}\b"),
    "student_number": re.compile(r"\bZ\d{7}\b"),
}


def find_spans(text: str, roster_names: list[str]) -> list[dict]:
    """Return non-overlapping detected spans (start, end, type), longest first."""
    spans = []
    for kind, pat in PATTERNS.items():
        for m in pat.finditer(text):
            spans.append({"start": m.start(), "end": m.end(), "type": kind})
    for name in roster_names:
        for m in re.finditer(r"\b" + re.escape(name) + r"\b", text):
            spans.append({"start": m.start(), "end": m.end(), "type": "name"})
    spans.sort(key=lambda s: (s["start"], -(s["end"] - s["start"])))
    kept, last_end = [], -1
    for s in spans:
        if s["start"] >= last_end:
            kept.append(s)
            last_end = s["end"]
    return kept


def redact(text: str, spans: list[dict]) -> str:
    out, pos = [], 0
    for s in spans:
        out.append(text[pos:s["start"]])
        out.append(f"[{s['type'].upper()}]")
        pos = s["end"]
    out.append(text[pos:])
    return "".join(out)


def _overlaps(a: dict, b: dict) -> bool:
    return a["start"] < b["end"] and b["start"] < a["end"]


def score(messages: list[dict], roster_names: list[str]) -> dict:
    """Span-level counts per type: a gold span counts as caught if any detection overlaps it."""
    per = {}
    residue = []
    for msg in messages:
        found = find_spans(msg["text"], roster_names)
        for g in msg["gold"]:
            t = per.setdefault(g["type"], {"gold": 0, "caught": 0, "detected": 0, "correct": 0})
            t["gold"] += 1
            if any(_overlaps(g, f) for f in found):
                t["caught"] += 1
            else:
                residue.append({"id": msg["id"], "type": g["type"], "text": msg["text"][g["start"]:g["end"]]})
        for f in found:
            t = per.setdefault(f["type"], {"gold": 0, "caught": 0, "detected": 0, "correct": 0})
            t["detected"] += 1
            if any(_overlaps(g, f) for g in msg["gold"]):
                t["correct"] += 1
    for t in per.values():
        t["recall"] = round(t["caught"] / t["gold"], 4) if t["gold"] else None
        t["precision"] = round(t["correct"] / t["detected"], 4) if t["detected"] else None
    return {"per_type": per, "residue": residue}


def singles_out(quasi: dict, roster: list[dict]) -> bool:
    """True when the quasi-identifiers left in a message match exactly one roster entry."""
    if not quasi:
        return False
    matches = [p for p in roster if all(p.get(k) == v for k, v in quasi.items())]
    return len(matches) == 1
