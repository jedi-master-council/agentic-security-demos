# Teaching-demo figures

Every demo folder carries two figures, referenced from its README under **How it works**:

| File | What it shows | Built from |
|---|---|---|
| `figures/fig1_procedure.svg` | The procedure as numbered stages: role on top, rule or variable beneath (monospace); dashed grey panels mark a trust domain or scope; a dashed red arrow marks where an adversary acts | the demo's entry in `specs_a.py` … `specs_d.py` |
| `figures/fig2_worked_example.svg` | The demo's own output on its synthetic fixture, drawn: values printed on the marks, thresholds as dashed red lines, verdicts written as text (failures are also hatched, never colour alone) | the demo's `results/*.json`, via its adapter in `worked_a.py` … `worked_c.py` |

One semantic palette is used throughout: blue for the defender, gate, verifier or verdict; red for the adversary, failure or hazard; green for data, environment or corpus; peach for an agent, model or estimator; grey for infrastructure, scope or "not modelled". Figures are vector SVG with text drawn as outlines, so they render the same on GitHub and offline, and carry no date, user or machine name.

## Rebuild

```bash
pip install -r tools/figures/requirements.txt   # matplotlib only
make all-demos                                  # writes each demo's results/
python3 tools/figures/build.py                  # all demos, or: python3 tools/figures/build.py 06 14
python3 tools/figures/docs.py                   # refresh the generated README and INSTRUCTIONS blocks
```

`build.py` also writes `captions.json`, the takeaway sentence of every Figure 2, which `docs.py` places under the figure. Set `FIG_PREVIEW_DIR=/some/dir` to write PNG previews for a visual check.

## What the figures deliberately leave out

The demos are simplified from research that is in progress or under peer review. The procedure figures name stages, not corpora, models, thresholds or results, and every number in a worked-example figure comes from the synthetic teaching fixture.
