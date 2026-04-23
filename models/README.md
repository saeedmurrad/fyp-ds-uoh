# Trained model artifacts (not committed by default)

Store **Keras/TensorFlow** weight files and checkpoints here. Large binaries are ignored by Git (see `.gitignore`); this file documents what belongs in this directory.

## Architectures in this project

Binary DR detection (No DR vs DR) uses **transfer learning** on ImageNet with a **frozen** backbone, **GlobalAveragePooling2D** → **Dropout(0.3)** → **Dense(1, sigmoid)**.

| Backbone | ~Params (ImageNet) | Preprocess | Suggested filename |
|----------|-------------------|------------|-------------------|
| **MobileNetV2** | ~2.2M (trainable top only) | `mobilenet_v2` | `dr_binary_mobilenetv2.keras` |
| **EfficientNetB0** | ~4M+ | `efficientnet` | `dr_binary_efficientnetb0.keras` |
| **ResNet50** | ~23.5M+ (frozen base) | `resnet50` | `dr_binary_resnet50.keras` |

*Parameter counts in the project report (Ch. 5) refer to full backbones; only the new dense head is trained by default.*

## Reported test performance (MSc thesis, Ch. 6, Table 1)

Reference only—your re-run will vary slightly with seeds and Kaggle data snapshot.

| Model | Accuracy | Precision | Recall | F1 |
|--------|:--------:|:---------:|:------:|:--:|
| MobileNetV2 | 0.68 | 0.39 | 0.42 | 0.41 |
| EfficientNetB0 | 0.68 | 0.42 | 0.49 | 0.45 |
| **ResNet50** | **0.69** | **0.44** | **0.56** | **0.49** |

**ResNet50** is the strongest in that experiment (best recall / lowest false negatives among the three). Full details: `../report/DR_thesis_updated_23081869.pdf`.

## Kaggle vs local

- **Local:** files here map to the repository at `fyp-ds-uoh/models/`.
- **Kaggle:** the helper `src/paths.py` can resolve `models_dir()` to `/kaggle/working/models` so you can download weights with the Kaggle “Output” file list.

## Optional: save in a notebook

```python
# After training a `model` in your loop:
# from src.paths import models_dir
# model.save(models_dir() / "dr_binary_resnet50.keras", include_optimizer=True)
```

Use the same name pattern so experiments stay comparable.
