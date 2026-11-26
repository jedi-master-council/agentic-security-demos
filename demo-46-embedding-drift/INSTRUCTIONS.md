# Demo 46 — Execution Instructions

```bash
python3 -m pytest tests/ -v
python3 student/run_drift.py
```

Expected: 4 tests passed. The small swap stays under the frozen mean 0.1222. The orthogonal swap is flagged above it.

---

<!-- BEGIN generated: figures-step (tools/figures/docs.py) -->
## Step F — Read the Figures

Open `README.md` and look at the two figures under **How it works**:

- `figures/fig1_procedure.svg`: the procedure as numbered stages. Match each stage to the file named in the step-by-step list.
- `figures/fig2_worked_example.svg`: the numbers this demo prints, drawn. Check one value in the figure against your own terminal output.

To regenerate both figures after changing a fixture (needs `matplotlib`), from the repository root:

```bash
make demo DEMO=46
python3 tools/figures/build.py 46
```

<!-- END generated: figures-step -->

