
# 💳 Fraud Detection System

## 📌 Project Overview
This project is an end-to-end Machine Learning application that detects whether a transaction is fraudulent or not. It includes model training, API deployment, and a user interface for real-time predictions.

---

## 🚀 Features
- Machine Learning model using Random Forest
- Real-time fraud prediction
- Flask-based REST API
- Simple web interface (HTML)
- Model saving using joblib

---

## 🧠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Flask
- HTML

---

## ⚙️ How It Works
1. Input transaction details (amount, time)
2. Model processes input
3. Predicts fraud or normal
4. Displays result on UI

---

## 🛠️ Installation & Run

### 1. Clone the repository

````

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

### 5. Open browser

```
http://127.0.0.1:5000/
```

---

## 📊 Model Details

* Algorithm: Random Forest Classifier
* Features: Amount, Time
* Output: Fraud (1) / Not Fraud (0)

---

## 💼 Use Case

* Banking fraud detection
* Transaction monitoring systems
* Fintech applications

---
