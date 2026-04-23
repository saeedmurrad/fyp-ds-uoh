# Repository architecture

## Layout

| Path | Role |
|------|------|
| `data/` | **Local** raw Kaggle / EyePACS files (not in Git). See `data/README.md`. |
| `notebooks/` | Experiments; production-style flow for binary DR: `dr-detection-training-final_updated.ipynb` and `final/dr_binary_detection_thesis_final.ipynb`. |
| `src/` | Shared Python helpers. `paths.py` exposes `project_root()`, `results_dir()`, `models_dir()`. |
| `results/` | **Outputs** from training: CSV comparison table, bar charts, confusion matrix PNGs. |
| `models/` | **Saved Keras weights** and naming conventions. See `models/README.md`. |
| `report/` | Thesis and PDF deliverables. |
| `scripts/` | Maintenance utilities (e.g. `patch_notebook_outputs.py` for batch notebook edits). |

## Data flow (binary pipeline)

1. **Labels** — Kaggle `trainLabels.csv` (5-class `level`); code maps to **binary** `Label`.
2. **Split** — Stratified train / val / test; **upsampling** on train only.
3. **Models** — MobileNetV2, EfficientNetB0, ResNet50; ImageNet backbone **frozen**; sigmoid head.
4. **Outputs** — Written under `results/` (or `/kaggle/working/results` on Kaggle) so runs do not pollute the repo root.

## Conventions

- **Git** ignores large binaries: `data/*`, `results/*` (except `README` + `.gitkeep`), `models/*` (except `README` + `.gitkeep`).
- **Kaggle** — If the full repo is not in the environment, the notebook’s bootstrap cell still creates `.../results` and `.../models` under `/kaggle/working` for download.

## Reference report

MSc findings and table of metrics: `report/DR_thesis_updated_23081869.pdf` (summary also in `models/README.md`).
