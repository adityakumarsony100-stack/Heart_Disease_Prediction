# ❤️ Heart Disease Prediction — Machine Learning & Streamlit

An end-to-end **machine learning classification project** built on **918 patient records** to analyze clinical factors associated with heart disease, compare multiple classification algorithms, evaluate model performance, and deploy the final **SVM model as an interactive Streamlit application**.

The project combines **exploratory data analysis, statistical hypothesis testing, machine learning, model evaluation, and deployment** in a single workflow.

## 🚀 Project Overview

**Workflow:**

`Data → EDA → Statistical Testing → Preprocessing → Model Comparison → SVM → Streamlit Deployment`

### Key Results

| Metric   |        SVM |
| -------- | ---------: |
| Accuracy | **89.13%** |
| Recall   | **95.10%** |
| F1 Score | **90.65%** |
| ROC-AUC  | **0.9285** |

The model achieved **95.10% recall** on the test set, meaning it correctly identified a high proportion of patients belonging to the heart-disease class in this dataset.

> **Note:** These results are specific to the dataset and evaluation procedure used in this project and should not be interpreted as clinical validation.

---

## 🎯 Project Objective

The objective was to investigate relationships between clinical characteristics and heart disease while developing a classification model that predicts the presence or absence of heart disease from patient-level features.

The project focuses on:

* Understanding the dataset through EDA
* Investigating selected clinical variables statistically
* Preparing numerical and categorical features
* Comparing multiple classification algorithms
* Evaluating models using multiple performance metrics
* Saving the trained model and preprocessing objects
* Deploying the final model through Streamlit

---

## 📊 Dataset

The dataset contains **918 patient records** and **12 variables**.

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
| `HeartDisease`   | Binary target variable                         |

`HeartDisease` is the target variable used for classification.

---

## 🔎 Exploratory Data Analysis

The exploratory analysis examined:

* Dataset structure and data types
* Missing values
* Descriptive statistics
* Target-class distribution
* Numerical feature distributions
* Correlations between numerical variables
* Differences in selected clinical variables between target groups

### Variables Selected for Statistical Analysis

The following variables were investigated further:

* **Age**
* **Resting Blood Pressure**
* **Cholesterol**

---

## 🧪 Statistical Hypothesis Testing

Independent-sample hypothesis tests were performed to examine whether the selected numerical variables differed between patients with and without heart disease.

### Results

| Variable    | No Heart Disease | Heart Disease |       p-value |
| ----------- | ---------------: | ------------: | ------------: |
| Age         |            50.55 |         55.90 | **< 0.00001** |
| RestingBP   |           130.18 |        134.19 |   **0.00087** |
| Cholesterol |           227.12 |        175.94 | **< 0.00001** |

Using a significance level of **α = 0.05**, all three variables showed statistically significant differences between the two groups in this dataset.

These findings indicate **statistical associations**, not causal relationships.

---

## 🤖 Machine Learning

Five classification algorithms were trained and compared:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Support Vector Machine (SVM)
4. Decision Tree
5. Gaussian Naive Bayes

### Preprocessing

The machine-learning workflow included:

1. Separating features and target
2. Encoding categorical variables
3. Scaling features using `StandardScaler`
4. Splitting the data into training and testing sets
5. Training multiple classification models
6. Evaluating model performance

The **SVM model** was selected for deployment based on the evaluation performed in the project.

---

## 📈 Model Evaluation

The final SVM model was evaluated using:

* Accuracy
* Recall
* F1 Score
* ROC-AUC

### SVM Performance

```text
Accuracy    : 89.13%
Recall      : 95.10%
F1 Score    : 90.65%
ROC-AUC     : 0.9285
```

Using multiple evaluation metrics provides a more complete assessment of classification performance than accuracy alone.

---

## 🚀 Streamlit Application

The trained SVM model is deployed as an interactive **Streamlit web application**.

Users can enter clinical information such as:

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

The application applies the same preprocessing used during model training and generates a predicted class.

### Application Features

* 🧑‍⚕️ Interactive patient input
* 🤖 Trained SVM model
* ⚙️ Consistent feature preprocessing
* ⚡ Real-time prediction
* 📊 Model performance information
* 📋 Patient input summary
* ⚠️ Medical-use disclaimer

---

## 🎥 Application Demo

**Live Demo:**
[Open the Streamlit Application](https://drive.google.com/file/d/1iIBP-E40N9dkunOdZXDidYx8wlDyCXJj/view?usp=sharing)


## 🛠️ Technologies

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Statistical Analysis

* SciPy

### Machine Learning

* Scikit-learn

### Deployment

* Streamlit

### Model Serialization

* Joblib

---


## 💡 What I Learned

This project provided practical experience in:

* Exploratory data analysis
* Statistical hypothesis testing
* Working with numerical and categorical variables
* Feature preprocessing and scaling
* Classification algorithms
* Model comparison
* Model evaluation
* Model serialization with Joblib
* Streamlit application development
* Building an end-to-end machine-learning workflow

A key focus of the project was taking the model **beyond the notebook and into a usable interactive application**.

---


## 👨‍💻 Author

### Aditya Kumar Sony

**BSc Mathematics | Data Science & Machine Learning**

Interested in:

`Data Analytics • Machine Learning • Mathematical Modeling • Applied Data Science`

---

## ⭐ Project Highlights

```text
918 Patient Records
        ↓
Exploratory Data Analysis
        ↓
Statistical Hypothesis Testing
        ↓
5 Classification Algorithms
        ↓
Support Vector Machine
        ↓
89.13% Accuracy
95.10% Recall
90.65% F1 Score
0.9285 ROC-AUC
        ↓
Streamlit Deployment
```

If you found this project useful, consider giving the repository a ⭐.
