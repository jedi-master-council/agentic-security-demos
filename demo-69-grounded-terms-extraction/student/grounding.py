"""Demo 69 teaching toy: is every extracted access term grounded in its source?

A model (or a person) reads a vendor's terms for an AI service and records five fields:
tier, data use, price, continuity and exit. Each field carries a verbatim quote that is
meant to support it. This toy checks, without any model:

1. the quote exists in the source after whitespace and case normalisation (grounded);
2. the value is consistent with the quote (a number in the value appears in the quote;
   key words of the value appear in the quote);
3. the value matches the hand-labelled gold value (accuracy).

A fabricated quote fails check 1 even when the value happens to be right, which is the
point: a register built from model extraction is only as good as its traceability.
All terms documents and extractions are synthetic.
"""
from __future__ import annotations

import re

FIELDS = ("tier", "data_use", "price", "continuity", "exit")
STOP = {"the", "a", "an", "of", "for", "to", "and", "or", "in", "on", "per", "is", "are", "be", "with", "by"}


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def grounded(quote: str | None, source: str) -> bool:
    return bool(quote) and norm(quote) in norm(source)


def _numbers(text: str) -> set[str]:
    return set(re.findall(r"\d+(?:\.\d+)?", text))


def _words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]+", text.lower()) if w not in STOP and len(w) > 2}


def consistent(value: str | None, quote: str | None) -> bool:
    """Numbers in the value must appear in the quote; most content words must too."""
    if not value or not quote:
        return False
    if not _numbers(value) <= _numbers(quote):
        return False
    words = _words(value)
    return not words or len(words & _words(quote)) / len(words) >= 0.5


def check_extraction(extraction: dict, source: str, gold: dict) -> dict:
    rows = []
    for f in FIELDS:
        item = extraction.get(f) or {}
        value, quote = item.get("value"), item.get("quote")
        rows.append({
            "field": f,
            "present": value is not None,
            "grounded": grounded(quote, source),
            "consistent": consistent(value, quote),
            "correct": value is not None and norm(value) == norm(gold.get(f, "")),
        })
    return {"rows": rows,
            "grounded_share": sum(r["grounded"] for r in rows) / len(rows),
            "accepted": sum(r["grounded"] and r["consistent"] for r in rows)}


def rule_extract(source: str) -> dict:
    """A deliberately simple keyword baseline: take the first sentence mentioning each cue."""
    cues = {"tier": ("plan", "tier"), "data_use": ("train", "data"), "price": ("£", "price", "per user"),
            "continuity": ("notice", "discontinue", "withdraw"), "exit": ("export", "terminat", "delete")}
    sentences = re.split(r"(?<=[.!?])\s+", source.strip())
    out = {}
    for f, words in cues.items():
        hit = next((s for s in sentences if any(w in s.lower() for w in words)), None)
        out[f] = {"value": hit, "quote": hit}
    return out
