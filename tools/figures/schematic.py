"""Figure 1 of every teaching demo: the procedure as a numbered storyboard.

A spec is a dict:
  stages : list of (kind, role, law, note)   kind in defender|env|agent|infra
  flows  : list of labels for the arrows between consecutive boxes (len = boxes - 1)
  output : optional (role, law, note) drawn as the final verdict box
  scopes : optional list of (first, last, caption)   dashed grey trust domain/scope
  adversary : optional list of (stage_index, label)  dashed red path into a stage
Boxes carry two layers (role on top, law or variable beneath, in monospace).
Arrows are orthogonal, labelled beside the line, and never cross a box or a label.
"""
import textwrap

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from style import (FONT, FS_FLOW, FS_LAW, FS_NOTE, FS_ROLE, INK, MONO, MUTED,
                   PALETTE, WIDTH_IN, apply, save)

BOX_H = 1.0
GAP_1ROW = 0.62
GAP_2ROW = 0.78
CHANNEL = 0.62
ADV_H = 0.34
ADV_GAP = 0.36
MARGIN = 0.06


def _wrap(text, width_in, fs, mono=False):
    chars = max(6, int(width_in / (fs * (0.0088 if mono else 0.0078))))
    return textwrap.wrap(text, chars) if text else []


def _box(ax, x, y, w, h, kind, role, law, note, number=None):
    face, edge = PALETTE[kind]
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.06",
                                fc=face, ec=edge, lw=1.0))
    head = f"{number}  {role}" if number is not None else role
    lines = textwrap.wrap(head, max(6, int((w - 0.12) / (FS_ROLE * 0.0092))))[:2]
    ty = y + h - 0.13
    for ln in lines:
        ax.text(x + w / 2, ty, ln, ha="center", va="center", fontsize=FS_ROLE,
                fontweight="bold", color=edge, family=FONT)
        ty -= 0.135
    ty -= 0.02
    ax.plot([x + 0.08, x + w - 0.08], [ty + 0.05, ty + 0.05], color=edge, lw=0.5)
    for ln in _wrap(law, w - 0.08, FS_LAW, mono=True)[:2]:
        ty -= 0.075
        ax.text(x + w / 2, ty, ln, ha="center", va="center", fontsize=FS_LAW,
                family=[MONO, FONT], color=INK)
        ty -= 0.06
    ty -= 0.05
    for ln in _wrap(note, w - 0.1, FS_NOTE)[:4]:
        ty -= 0.06
        if ty < y + 0.05:
            break
        ax.text(x + w / 2, ty, ln, ha="center", va="center", fontsize=FS_NOTE,
                color=MUTED, family=FONT)
        ty -= 0.06


def _arrow(ax, pts, color=INK, dashed=False, lw=0.9):
    for (x0, y0), (x1, y1) in zip(pts[:-2], pts[1:-1]):
        ax.plot([x0, x1], [y0, y1], color=color, lw=lw, ls=(0, (3, 2)) if dashed else "-",
                solid_capstyle="butt")
    ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>", mutation_scale=8,
                                 color=color, lw=lw, ls=(0, (3, 2)) if dashed else "-",
                                 shrinkA=0, shrinkB=0))


def render(spec, path):
    apply()
    boxes = [tuple(s)[:4] for s in spec["stages"]]
    if spec.get("output"):
        r, l, n = spec["output"]
        boxes.append(("verdict", r, l, n))
    k = len(boxes)
    two_rows = k >= 5
    per_row = (k + 1) // 2 if two_rows else k
    gap = GAP_2ROW if two_rows else GAP_1ROW
    usable = WIDTH_IN - 2 * MARGIN
    w = (usable - (per_row - 1) * gap) / per_row
    adv = spec.get("adversary") or []
    adv_rows = {(i // per_row) for i, _ in adv}
    top_pad = (ADV_H + ADV_GAP) if 0 in adv_rows else 0.0
    bot_pad = (ADV_H + ADV_GAP) if (1 in adv_rows and two_rows) else 0.0
    scope_pad = 0.24 if spec.get("scopes") else 0.0
    rows = 2 if two_rows else 1
    height = top_pad + scope_pad + rows * BOX_H + (CHANNEL + scope_pad if two_rows else 0) + bot_pad + 0.12
    fig = plt.figure(figsize=(WIDTH_IN, height))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, WIDTH_IN)
    ax.set_ylim(0, height)
    ax.set_aspect("equal")
    ax.axis("off")

    pos = []
    for i in range(k):
        r, c = divmod(i, per_row)
        x = MARGIN + c * (w + gap)
        y = height - top_pad - scope_pad - BOX_H - r * (BOX_H + CHANNEL + scope_pad) - 0.04
        pos.append((x, y))

    segments = []
    for first, last, caption in spec.get("scopes") or []:
        last = min(last, k - 1)
        run = [first]
        for i in range(first + 1, last + 1):
            if i // per_row != run[-1] // per_row:
                segments.append((run[0], run[-1], caption if not any(c == caption for *_, c in segments) else ""))
                run = [i]
            else:
                run.append(i)
        segments.append((run[0], run[-1], caption if not any(c == caption for *_, c in segments) else ""))
    for first, last, caption in segments:
        xs = [pos[i][0] for i in range(first, last + 1)]
        ys = [pos[i][1] for i in range(first, last + 1)]
        x0, x1 = min(xs) - 0.05, max(xs) + w + 0.05
        y0, y1 = min(ys) - 0.05, max(ys) + BOX_H + scope_pad - 0.03
        ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                    boxstyle="round,pad=0,rounding_size=0.08", fc="none",
                                    ec=PALETTE["infra"][1], lw=0.8, ls=(0, (4, 2.5))))
        ax.text(x0 + 0.07, y1 - 0.1, caption, ha="left", va="center", fontsize=FS_NOTE,
                style="italic", color=PALETTE["infra"][1])

    for i, (kind, role, law, note) in enumerate(boxes):
        x, y = pos[i]
        num = i + 1 if kind != "verdict" else None
        _box(ax, x, y, w, BOX_H, kind, role, law, note, number=num)

    flows = spec.get("flows") or []
    for i in range(k - 1):
        (x0, y0), (x1, y1) = pos[i], pos[i + 1]
        label = flows[i] if i < len(flows) else ""
        if abs(y0 - y1) < 1e-6:
            ym = y0 + BOX_H * 0.42
            _arrow(ax, [(x0 + w, ym), (x1, ym)])
            for j, ln in enumerate(_wrap(label, gap - 0.04, FS_FLOW)[:3]):
                ax.text((x0 + w + x1) / 2, ym + 0.1 + 0.115 * (len(_wrap(label, gap - 0.04, FS_FLOW)[:3]) - 1 - j),
                        ln, ha="center", va="bottom", fontsize=FS_FLOW, color=INK)
        else:
            xa = x0 + w / 2
            yc = y0 - (CHANNEL + scope_pad) / 2 - 0.02
            xb = x1 + w / 2
            _arrow(ax, [(xa, y0), (xa, yc), (xb, yc), (xb, y1 + BOX_H)])
            ax.text((xa + xb) / 2, yc + 0.05, label, ha="center", va="bottom",
                    fontsize=FS_FLOW, color=INK)

    for i, label in adv:
        x, y = pos[i]
        aw = min(max(min(w, 1.7), 0.075 * len(label) + 0.2), w + gap * 0.8)
        ax_ = max(MARGIN, min(x + (w - aw) / 2, WIDTH_IN - MARGIN - aw))
        face, edge = PALETTE["adversary"]
        if i // per_row == 0:
            ay = height - ADV_H - 0.04
            ax.add_patch(FancyBboxPatch((ax_, ay), aw, ADV_H, boxstyle="round,pad=0,rounding_size=0.05",
                                        fc=face, ec=edge, lw=0.9))
            ax.text(ax_ + aw / 2, ay + ADV_H / 2, label, ha="center", va="center",
                    fontsize=FS_NOTE, color=edge, fontweight="bold")
            xm = x + w * 0.8
            _arrow(ax, [(xm, ay), (xm, y + BOX_H)], color=edge, dashed=True)
        else:
            ay = 0.06
            ax.add_patch(FancyBboxPatch((ax_, ay), aw, ADV_H, boxstyle="round,pad=0,rounding_size=0.05",
                                        fc=face, ec=edge, lw=0.9))
            ax.text(ax_ + aw / 2, ay + ADV_H / 2, label, ha="center", va="center",
                    fontsize=FS_NOTE, color=edge, fontweight="bold")
            xm = x + w * 0.8
            _arrow(ax, [(xm, ay + ADV_H), (xm, y)], color=edge, dashed=True)
    save(fig, path)


if __name__ == "__main__":
    demo = {
        "stages": [
            ("env", "Declare", "AIBOM: D", "components, tools and capabilities the release claims"),
            ("agent", "Observe", "runtime: R", "capabilities exercised during a run"),
            ("defender", "Compare", "V = R \\ D", "undeclared or denied capabilities"),
            ("defender", "Waive", "w valid(t)", "approved, scoped, time-bounded exceptions"),
        ],
        "flows": ["D", "R", "V", "V minus waived"],
        "output": ("Verdict", "ALLOW | BLOCK", "fail-closed: unknown means block"),
        "scopes": [(2, 4, "release gate (trusted)")],
        "adversary": [(1, "undeclared tool")],
    }
    render(demo, "/tmp/cw/test_fig1.svg")
    print("ok")
