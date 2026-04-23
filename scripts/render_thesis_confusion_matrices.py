#!/usr/bin/env python3
"""
Rebuild confusion-matrix PNGs from values in `report/DR_thesis_updated_23081869.pdf` (Ch. 6, Tables 3–5).
The PDF stores these as tables, not as embedded image objects, so this script recreates the heatmaps.
Run from repo root:  python scripts/render_thesis_confusion_matrices.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Allow import from any cwd
root = Path(__file__).resolve().parent.parent
os.chdir(root)
sys.path.insert(0, str(root))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from src.paths import results_dir

# Rows: actual (No DR, DR); cols: predicted (No DR, DR) — matching the thesis / notebook
MATRICES: dict[str, np.ndarray] = {
    "MobileNetV2": np.array([[340, 101], [93, 66]], dtype=int),
    "EfficientNetB0": np.array([[334, 107], [82, 77]], dtype=int),
    "ResNet50": np.array([[326, 115], [71, 88]], dtype=int),
}


def main() -> None:
    out = results_dir()
    labels = ["No DR", "DR"]
    for name, cm in MATRICES.items():
        fig, ax = plt.subplots(figsize=(5.5, 4.5))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=labels,
            yticklabels=labels,
            ax=ax,
        )
        ax.set(xlabel="Predicted", ylabel="True (actual)")
        ax.set_title(f"{name} — thesis Ch. 6 (test set)", fontsize=12)
        safe = name.replace(" ", "_")
        path = out / f"cm_thesis_{safe}.png"
        fig.tight_layout()
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print("Wrote", path)

    # Combined legend file list for README
    print("Output directory:", out)


if __name__ == "__main__":
    main()
