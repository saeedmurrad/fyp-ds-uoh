#!/usr/bin/env python3
"""Insert RESULTS_DIR cell and save figures/CSVs to results/. Run: python scripts/patch_notebook_outputs.py"""

from __future__ import annotations

import json
from pathlib import Path

PATHS_SOURCE = """# =========================================================
# OUTPUT DIRS (repo `results/`, or `/kaggle/working` on Kaggle)
# =========================================================
import sys
from pathlib import Path

def _init_output_dirs():
    for base in (Path.cwd(), *Path.cwd().parents):
        if (base / "src" / "paths.py").is_file():
            if str(base) not in sys.path:
                sys.path.insert(0, str(base))
            try:
                from src.paths import results_dir, models_dir

                return results_dir(), models_dir()
            except Exception:
                break
    r = (
        Path("/kaggle/working") / "results"
        if Path("/kaggle/working").is_dir()
        else Path.cwd() / "results"
    )
    m = (
        Path("/kaggle/working") / "models"
        if Path("/kaggle/working").is_dir()
        else Path.cwd() / "models"
    )
    r.mkdir(parents=True, exist_ok=True)
    m.mkdir(parents=True, exist_ok=True)
    return r, m

RESULTS_DIR, MODELS_DIR = _init_output_dirs()
print("Results ->", RESULTS_DIR)
print("Models   ->", MODELS_DIR)
"""


def cell_string(cell: dict) -> str:
    src = cell.get("source", "")
    if isinstance(src, list):
        return "".join(src)
    return str(src)


def set_cell_string(cell: dict, text: str) -> None:
    if not text.endswith("\n") and text:
        text = text + "\n"
    cell["source"] = [ln for ln in text.splitlines(keepends=True)]


def patch_text(t: str) -> str:
    t = t.replace(
        'results_df.to_csv("model_comparison_results_224.csv", index=False)',
        'results_df.to_csv(RESULTS_DIR / "model_comparison_results_224.csv", index=False)',
    )
    t = t.replace(
        "plt.xlabel(\"Models\")\nplt.ylabel(\"Accuracy\")\nplt.ylim(0, 1)\nplt.grid(axis=\"y\", linestyle=\"--\", alpha=0.5)\nplt.show()",
        "plt.xlabel(\"Models\")\nplt.ylabel(\"Accuracy\")\nplt.ylim(0, 1)\nplt.grid(axis=\"y\", linestyle=\"--\", alpha=0.5)\nplt.tight_layout()\nplt.savefig(RESULTS_DIR / \"bar_accuracy.png\", dpi=150, bbox_inches=\"tight\")\nplt.show()",
    )
    t = t.replace(
        "plt.xlabel(\"Models\")\nplt.ylabel(\"Precision\")\nplt.ylim(0, 1)\nplt.grid(axis=\"y\", linestyle=\"--\", alpha=0.5)\nplt.show()",
        "plt.xlabel(\"Models\")\nplt.ylabel(\"Precision\")\nplt.ylim(0, 1)\nplt.grid(axis=\"y\", linestyle=\"--\", alpha=0.5)\nplt.tight_layout()\nplt.savefig(RESULTS_DIR / \"bar_precision.png\", dpi=150, bbox_inches=\"tight\")\nplt.show()",
    )
    t = t.replace(
        "plt.xlabel(\"Models\")\nplt.ylabel(\"Recall\")\nplt.ylim(0, 1)\nplt.grid(axis=\"y\", linestyle=\"--\", alpha=0.5)\nplt.show()",
        "plt.xlabel(\"Models\")\nplt.ylabel(\"Recall\")\nplt.ylim(0, 1)\nplt.grid(axis=\"y\", linestyle=\"--\", alpha=0.5)\nplt.tight_layout()\nplt.savefig(RESULTS_DIR / \"bar_recall.png\", dpi=150, bbox_inches=\"tight\")\nplt.show()",
    )
    t = t.replace(
        "plt.xlabel(\"Models\")\nplt.ylabel(\"F1-Score\")\nplt.ylim(0, 1)\nplt.grid(axis=\"y\", linestyle=\"--\", alpha=0.5)\nplt.show()",
        "plt.xlabel(\"Models\")\nplt.ylabel(\"F1-Score\")\nplt.ylim(0, 1)\nplt.grid(axis=\"y\", linestyle=\"--\", alpha=0.5)\nplt.tight_layout()\nplt.savefig(RESULTS_DIR / \"bar_f1.png\", dpi=150, bbox_inches=\"tight\")\nplt.show()",
    )
    t = t.replace(
        "plt.title(f\"Confusion Matrix - {result['model_name']}\")\n    plt.xlabel(\"Predicted Label\")\n    plt.ylabel(\"True Label\")\n    plt.show()",
        "plt.title(f\"Confusion Matrix - {result['model_name']}\")\n    plt.xlabel(\"Predicted Label\")\n    plt.ylabel(\"True Label\")\n    plt.tight_layout()\n    out = RESULTS_DIR / f\"cm_{result['model_name'].replace(' ', '_')}.png\"\n    plt.savefig(out, dpi=150, bbox_inches=\"tight\")\n    plt.show()",
    )
    return t


def patch_path(nb_path: Path) -> None:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    cells: list[dict] = nb["cells"]
    if not any("OUTPUT DIRS" in cell_string(c) and "RESULTS_DIR" in cell_string(c) for c in cells):
        j = 1
        for i, c in enumerate(cells):
            s = cell_string(c).upper()
            if c.get("cell_type") == "code" and "IMPORT LIBRARIES" in s:
                j = i + 1
                break
        ps = PATHS_SOURCE
        if not ps.endswith("\n"):
            ps += "\n"
        cells.insert(
            j,
            {
                "cell_type": "code",
                "metadata": {"trusted": True},
                "source": [ln for ln in ps.splitlines(keepends=True)],
                "outputs": [],
                "execution_count": None,
            },
        )
    for c in cells:
        if c.get("cell_type") != "code":
            continue
        t0 = cell_string(c)
        t1 = patch_text(t0)
        if t1 != t0:
            c.pop("id", None)
            set_cell_string(c, t1)
    nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("Patched", nb_path)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    for name in (
        "notebooks/dr-detection-training-final_updated.ipynb",
        "notebooks/final/dr_binary_detection_thesis_final.ipynb",
    ):
        p = root / name
        if p.is_file():
            patch_path(p)
        else:
            print("missing", p)
