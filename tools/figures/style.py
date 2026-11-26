"""Shared figure style for the teaching demos.

One semantic palette for every figure in the repository (pale fills, crisp strokes):
blue = defender, gate, verifier or verdict; red = adversary, failure or hazard;
green = environment, data or corpus; peach = agent, model or estimator;
grey = infrastructure, scope or "not modelled". Dashed lines always carry a
stated meaning: dashed red = adversarial path; dashed grey = scope or trust domain;
dashed red horizontal line in a plot = registered threshold.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PALETTE = {
    "defender": ("#DCE8F6", "#1F4E8C"),
    "adversary": ("#F8DEDC", "#A3241B"),
    "env": ("#E3F1E1", "#2E6B30"),
    "agent": ("#FBE8D6", "#9A5414"),
    "infra": ("#EEEEEE", "#5A5A5A"),
    "verdict": ("#DCE8F6", "#1F4E8C"),
}
INK = "#222222"
MUTED = "#555555"
GOOD = PALETTE["defender"]
BAD = PALETTE["adversary"]
NEUTRAL = PALETTE["infra"]

FONT = "DejaVu Sans"
MONO = "DejaVu Sans Mono"
FS_ROLE = 8.0
FS_LAW = 7.4
FS_NOTE = 7.0
FS_FLOW = 7.0
FS_AXIS = 7.5
FS_TICK = 7.0
FS_PANEL = 8.0

WIDTH_IN = 7.0  # print width: the full text width of a two-column page


def apply():
    plt.rcParams.update({
        "font.family": FONT,
        "font.size": FS_AXIS,
        "axes.titlesize": FS_PANEL,
        "axes.labelsize": FS_AXIS,
        "xtick.labelsize": FS_TICK,
        "ytick.labelsize": FS_TICK,
        "legend.fontsize": FS_TICK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
        "axes.edgecolor": INK,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "svg.fonttype": "path",
        "svg.hashsalt": "agentic-security-demos",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "figure.dpi": 100,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.04,
    })


PREVIEW_DIR = None  # set to a directory to also write PNG previews for visual checks


def save(fig, path):
    """Write a deterministic SVG (no timestamp, no user or machine names)."""
    fig.savefig(path, format="svg", metadata={"Date": None, "Creator": None})
    if PREVIEW_DIR:
        import os
        name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(path))))
        fig.savefig(os.path.join(PREVIEW_DIR, name + "_" + os.path.basename(path)[:-4] + ".png"), dpi=200)
    plt.close(fig)
