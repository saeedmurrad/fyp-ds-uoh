# **Deep Learning for Diabetic Retinopathy Detection Using Retinal Fundus Images**

## **Project Overview**
This project explores the use of deep learning techniques to automatically detect **Diabetic Retinopathy (DR)** from retinal fundus images. DR is one of the leading causes of preventable blindness worldwide, and early detection plays a crucial role in improving patient outcomes. Using the **EyePACS** dataset from Kaggle, this project evaluates multiple convolutional neural network (CNN) architectures to classify DR severity into five levels.

The work forms part of an **MSc Data Science** final project, combining a software engineering background with applied machine learning to address a real-world healthcare challenge.

---

## **Objectives**
- Build and compare multiple deep learning models for DR detection  
- Analyse performance across the five DR severity classes  
- Evaluate the impact of preprocessing and data augmentation  
- Develop a reproducible training and evaluation pipeline  
- Provide insights into model strengths, weaknesses, and clinical relevance  

---

## **Research Questions**
1. **Which deep learning architectures achieve the highest accuracy** in detecting diabetic retinopathy from retinal fundus images?  
2. **How does model performance vary across DR severity levels** (No DR, Mild, Moderate, Severe, Proliferative DR)?  
3. **Do preprocessing and data augmentation techniques improve model performance and generalisation?**

---

## **Dataset**
**Source:** [Kaggle — Diabetic Retinopathy Detection (EyePACS)](https://www.kaggle.com/c/diabetic-retinopathy-detection)  

**Data characteristics:** high-resolution retinal fundus images, clinician labels, five-class classification (0 — No DR through 4 — Proliferative DR).

---

## **Repository structure**

```
├── data/                 # Local dataset (not in Git; see data/README.md)
├── notebooks/            # Jupyter experiments
├── scripts/              # Optional helper scripts
├── src/                  # Python package for project code
├── models/               # Saved weights (not in Git)
├── results/              # Outputs, plots (not in Git)
├── requirements.txt
├── LICENSE
└── README.md
```

---

## **License**

This project is released under the terms in `LICENSE` (MIT).

**Author —** Saeed Murrad

---

## **Future work**
- Explainability (e.g. Grad-CAM)  
- Ensemble models  
- Deployment (web or mobile)  
- Integration with clinical workflows  
