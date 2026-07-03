# 🌍 A Comprehensive Measure of Well-Being
## Human Development Index (HDI) Predictor — ML-0027

---

## 📁 Project Structure

```
ML-0027-Human-Development-Index/
├── Dataset/
│   └── HDI.csv                    ← Download from Kaggle and place here
├── Flask/
│   ├── templates/
│   │   ├── home.html              ← Home page
│   │   ├── indexnew.html          ← Prediction input form
│   │   └── resultnew.html         ← Result display page
│   ├── app.py                     ← Flask backend
│   └── HDI.pkl                    ← Generated after running notebook
├── Training/
│   └── HumDevIndex.ipynb          ← Jupyter notebook for ML training
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### Step 1: Install required packages
```bash
pip install numpy pandas matplotlib scikit-learn Flask jupyter notebook
```

### Step 2: Download Dataset
- Download HDI.csv from:
  https://github.com/Guided-Projects/HumanDevelopmentIndex/tree/main/Dataset
- Place it inside the `Dataset/` folder

### Step 3: Run the Jupyter Notebook
```bash
cd Training
jupyter notebook HumDevIndex.ipynb
```
- Run all cells in order (Epic 2 → Epic 7)
- This will generate `Flask/HDI.pkl`

### Step 4: Run the Flask Web App
```bash
cd Flask
python app.py
```
- Open browser: http://localhost:5000

---

## 🤖 Model Details

| Property | Value |
|----------|-------|
| Algorithm | Linear Regression |
| Dataset | UNDP HDI Data (195 rows × 82 columns) |
| Train/Test Split | 90% / 10% |
| Random State | 42 |
| Model File | HDI.pkl (Pickle) |

---

## 🎯 HDI Categories

| Score Range | Category |
|-------------|----------|
| 0.80 – 0.94 | 🟢 Very High HDI |
| 0.70 – 0.80 | 🔵 High HDI |
| 0.40 – 0.70 | 🟡 Medium HDI |
| 0.30 – 0.40 | 🔴 Low HDI |

---

## 👥 Team Members — ML-0027

| Name | Role |
|------|------|
| Rohit Venkata Manikanta Jannu | Team Lead |
| Gopi Krishna Valleti | Member |
| Jagan Surya Satish Reddy Medapati | Member |
| Chetan Kamjula | Member |
| Yaswanth Naidu Vinnakota | Member |

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn (Linear Regression)
- Flask (Web Framework)
- Pickle (Model Serialization)
- Jupyter Notebook

---

**Date:** 26 June 2026
