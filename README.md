<img width="1897" height="767" alt="image" src="https://github.com/user-attachments/assets/9b6aa86c-39ec-4c96-ab2a-052bce43aba9" />

# 🌍 A Comprehensive Measure of Well-Being
### Human Development Index (HDI) Predictor

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle)

**A machine learning web application that predicts a country's Human Development Index score in real time**

[🔮 Predict HDI](#-usage-instructions) · [⚙️ Setup](#️-installation-steps) · [📊 Model](#-model-details) · [👥 Team](#-team-members)


---

## 📌 Abstract

The **Human Development Index (HDI) Predictor** is an end-to-end machine learning web application that predicts the HDI score of any country using four key development indicators:

- 🫀 **Life Expectancy**
- 📚 **Expected Years of Schooling**
- 🎓 **Mean Years of Schooling**
- 💰 **GNI per Capita (PPP $)**

A **Linear Regression model** trained on the UNDP 2021 HDI dataset (191 countries) is deployed via **Flask** with an interactive dark-themed UI, a **live HDI score estimator**, and automatic classification into four development tiers — **Low, Medium, High, and Very High HDI**.

---

## ❗ Problem Statement

No simple, interactive, ML-powered tool exists to predict HDI scores from basic country indicators. Existing resources like UNDP PDF reports require significant time and technical expertise. This project solves that by providing:

- ⚡ Instant HDI prediction from 4 simple inputs
- 🎯 Automatic tier classification (Low / Medium / High / Very High)
- 🌐 A browser-accessible tool requiring zero statistical knowledge

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔮 Real-time HDI Prediction | Predicts HDI score using Linear Regression from 4 indicators |
| 📊 Live Score Estimator | Score updates instantly as user types — no server call needed |
| 🏷️ Auto Classification | Classifies score into Low / Medium / High / Very High HDI |
| 🎨 Interactive Dark UI | Modern gradient design with animated elements |
| 📈 Step Progress Tracker | Animated checkmarks show completed input fields |
| 📉 Per-field Progress Bars | Visual fill bars update as values are entered |
| 🌈 Result Scale Bar | Gradient Low→Very High bar shows where score falls |
| 💾 Model Persistence | Trained model saved as HDI.pkl via Pickle for instant reuse |

---

## 📁 Project Structure

```
AIML-TRACK-_INTERNSHIP/
│
├── Dataset/
│   └── HDI.csv                    ← UNDP HDI Dataset (Kaggle, 191 countries)
│
├── Flask/
│   ├── templates/
│   │   ├── home.html              ← Home page (HDI introduction + category cards)
│   │   ├── indexnew.html          ← Prediction form (live estimator + inputs)
│   │   └── resultnew.html         ← Result page (score + category + scale bar)
│   ├── app.py                     ← Flask backend (routes + prediction logic)
│   └── HDI.pkl                    ← Saved trained model (auto-generated)
│
├── Training/
│   └── HumDevIndex.ipynb          ← Jupyter notebook (Epics 2–7: train → save)
│
├── requirements.txt               ← All dependencies
└── README.md                      ← This file
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | HTML5, CSS3, JavaScript | 3 web pages + live estimator logic |
| **Backend** | Python 3.x, Flask | Routing, form processing, model serving |
| **ML Model** | Scikit-learn (Linear Regression) | HDI score prediction |
| **Data** | Pandas, NumPy | Dataset loading, preprocessing, null handling |
| **Visualization** | Matplotlib, Seaborn | Scatter plots + correlation heatmap |
| **Model Saving** | Pickle | Serialize and load HDI.pkl |
| **IDE** | VS Code, Jupyter Notebook | Development + training |
| **Dataset** | Kaggle (UNDP HDI 2021) | 191 countries × 82 columns |
| **Version Control** | GitHub | Code hosting and submission |

---

## ⚙️ Installation Steps

### Prerequisites
- Python 3.x installed
- VS Code installed
- Git installed

---

### Step 1 — Clone the Repository
```bash
git clone https://github.com/Rohit12223/AIML-TRACK-_INTERNSHIP.git
cd AIML-TRACK-_INTERNSHIP
```

### Step 2 — Install Required Packages
```bash
pip install -r requirements.txt
```

### Step 3 — Download the Dataset
- Go to: [Kaggle HDI Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/human-development-index-dataset)
- Download and extract the ZIP file
- Place the CSV inside the `Dataset/` folder

### Step 4 — Train the Model
Open VS Code → open `Training/HumDevIndex.ipynb` → click **Run All**

This runs all 8 epics in order and auto-generates `Flask/HDI.pkl`

```bash
# OR run from terminal:
cd Training
jupyter notebook HumDevIndex.ipynb
```

### Step 5 — Run the Flask App
```bash
cd Flask
python app.py
```

### Step 6 — Open in Browser
```
http://localhost:5000
```

---

## 📖 Usage Instructions

```
1. Open http://localhost:5000
        ↓
2. Click "Predict HDI Now" on home page
        ↓
3. Enter 4 country indicators:
   • Life Expectancy       → e.g. 72.5   (range: 50–89)
   • Expected Schooling    → e.g. 13.2   (range: 1–18)
   • Mean Schooling        → e.g. 8.5    (range: 1–15)
   • GNI per Capita        → e.g. 15000  (range: 600–75000)
        ↓
4. Watch live score estimator update on left panel
        ↓
5. Click "Predict HDI Score"
        ↓
6. View result: score + category + scale bar
```

---


---

## 🤖 Model Details

| Property | Value |
|----------|-------|
| **Algorithm** | Linear Regression |
| **Dataset** | UNDP HDI 2021 (Kaggle) |
| **Countries** | 191 |
| **Train / Test Split** | 90% / 10% |
| **Random State** | 42 |
| **Input Features** | Life Expectancy, Expected Schooling, Mean Schooling, GNI per Capita |
| **Output** | HDI Score (float, e.g. 0.74) |
| **Model File** | `Flask/HDI.pkl` (Pickle serialization) |

---

## 🎯 HDI Categories

| Score Range | Category | Examples |
|-------------|----------|---------|
| 0.80 – 0.94 | 🟢 **Very High HDI** | Norway, Australia, Germany |
| 0.70 – 0.80 | 🔵 **High HDI** | Brazil, China, Mexico |
| 0.40 – 0.70 | 🟡 **Medium HDI** | India, Ghana, Vietnam |
| 0.30 – 0.40 | 🔴 **Low HDI** | Niger, Chad, Mali |

---

## 📊 Dataset

| Field | Details |
|-------|---------|
| **Name** | Human Development Index Dataset |
| **Source** | Kaggle |
| **Link** | [Human Development Index Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/human-development-index-dataset) | |
| **Year** | 2021 |
| **Rows** | 191 countries |
| **Columns Used** | Life Expectancy, Expected Schooling, Mean Schooling, GNI per Capita, HDI |

---

## 🔮 Future Scope

- ☁️ **Cloud Deployment** — Deploy on Heroku / Render for global access
- 📅 **Updated Data** — Integrate UNDP 2022–2024 HDI data
- 🤖 **Better Models** — Try Random Forest or XGBoost for higher accuracy
- 🌐 **Country Comparison** — Compare HDI scores of 2 countries side by side
- 📈 **Historical Trends** — Line charts showing HDI change over the years
- 📱 **Mobile Responsive** — Optimise UI for phones and tablets
- 🔗 **REST API** — Expose prediction as an API for third-party apps

---

## 👥 Team Members 

| Name | Role | Responsibility |
|------|------|----------------|
| **Rohit Venkata Manikanta Jannu** | 🏆 Team Lead | ML model, Flask backend, Frontend (HTML/CSS), Flask integration, Model evaluation & testing, Overall coordination |
| **Jagan Surya Satish Reddy Medapati** | Member | Dataset collection and preprocessing |

## 📦 Requirements

```txt
numpy
pandas
matplotlib
seaborn
scikit-learn
Flask
jupyter
notebook
```

Install all at once:
```bash
pip install -r requirements.txt
```

---


**Last Updated:** 03 July 2026

## Author

**Rohit Venkata Manikanta Jannu**

**LinkedIn:** [Rohit Venkata Manikanta Jannu](https://www.linkedin.com/in/rohit-venkata-manikanta-jannu-a576a9379)

