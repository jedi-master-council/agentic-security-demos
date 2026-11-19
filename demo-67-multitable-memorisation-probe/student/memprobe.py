"""Demo 67 teaching toy: a multi-table memorisation probe and its controls.

All tables and "models" here are synthetic. A model is any function that, given a
partial row (and, for the linked test, a key from another table), guesses a hidden
field. Three toy models are provided:

* ``FrequencyGuesser`` - always guesses the most frequent value; it has seen no rows.
* ``Memoriser`` - recalls the published tables row by row with a recall probability
  that rises with the number of exposures (a stand-in for a model fine-tuned on them).
* ``Remembers nothing`` is the memoriser at zero exposures.

Remapping replaces every identifier and category code with a consistent bijection, so
marginal frequencies and join structure are kept but the literal values a memoriser
could recall are not. Scores on remapped copies form the null distribution, and the
probe flags a model whose score on the published tables exceeds the null's upper
quantile at the registered false-positive rate.
"""
from __future__ import annotations

import hashlib
import random
from collections import Counter


def _h(*parts) -> float:
    digest = hashlib.sha256("|".join(map(str, parts)).encode()).hexdigest()
    return int(digest[:12], 16) / float(16 ** 12)


def remap(tables: dict, seed: int) -> dict:
    """Consistently relabel identifiers and codes in every table (keys stay joinable)."""
    rng = random.Random(seed)
    maps: dict[str, dict] = {}

    def code(field: str, value):
        if field not in maps:
            maps[field] = {}
        m = maps[field]
        if value not in m:
            m[value] = f"{field[:3].upper()}{rng.randrange(10 ** 6):06d}"
        return m[value]

    out = {}
    for name, rows in tables.items():
        out[name] = [{k: code(k, v) for k, v in row.items()} for row in rows]
    return out


class FrequencyGuesser:
    """Guesses the modal value of the target field in whatever table it is shown."""

    def __init__(self, tables: dict):
        self.tables = tables

    def guess(self, table: str, row: dict, target: str):
        counts = Counter(r[target] for r in self.tables[table])
        return counts.most_common(1)[0][0]


class Memoriser:
    """Recalls published rows with probability 1 - (1 - per_exposure) ** exposures.

    It remembers only the published tables, whatever tables it is shown."""

    def __init__(self, published: dict, exposures: int, shown: dict | None = None,
                 per_exposure: float = 0.2, salt: str = "m"):
        self.published = published
        self.p = 1.0 - (1.0 - per_exposure) ** exposures
        self.salt = salt
        # When it cannot recall a row, it falls back on the frequencies of the tables it is shown.
        self.fallback = FrequencyGuesser(shown if shown is not None else published)

    def guess(self, table: str, row: dict, target: str):
        for pub in self.published[table]:
            if all(pub.get(k) == v for k, v in row.items() if k != target):
                if _h(self.salt, table, tuple(sorted(row.items())), target) < self.p:
                    return pub[target]
                break
        return self.fallback.guess(table, row, target)


def row_completion_score(model, tables: dict, table: str, target: str) -> float:
    """Share of rows whose hidden ``target`` field the model reproduces exactly."""
    rows = tables[table]
    hits = 0
    for r in rows:
        shown = {k: v for k, v in r.items() if k != target}
        hits += int(model.guess(table, shown, target) == r[target])
    return hits / len(rows)


def linked_completion_score(model, tables: dict, left: str, right: str, key: str, target: str) -> float:
    """Multi-table test: for each key in ``left``, guess ``target`` from ``right``.

    The model sees only the key. Exact recall across the join is evidence of having
    seen the linked rows, which single-table tests cannot show."""
    right_rows = {r[key]: r for r in tables[right]}
    keys = [r[key] for r in tables[left] if r[key] in right_rows]
    hits = sum(int(model.guess(right, {key: k}, target) == right_rows[k][target]) for k in keys)
    return hits / len(keys)


def null_threshold(scores: list[float], fpr: float) -> float:
    """Upper (1 - fpr) empirical quantile of the null scores (conservative order statistic)."""
    s = sorted(scores)
    idx = min(len(s) - 1, int(-(-(1.0 - fpr) * len(s) // 1)) - 1)
    return s[max(idx, 0)]


def probe(model_factory, published: dict, test: dict, n_remaps: int, fpr: float, seed: int) -> dict:
    """Score a model on the published tables and on ``n_remaps`` remapped copies.

    ``model_factory(tables_shown)`` builds the model for the tables it is shown."""
    def score(tables):
        m = model_factory(tables)
        if test["kind"] == "row":
            return row_completion_score(m, tables, test["table"], test["target"])
        return linked_completion_score(m, tables, test["left"], test["right"], test["key"], test["target"])

    observed = score(published)
    null = [score(remap(published, seed + i)) for i in range(n_remaps)]
    thr = null_threshold(null, fpr)
    return {"observed": round(observed, 4), "null_max": round(max(null), 4),
            "threshold": round(thr, 4), "flagged": observed > thr}
