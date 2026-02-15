# 📊 Risk Score Classification System

## 📌 Project Overview

This Python program classifies input scores into different risk categories based on predefined ranges.
It also applies a simple personalization filter based on a registration digit.

The program:

* Accepts multiple scores from the user
* Classifies them into risk levels
* Ignores negative scores
* Applies personalization filtering
* Displays summary statistics

---

## ⚙️ How It Works

### 1️⃣ User Input

* User enters the number of scores (`m`)
* User enters `m` score values

---

### 2️⃣ Risk Classification

Scores are classified as:

| Score Range | Risk Category |
| ----------- | ------------- |
| `< 0`       | Ignored       |
| `0 – 30`    | Low Risk      |
| `31 – 60`   | Medium Risk   |
| `61 – 100`  | High Risk     |
| `> 100`     | Critical Risk |

---

### 3️⃣ Personalization Filtering

* A registration digit `d` is used.
* If `d` is **even** → All **Low Risk** scores are removed.
* If `d` is **odd** → All **Critical Risk** scores are removed.

(Default value in code: `d = 1` → removes Critical Risk scores)

---

## 📈 Output Display

The program displays:

* Low Risk Scores
* Medium Risk Scores
* High Risk Scores
* Critical Risk Scores
* Total Valid Entries
* Total Ignored Entries
* Total Removed Due to Personalization

---

## 🖥️ Example Run

```
enter size 5
enter scores :10
enter scores :45
enter scores :70
enter scores :-5
enter scores :120

registration digit : 1

low risk : [10]
medium risk : [45]
high risk : [70]
critical risk : [120]

after personalization filtering:
low risk : [10]
medium risk : [45]
high risk : [70]
critical risk : []

total valid entries : 4
total ignored entries : 1
total removed due to personalization : 1
```

---

## 🛠️ Technologies Used

* Python 3

---

## 🚀 How to Run

1. Install Python (if not installed)
2. Save the file as `risk_classifier.py`
3. Run the program:


## 📂 File Structure
risk-classification/
│
├── risk_classifier.py
└── README.md
## 🎯 Key Concepts Used

* Lists
* Conditional Statements
* Loops
* User Input Handling
* Basic Data Categorization
* Counting and Filtering Logic
