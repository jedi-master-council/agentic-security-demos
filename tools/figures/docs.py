"""Write the generated "How it works" section into every demo README and a figure step into
every INSTRUCTIONS.md. Re-runnable: the generated blocks are replaced between markers.

    python3 tools/figures/docs.py
"""
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import specs_a, specs_b, specs_c, specs_d  # noqa: E402

SPECS = {**specs_a.S, **specs_b.S, **specs_c.S, **specs_d.S}
CAPS = json.load(open(os.path.join(HERE, "captions.json"), encoding="utf-8"))
B, E = "<!-- BEGIN generated: how-it-works (tools/figures/docs.py) -->", "<!-- END generated: how-it-works -->"
BI, EI = "<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->", "<!-- END generated: figures-step -->"

CURRENT = {"01": "format_effect.py", "02": "enforcement_cost.py", "03": "leakage_rules.py", "04": "zero_audit.py",
           "06": "label_vs_oracle.py", "10": "blocked_vs_contained.py", "16": "relay_control.py",
           "20": "soft404_gate.py", "21": "registry_hosting.py", "43": "confirmation_gap.py"}


def cap_first(s):
    return s[:1].upper() + s[1:] if s else s


def section(n, d):
    s = SPECS[n]
    out = [B, "## How it works", "",
           f'<p align="center"><img src="figures/fig1_procedure.svg" width="100%" alt="Figure 1: the procedure of Demo {n} as numbered stages"></p>', "",
           f"**Figure 1.** {s['cap1']} Numbered boxes are stages (role on top, rule or variable beneath, in monospace); "
           "dashed grey panels mark a trust domain or scope; a dashed red arrow marks where an adversary acts. "
           "Teaching schematic: it simplifies the research procedure and leaves out its corpora, models and thresholds.", "",
           "### Step by step", ""]
    for i, (kind, role, law, note, where) in enumerate(s["stages"], 1):
        txt = (cap_first(note) + ("" if note.endswith(("?", ".")) else ".")) if note else ""
        out.append(f"{i}. **{role}** (`{law}`). {txt} In this demo: `{where}`.".replace("  ", " "))
    if s.get("output"):
        r, l, nt = s["output"]
        out.append(f"{len(s['stages']) + 1}. **{r}** (`{l}`). {cap_first(nt).rstrip('.')}. Run `make demo` to print it.")
    out += ["", f'<p align="center"><img src="figures/fig2_worked_example.svg" width="100%" alt="Figure 2: worked example of Demo {n} on the synthetic fixture"></p>', "",
            f"**Figure 2.** {CAPS.get(n, '')} Values come from `make demo` on the synthetic fixture: they are illustrative "
            "and are not research results.", ""]
    if s.get("new"):
        out += ["### New in this update (26 November 2026)", "",
                "The research procedure for this topic has moved on since the demo was first written. A new step teaches "
                f"the current procedure in simplified form: {s['new'].rstrip('.')}. `make demo` now runs it after the original exercise, "
                "and `tests/test_current_procedure.py` pins its behaviour.", ""]
    out += ["### What the research version adds (withheld while under peer review)", ""]
    out += [f"- {cap_first(a)}" for a in s["adds"]]
    out += ["", "The study's data, exact protocol, thresholds and results are not part of this teaching demo. "
            "They will be linked here once the paper is published open access.", "", E]
    return "\n".join(out)


def insert_readme(path, block):
    txt = open(path, encoding="utf-8").read()
    if B in txt:
        txt = re.sub(re.escape(B) + ".*?" + re.escape(E), lambda m: block, txt, flags=re.S)
    else:
        heads = [m.start() for m in re.finditer(r"^## ", txt, flags=re.M)]
        lo = re.search(r"^## Learning Objectives", txt, flags=re.M)
        pos = None
        if lo:
            nxt = [h for h in heads if h > lo.start()]
            pos = nxt[0] if nxt else len(txt)
        elif heads:
            pos = heads[0]
        else:
            pos = len(txt)
        txt = txt[:pos] + block + "\n\n" + txt[pos:]
    open(path, "w", encoding="utf-8").write(txt)


def run_out(d, script):
    r = subprocess.run([sys.executable, os.path.join("student", script)], cwd=d, capture_output=True, text=True)
    return r.stdout.rstrip()


def instr_block(n, d):
    out = [BI, "## Step F — Read the Figures", "",
           "Open `README.md` and look at the two figures under **How it works**:", "",
           "- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.",
           "- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.", "",
           "To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:", "",
           "```bash", f"make demo DEMO={n}", f"python3 tools/figures/build.py {n}", "```", ""]
    if n in CURRENT:
        out += ["## Step G — Run the Current Procedure (Simplified)", "",
                "The research procedure for this topic has changed since the first version of this demo. This step teaches the current version.", "",
                "```bash", f"python3 student/{CURRENT[n]}", "python3 -m pytest tests/test_current_procedure.py -v", "```", "",
                "**Expected output**:", "", "```text", run_out(d, CURRENT[n]), "```", ""]
    out.append(EI)
    return "\n".join(out)


def insert_instr(path, block):
    txt = open(path, encoding="utf-8").read()
    if BI in txt:
        txt = re.sub(re.escape(BI) + ".*?" + re.escape(EI), lambda m: block, txt, flags=re.S)
    else:
        m = re.search(r"^## (Reproducibility|What to look for|Troubleshooting)", txt, flags=re.M)
        pos = m.start() if m else len(txt)
        txt = txt[:pos].rstrip() + "\n\n---\n\n" + block + "\n\n" + txt[pos:]
    open(path, "w", encoding="utf-8").write(txt)


def main():
    for n in sorted(SPECS):
        hits = glob.glob(os.path.join(ROOT, f"demo-{n}-*"))
        if not hits:
            continue
        d = hits[0]
        insert_readme(os.path.join(d, "README.md"), section(n, d))
        if os.path.exists(os.path.join(d, "INSTRUCTIONS.md")):
            insert_instr(os.path.join(d, "INSTRUCTIONS.md"), instr_block(n, d))
    print("ok")


if __name__ == "__main__":
    main()
