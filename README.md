# 🛡️ Smart Spam Detection Web App

A Machine Learning-powered web application that detects whether a message is **Spam or Not Spam** using NLP and TF-IDF Vectorization.

---

## 🚀 Live Demo
*(Add your deployed link here after Render deployment)*  
https://your-app-name.onrender.com

---

## 📌 Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning to classify SMS messages as spam or not spam.

It is built using:
- Flask (Backend Web Framework)
- Scikit-learn (Machine Learning)
- TF-IDF Vectorizer (Text Feature Extraction)

---

## 🧠 Model Details

- Algorithm: Naive Bayes / ML Classifier
- Dataset: SMS Spam Collection Dataset (5572 messages)
- Accuracy: ~97.9%
- Features: TF-IDF text representation

---

## 🏗️ Project Structure

smart-spam-detection-app/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── spam.tsv 
│
└── train_model.py 
---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/smart-spam-detection-app.git
cd smart-spam-detection-app