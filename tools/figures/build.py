"""Build Figure 1 (procedure) and Figure 2 (worked example) for every teaching demo.

Run from the repository root after `make all-demos` (Figure 2 reads each demo's results/):
    python3 tools/figures/build.py            # all demos
    python3 tools/figures/build.py 01 14      # selected demos
Writes demo-XX-*/figures/fig1_procedure.svg and fig2_worked_example.svg, and
tools/figures/captions.json (the takeaway sentence of every Figure 2).
"""
import glob
import json
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))

import schematic  # noqa: E402
import specs_a, specs_b, specs_c, specs_d  # noqa: E402

SPECS = {**specs_a.S, **specs_b.S, **specs_c.S, **specs_d.S}
WORKED = {}
for mod in ("worked_a", "worked_b", "worked_c"):
    try:
        WORKED.update(__import__(mod).W)
    except ImportError:
        pass


def demo_dir(n):
    hits = glob.glob(os.path.join(ROOT, f"demo-{n}-*"))
    return hits[0] if hits else None


def main(argv):
    import style
    style.PREVIEW_DIR = os.environ.get("FIG_PREVIEW_DIR")
    keys = argv or sorted(SPECS)
    cap_path = os.path.join(HERE, "captions.json")
    caps = json.load(open(cap_path)) if os.path.exists(cap_path) else {}
    failed = []
    for n in keys:
        d = demo_dir(n)
        if not d:
            continue
        out = os.path.join(d, "figures")
        os.makedirs(out, exist_ok=True)
        try:
            schematic.render(SPECS[n], os.path.join(out, "fig1_procedure.svg"))
            if n in WORKED:
                fig, cap = WORKED[n](d)
                style.save(fig, os.path.join(out, "fig2_worked_example.svg"))
                caps[n] = cap
        except Exception:
            failed.append(n)
            traceback.print_exc()
    with open(cap_path, "w", encoding="utf-8") as fh:
        json.dump(dict(sorted(caps.items())), fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("built", len(keys) - len(failed), "failed", failed)


if __name__ == "__main__":
    main(sys.argv[1:])
