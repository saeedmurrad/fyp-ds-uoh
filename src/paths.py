"""
Repository paths: results, models, and project root (local or Kaggle).
Import from notebooks after adding the repo root to `sys.path`.
"""

from __future__ import annotations

import os
from pathlib import Path


def project_root() -> Path:
    """
    Directory that contains `requirements.txt` and `data/`, i.e. the repo root.
    Walks from the current working directory up.
    """
    here = Path.cwd().resolve()
    for p in (here, *here.parents):
        if (p / "requirements.txt").is_file() and (p / "src" / "paths.py").is_file():
            return p
    return here


def is_kaggle() -> bool:
    return os.path.isdir("/kaggle/working") or os.path.isdir("/kaggle/input")


def results_dir() -> Path:
    """
    Where CSVs and figures are written. On Kaggle, uses /kaggle/working/results
    (downloadable) when the project layout is not checked out; otherwise
    <repo>/results.
    """
    if Path("/kaggle/working").is_dir():
        d = Path("/kaggle/working") / "results"
    else:
        d = project_root() / "results"
    d.mkdir(parents=True, exist_ok=True)
    return d


def models_dir() -> Path:
    """
    Trained Keras/TensorFlow weights. Same pattern as `results_dir`.
    """
    if Path("/kaggle/working").is_dir():
        d = Path("/kaggle/working") / "models"
    else:
        d = project_root() / "models"
    d.mkdir(parents=True, exist_ok=True)
    return d


__all__ = ["project_root", "results_dir", "models_dir", "is_kaggle"]
