# Data directory

Place **Kaggle / EyePACS** assets here for local work (e.g. `train/` images and `trainLabels.csv` or `.zip`).

## Expected inputs (typical Kaggle download)

- **`trainLabels.csv`** (or the zipped variant) with columns `image` and `level` (0–4).
- **`train/*.jpeg`** — unzipped retinal fundus files matching the `image` stems.

## Binary task

Notebooks in this project often **collapse** labels to binary: `level == 0` → No DR, `level > 0` → DR present, then balance and split.

## Version control

Large files are **not** committed. Only this README and `.gitkeep` are tracked; see the root `.gitignore`.

## Competition link

- [Kaggle: Diabetic Retinopathy Detection](https://www.kaggle.com/c/diabetic-retinopathy-detection)
