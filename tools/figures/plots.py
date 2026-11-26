"""Figure 2 of every teaching demo: the worked example on the synthetic fixture.

Small, reusable plot primitives in the repository style: L-shaped axes, values printed
on the marks, thresholds as dashed red lines labelled at their end, verdicts written as
text (never colour alone: failures are also hatched or labelled).
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from style import FS_NOTE, FS_PANEL, FS_TICK, INK, MUTED, PALETTE, WIDTH_IN, apply

KIND = {
    "good": PALETTE["defender"], "bad": PALETTE["adversary"], "env": PALETTE["env"],
    "agent": PALETTE["agent"], "neutral": PALETTE["infra"],
}
HATCH = {"bad": "////"}


def panels(n=1, height=2.4, widths=None, titles=None):
    apply()
    fig, axes = plt.subplots(1, n, figsize=(WIDTH_IN, height),
                             gridspec_kw={"width_ratios": widths} if widths else None)
    axes = [axes] if n == 1 else list(axes)
    for i, ax in enumerate(axes):
        if titles:
            ax.set_title(f"({chr(97 + i)}) {titles[i]}" if n > 1 else titles[i], loc="left",
                         fontsize=FS_PANEL, color=INK, pad=8)
    fig.subplots_adjust(wspace=0.38)
    return fig, axes


def _style_bar(b, kind):
    face, edge = KIND.get(kind or "good", KIND["good"])
    b.set_facecolor(face)
    b.set_edgecolor(edge)
    b.set_linewidth(0.9)
    if kind in HATCH:
        b.set_hatch(HATCH[kind])


def threshold(ax, y, label, horizontal=True):
    edge = PALETTE["adversary"][1]
    if horizontal:
        ax.axhline(y, color=edge, lw=0.9, ls=(0, (4, 2)))
        x1 = ax.get_xlim()[1]
        ax.text(x1, y, " " + label, color=edge, fontsize=FS_NOTE, va="center", ha="left")
    else:
        ax.axvline(y, color=edge, lw=0.9, ls=(0, (4, 2)))
        y1 = ax.get_ylim()[1]
        ax.text(y, y1, label, color=edge, fontsize=FS_NOTE, va="bottom", ha="center")


def bars(ax, labels, values, kinds=None, fmt="{:g}", ylabel="", ylim=None, thr=None,
         thr_label=None, notes=None, rotate=0):
    kinds = kinds or ["good"] * len(values)
    bs = ax.bar(range(len(values)), values, width=0.62)
    for b, k in zip(bs, kinds):
        _style_bar(b, k)
    top = max([v for v in values] + [thr or 0] + [1e-9])
    ax.set_ylim(*(ylim or (0, top * 1.22)))
    span = ax.get_ylim()[1] - ax.get_ylim()[0]
    for i, v in enumerate(values):
        txt = fmt.format(v) + (("\n" + notes[i]) if notes and notes[i] else "")
        if v < 0:
            ax.text(i, v - span * 0.02, txt, ha="center", va="top", fontsize=FS_NOTE, color=INK)
        else:
            ax.text(i, v + span * 0.02, txt, ha="center", va="bottom", fontsize=FS_NOTE, color=INK)
    ax.set_xticks(range(len(values)))
    ax.set_xticklabels(labels, rotation=rotate, ha="right" if rotate else "center")
    ax.set_ylabel(ylabel)
    ax.set_xlim(-0.6, len(values) - 0.4)
    if thr is not None:
        threshold(ax, thr, thr_label or "")
    return ax


def hbars(ax, labels, values, kinds=None, fmt="{:g}", xlabel="", xlim=None, thr=None,
          thr_label=None):
    kinds = kinds or ["good"] * len(values)
    ys = list(range(len(values)))[::-1]
    bs = ax.barh(ys, values, height=0.6)
    for b, k in zip(bs, kinds):
        _style_bar(b, k)
    top = max(list(values) + [thr or 0] + [1e-9])
    ax.set_xlim(*(xlim or (0, top * 1.25)))
    for y, v in zip(ys, values):
        ax.text(v + ax.get_xlim()[1] * 0.015, y, fmt.format(v), va="center", fontsize=FS_NOTE)
    ax.set_yticks(ys)
    ax.set_yticklabels(labels)
    ax.set_xlabel(xlabel)
    if thr is not None:
        threshold(ax, thr, thr_label or "", horizontal=False)
    return ax


def grouped(ax, cats, series, fmt="{:g}", ylabel="", ylim=None, thr=None, thr_label=None,
            legend=True, rotate=0):
    """series: list of (name, values, kind)."""
    n = len(series)
    w = 0.78 / n
    top = 0
    for j, (name, vals, kind) in enumerate(series):
        xs = [i - 0.39 + w * (j + 0.5) for i in range(len(cats))]
        bs = ax.bar(xs, vals, width=w * 0.92, label=name)
        for b in bs:
            _style_bar(b, kind)
        top = max([top] + list(vals))
        for x, v in zip(xs, vals):
            ax.text(x, v, fmt.format(v), ha="center", va="bottom", fontsize=FS_NOTE - 0.5)
    lo, hi = ylim or (0, max(top, thr or 0) * 1.25 + 1e-9)
    ax.set_ylim(lo, hi + (hi - lo) * (0.22 if legend else 0))
    ax.set_xticks(range(len(cats)))
    ax.set_xticklabels(cats, rotation=rotate, ha="right" if rotate else "center")
    ax.set_ylabel(ylabel)
    if thr is not None:
        threshold(ax, thr, thr_label or "")
    if legend:
        ax.legend(loc="upper left", ncol=n, frameon=False, handlelength=1.2,
                  borderaxespad=0.2, columnspacing=1.0, fontsize=FS_TICK)
    return ax


def strip(ax, cols, rows, col_title=None):
    """A case-outcome grid. rows: list of (row_label, [(text, kind), ...]).

    Every cell carries its verdict as text; colour only repeats it."""
    nr, nc = len(rows), len(cols)
    for r, (label, cells) in enumerate(rows):
        y = nr - 1 - r
        ax.text(-0.15, y + 0.5, label, ha="right", va="center", fontsize=FS_TICK, color=INK)
        for c, (text, kind) in enumerate(cells):
            face, edge = KIND.get(kind, KIND["neutral"])
            ax.add_patch(Rectangle((c + 0.05, y + 0.08), 0.9, 0.84, fc=face, ec=edge, lw=0.8,
                                   hatch=HATCH.get(kind)))
            ax.text(c + 0.5, y + 0.5, text, ha="center", va="center", fontsize=FS_NOTE - 0.3,
                    color=edge, fontweight="bold" if kind == "bad" else "normal",
                    bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.9) if kind == "bad" else None)
    rotated = any(len(str(n).split("\n")[0]) > 6 for n in cols) and nc > 4
    for c, name in enumerate(cols):
        ax.text(c + 0.5, nr + 0.12, name, ha="center", va="bottom", fontsize=FS_TICK,
                color=MUTED, rotation=30 if rotated else 0)
    if rotated:
        ax.title.set_y(1.32)
    ax.set_xlim(-0.05, nc + 0.05)
    ax.set_ylim(-0.05, nr + 0.7)
    ax.axis("off")
    if col_title:
        ax.text(nc / 2, nr + 0.62, col_title, ha="center", va="bottom", fontsize=FS_TICK, color=MUTED)
    return ax


def note(ax, x, y, text, xy=None, color=MUTED):
    """Annotation in white space with a thin leader."""
    if xy is None:
        ax.text(x, y, text, fontsize=FS_NOTE, color=color)
    else:
        ax.annotate(text, xy=xy, xytext=(x, y), fontsize=FS_NOTE, color=color,
                    arrowprops=dict(arrowstyle="-", lw=0.6, color=color))
