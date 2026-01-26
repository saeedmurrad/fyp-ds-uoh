# 🩺 **Deep Learning for Diabetic Retinopathy Detection Using Retinal Fundus Images**

## 📘 **Project Overview**
This project explores the use of deep learning techniques to automatically detect **Diabetic Retinopathy (DR)** from retinal fundus images. DR is one of the leading causes of preventable blindness worldwide, and early detection plays a crucial role in improving patient outcomes. Using the **EyePACS** dataset from Kaggle, this project evaluates multiple convolutional neural network (CNN) architectures to classify DR severity into five levels.

The work forms part of my **MSc Data Science final project**, combining my background in software engineering with applied machine learning to address a real-world healthcare challenge.

---

## 🎯 **Objectives**
- Build and compare multiple deep learning models for DR detection  
- Analyse performance across the five DR severity classes  
- Evaluate the impact of preprocessing and data augmentation  
- Develop a reproducible training and evaluation pipeline  
- Provide insights into model strengths, weaknesses, and clinical relevance  

---

## 🔍 **Research Questions**
1. **Which deep learning architectures achieve the highest accuracy** in detecting diabetic retinopathy from retinal fundus images?  
2. **How does model performance vary across DR severity levels** (No DR, Mild, Moderate, Severe, Proliferative DR)?  
3. **Do preprocessing and data augmentation techniques improve model performance and generalisation?**

---

## 📊 **Dataset**
**Source:** Kaggle — Diabetic Retinopathy Detection (EyePACS)  
**Link:** `https://www.kaggle.com/c/diabetic-retinopathy-detection` [(kaggle.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.kaggle.com%2Fc%2Fdiabetic-retinopathy-detection")  

**Data Characteristics:**
- High‑resolution retinal fundus images  
- Labels assigned by trained clinicians  
- Five-class classification problem:  
  - 0 — No DR  
  - 1 — Mild  
  - 2 — Moderate  
  - 3 — Severe  
  - 4 — Proliferative DR  

---

## 🧠 **Methodology**
### **1. Preprocessing**
- Image resizing  
- Normalisation  
- Cropping and centering  
- Contrast enhancement (CLAHE)  
- Removal of black borders  

### **2. Data Augmentation**
- Rotation  
- Horizontal/vertical flips  
- Brightness/contrast adjustments  
- Zoom and shift transformations  

### **3. Model Architectures**
- VGG16 / VGG19  
- ResNet50  
- InceptionV3  
- EfficientNetB0–B3  
- Custom CNN baseline  

### **4. Evaluation Metrics**
- Accuracy  
- Precision, Recall, F1‑Score  
- Confusion Matrix  
- AUC‑ROC  
- Class‑wise performance analysis  

---

## 🏗️ **Project Structure**
```
├── data/                 # Dataset (not included in repo)
├── notebooks/            # Jupyter notebooks for EDA and experiments
├── src/                  # Training, preprocessing, and model scripts
├── models/               # Saved model weights
├── results/              # Metrics, plots, confusion matrices
├── README.md             # Project documentation
└── requirements.txt      # Dependencies
```

---

## 🚀 **Key Features**
- End‑to‑end deep learning pipeline  
- Modular and reproducible codebase  
- Multiple model comparisons  
- Visualisation of training curves and class performance  
- Clinically relevant insights into DR detection challenges  

---

## 🎯 **Motivation**
As someone with a personal interest in diabetic health, this project represents more than a technical exercise. It reflects a commitment to exploring AI solutions that can support early detection and improve patient outcomes. Combining my engineering background with healthcare-focused machine learning allows me to contribute to meaningful, real-world impact.

---

## 📌 **Future Work**
- Explainability (Grad‑CAM, saliency maps)  
- Ensemble models  
- Deployment as a web or mobile application  
- Integration with clinical workflows  
