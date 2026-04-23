# Deep learning for diabetic retinopathy (retinal fundus images)

MSc Data Science project: **binary detection** of diabetic retinopathy (No DR vs DR present) using **transfer learning** (MobileNetV2, EfficientNetB0, ResNet50) on the [Kaggle EyePACS](https://www.kaggle.com/c/diabetic-retinopathy-detection) data. A five-class label is **collapsed to binary** for the main experiment; EDA in the report uses the full severity distribution.

**Author:** Saeed Murrad  
**Thesis (PDF):** `report/DR_thesis_updated_23081869.pdf`  
**Repository:** [github.com/saeedmurrad/fyp-ds-uoh](https://github.com/saeedmurrad/fyp-ds-uoh)

---

## Quick start

```bash
git clone https://github.com/saeedmurrad/fyp-ds-uoh.git
cd fyp-ds-uoh
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

1. Add Kaggle `train` images and `trainLabels.csv` under `data/` (see `data/README.md`).
2. Open `notebooks/dr-detection-training-final_updated.ipynb` in Jupyter/VS Code.
3. Run from the **repo root** (or on Kaggle with competition data attached). Trained **metrics and figures** are written to **`results/`** (see `results/README.md`).

On **Kaggle**, the notebook’s **OUTPUT DIRS** cell points to `/kaggle/working/results` so you can download CSVs and PNGs from the Output tab.

---

## Repository map

```text
fyp-ds-uoh/
├── data/           # Local dataset (git-ignored; README explains layout)
├── docs/           # ARCHITECTURE.md
├── models/         # Trained .keras files (git-ignored) + model comparison docs
├── notebooks/      # All experiments; README in folder indexes notebooks
│   ├── final/      # Thesis-tagged copy of the main training notebook
│   └── dr-detection-training-final_updated.ipynb
├── report/         # Thesis PDF
├── results/        # Run outputs: CSV + plots (git-ignored)
├── scripts/        # Helper scripts
├── src/            # `paths.py` (results / models / project root)
├── requirements.txt
├── LICENSE
└── README.md
```

More detail: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

## Results and model artifacts

- **`results/`** — After a full run: `model_comparison_results_224.csv`, `bar_*.png`, `cm_*.png`.  
- **`models/`** — Optional saved weights; naming and **reported test metrics** (Table 1) are documented in `models/README.md`.

Generated files stay **out of Git** (see `.gitignore`); commit only code and these READMEs.

---

## License

[MIT](LICENSE) — 2026 Saeed Murrad

---

## Future work

- Backbone fine-tuning, ensembles, Grad-CAM  
- Multi-class severity again or deployment as a tool
