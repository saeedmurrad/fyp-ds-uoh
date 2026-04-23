# Results (generated outputs)

Training notebooks should write **metrics** and **figures** here (or, on Kaggle, to `/kaggle/working/results/` — see `src/paths.py`).

## From the thesis (PDF), committed in Git

The thesis report stores confusion matrices as **numeric tables** (Ch. 6, Tables 3–5), not as separate image files. The following heatmaps are **rebuilt from those exact counts** and checked in so the repo has figures that match the PDF:

| File | Source in `report/DR_thesis_updated_23081869.pdf` |
|------|--------------------------------------------------|
| `cm_thesis_MobileNetV2.png` | Table 3 (340 / 101 / 93 / 66) |
| `cm_thesis_EfficientNetB0.png` | Table 4 (334 / 107 / 82 / 77) |
| `cm_thesis_ResNet50.png` | Table 5 (326 / 115 / 71 / 88) |

Regenerate (e.g. after a style change): `python scripts/render_thesis_confusion_matrices.py` from the repository root.

**Layout:** rows = *actual* (No DR, DR), columns = *predicted* (No DR, DR), as in the thesis and the training notebook.

## From a local / Kaggle training run (not committed by default)

| Pattern | Description |
|--------|-------------|
| `model_comparison_results_224.csv` | Test-set comparison (accuracy, precision, recall, F1, AUC) for the three models. |
| `bar_accuracy.png`, `bar_precision.png`, `bar_recall.png`, `bar_f1.png` | Metric bar charts. |
| `cm_*.png` (without `thesis` in the name) | Confusion matrices saved when you run `notebooks/dr-detection-training-final_updated.ipynb`. |

Reproduce a full training run: run that notebook from `notebooks/` (see `notebooks/README.md`).

**Git:** ad-hoc run outputs stay ignored; `cm_thesis_*.png` and this `README` are exceptions so thesis-aligned figures are versioned.
