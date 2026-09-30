# ❤️ Heart Disease Prediction — Machine Learning & Streamlit

An end-to-end machine learning project that analyzes **918 patient records** to identify patterns associated with heart disease, statistically evaluate selected clinical variables, compare multiple classification algorithms, and deploy the final SVM model as an interactive **Streamlit web application**.

The project combines **exploratory data analysis, statistical hypothesis testing, machine learning, model evaluation, and deployment** into a single workflow.

---

## 🎯 Project Objective

The objective of this project is to investigate clinical characteristics associated with heart disease and develop a classification model capable of predicting whether a patient belongs to the heart-disease class based on recorded clinical features.

The project follows an end-to-end workflow:

**Data → EDA → Statistical Analysis → Feature Preparation → Model Training → Model Evaluation → Deployment**

---

## 📊 Dataset

The dataset contains **918 patient records** and 12 variables.

### Features

| Feature          | Description                                    |
| ---------------- | ---------------------------------------------- |
| `Age`            | Patient age                                    |
| `Sex`            | Patient sex                                    |
| `ChestPainType`  | Type of chest pain                             |
| `RestingBP`      | Resting blood pressure                         |
| `Cholesterol`    | Serum cholesterol level                        |
| `FastingBS`      | Whether fasting blood sugar is above 120 mg/dL |
| `RestingECG`     | Resting electrocardiogram result               |
| `MaxHR`          | Maximum heart rate achieved                    |
| `ExerciseAngina` | Exercise-induced angina                        |
| `Oldpeak`        | ST depression                                  |
| `ST_Slope`       | Slope of the peak exercise ST segment          |
| `HeartDisease`   | Target variable                                |

`HeartDisease` is the binary target variable used for classification.

---

## 🔎 Exploratory Data Analysis

The analysis begins with an examination of:

* Dataset structure and data types
* Missing values
* Descriptive statistics
* Target-class distribution
* Feature distributions
* Correlations between numerical variables
* Differences in selected clinical variables between target groups

### Key variables investigated

The project specifically examines:

* Age
* Resting Blood Pressure
* Cholesterol

These variables were selected for additional statistical analysis after the exploratory stage.

---

## 🧪 Statistical Hypothesis Testing

Independent-sample hypothesis tests were conducted to examine whether the selected numerical variables differed between patients with and without heart disease.

### Results

| Variable    | No Heart Disease | Heart Disease |   p-value |
| ----------- | ---------------: | ------------: | --------: |
| Age         |            50.55 |         55.90 | < 0.00001 |
| RestingBP   |           130.18 |        134.19 |   0.00087 |
| Cholesterol |           227.12 |        175.94 | < 0.00001 |

At a significance level of **α = 0.05**, all three variables showed statistically significant differences between the two groups in this dataset.

> These results describe statistical associations within this dataset and should not be interpreted as evidence of causal relationships.

---

## 🤖 Machine Learning

Five classification algorithms were evaluated:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Decision Tree
* Gaussian Naive Bayes

### Preprocessing

The machine-learning pipeline includes:

1. Separation of features and target
2. Encoding of categorical variables
3. Feature scaling using `StandardScaler`
4. Train/test split
5. Model training
6. Classification performance evaluation

The final deployed model is a **Support Vector Machine (SVM)**.

---

## 📈 Model Performance

The final SVM model was evaluated using multiple classification metrics.

| Metric   | SVM Performance |
| -------- | --------------: |
| Accuracy |      **89.13%** |
| Recall   |      **95.10%** |
| F1 Score |      **90.65%** |
| ROC-AUC  |      **0.9285** |

Using multiple metrics provides a more complete view of classification performance than accuracy alone.

---

## 🚀 Streamlit Deployment

The trained SVM model is deployed through an interactive Streamlit application.

The application allows users to enter patient information including:

* Age
* Sex
* Chest pain type
* Resting blood pressure
* Cholesterol
* Fasting blood sugar
* Resting ECG
* Maximum heart rate
* Exercise-induced angina
* Oldpeak
* ST slope

The application then processes the input using the saved preprocessing artifacts and returns the model's predicted class.

### Application features

* Interactive patient-input interface
* Saved SVM model
* Consistent feature preprocessing
* Real-time prediction
* Patient input summary
* Model-performance dashboard
* Prediction disclaimer

---

## 🗂️ Project Structure

```text
Heart_Disease_Prediction/
│
├── app.py
│
├── heart_disease_prediction.ipynb
│
├── SVM_HeartDisease.pkl
├── scaler_HeartDisease.pkl
├── columns_HeartDisease.pkl
│
├── requirements.txt
│
└── README.md
```

### File Description

| File                             | Purpose                                                        |
| -------------------------------- | -------------------------------------------------------------- |
| `app.py`                         | Streamlit deployment application                               |
| `heart_disease_prediction.ipynb` | EDA, statistical analysis, preprocessing and model development |
| `SVM_HeartDisease.pkl`           | Trained SVM model                                              |
| `scaler_HeartDisease.pkl`        | Feature-scaling object                                         |
| `columns_HeartDisease.pkl`       | Feature-column structure used during training                  |
| `requirements.txt`               | Python dependencies                                            |
| `README.md`                      | Project documentation                                          |

---

## 🛠️ Technologies Used

**Programming**

* Python

**Data Analysis**

* Pandas
* NumPy

**Visualization**

* Matplotlib
* Seaborn

**Statistical Analysis**

* SciPy

**Machine Learning**

* Scikit-learn

**Model Deployment**

* Streamlit

**Model Serialization**

* Joblib

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd Heart_Disease_Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📋 Requirements

Example `requirements.txt`:

```text
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
scipy
joblib
```

---

## 🔬 Project Workflow

```text
                ┌──────────────────┐
                │   Patient Data   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │       EDA        │
                │ Statistics &     │
                │ Correlation      │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    Hypothesis    │
                │     Testing      │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   Preprocessing  │
                │ Encoding + Scale │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Model Comparison │
                │ LR | KNN | SVM   │
                │ DT | NB          │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   Final SVM      │
                │ 89.13% Accuracy  │
                │ 95.10% Recall    │
                │ 0.9285 ROC-AUC   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    Streamlit     │
                │    Deployment    │
                └──────────────────┘
```

---

## 💡 Key Takeaways

This project demonstrates practical experience with:

* Exploratory data analysis
* Statistical hypothesis testing
* Numerical and categorical feature preprocessing
* Classification algorithms
* Model comparison
* Performance evaluation
* Model serialization
* Streamlit application development
* End-to-end machine learning workflow

Rather than treating model training as the final step, the project extends the workflow to **deployment through an interactive application**.

---

## ⚠️ Disclaimer

This application is intended for **educational and demonstration purposes only**.

The predictions generated by the machine-learning model should not be considered medical diagnoses or used as a substitute for evaluation by a qualified healthcare professional.

---

## 👨‍💻 Author

**Aditya Kumar Sony**

BSc Mathematics | Data Science & Machine Learning

Interested in **Data Analytics, Machine Learning, Mathematical Modeling, and Applied Data Science**.

---

## ⭐ Project Highlights

```text
918 Patient Records
        ↓
EDA + Correlation Analysis
        ↓
Hypothesis Testing
        ↓
5 Classification Models
        ↓
SVM
        ↓
89.13% Accuracy
95.10% Recall
90.65% F1 Score
0.9285 ROC-AUC
        ↓
Streamlit Deployment
```

If you found this project useful, consider giving the repository a ⭐.
