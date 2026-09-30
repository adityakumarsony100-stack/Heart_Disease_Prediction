import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)


# =========================================================
# LOAD TRAINED MODEL AND PREPROCESSING OBJECTS
# =========================================================

@st.cache_resource
def load_model():

    model = joblib.load("SVM_HeartDisease.pkl")
    scaler = joblib.load("scaler_HeartDisease.pkl")
    expected_columns = joblib.load("columns_HeartDisease.pkl")

    return model, scaler, expected_columns


model, scaler, expected_columns = load_model()


# =========================================================
# TITLE
# =========================================================

st.title("❤️ Heart Disease Prediction by Aditya")

st.markdown(
    """
    ### Machine Learning-Based Heart Disease Prediction

    Enter the patient's clinical information below and use the
    trained Support Vector Machine (SVM) model to generate a prediction.
    """
)

st.divider()


# =========================================================
# PATIENT INFORMATION
# =========================================================

st.header("🧑‍⚕️ Patient Information")

col1, col2, col3 = st.columns(3)


# ---------------------------------------------------------
# COLUMN 1
# ---------------------------------------------------------

with col1:

    Age = st.slider(
        "Age",
        min_value=18,
        max_value=100,
        value=40
    )

    Sex = st.selectbox(
        "Sex",
        ["M", "F"]
    )

    ChestPainType = st.selectbox(
        "Chest Pain Type",
        ["ATA", "NAP", "ASY", "TA"]
    )

    RestingBP = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=80,
        max_value=200,
        value=120
    )


# ---------------------------------------------------------
# COLUMN 2
# ---------------------------------------------------------

with col2:

    Cholesterol = st.number_input(
        "Cholesterol Level (mg/dL)",
        min_value=100,
        max_value=600,
        value=200
    )

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dL",
        [0, 1]
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal", "ST", "LVH"]
    )


# ---------------------------------------------------------
# COLUMN 3
# ---------------------------------------------------------

with col3:

    max_hr = st.slider(
        "Maximum Heart Rate",
        min_value=60,
        max_value=220,
        value=150
    )

    exercise_angina = st.selectbox(
        "Exercise-Induced Angina",
        ["Y", "N"]
    )

    oldpeak = st.slider(
        "Oldpeak (ST Depression)",
        min_value=0.0,
        max_value=6.0,
        value=1.0,
        step=0.1
    )

    st_slope = st.selectbox(
        "ST Slope",
        ["Up", "Flat", "Down"]
    )


# =========================================================
# PREDICTION
# =========================================================

st.divider()

predict_button = st.button(
    "🔍 Predict Heart Disease",
    type="primary",
    use_container_width=True
)


if predict_button:

    # -----------------------------------------------------
    # CREATE RAW INPUT
    # -----------------------------------------------------

    raw_input = {

        "Age": Age,
        "RestingBP": RestingBP,
        "Cholesterol": Cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,

        "Sex_" + Sex: 1,

        "ChestPainType_" + ChestPainType: 1,

        "RestingECG_" + resting_ecg: 1,

        "ExerciseAngina_" + exercise_angina: 1,

        "ST_Slope_" + st_slope: 1
    }


    # -----------------------------------------------------
    # CREATE DATAFRAME
    # -----------------------------------------------------

    input_df = pd.DataFrame([raw_input])


    # -----------------------------------------------------
    # MATCH TRAINING FEATURES
    # -----------------------------------------------------

    # Add missing dummy columns
    for col in expected_columns:

        if col not in input_df.columns:

            input_df[col] = 0


    # Keep exactly the same column order
    input_df = input_df[expected_columns]


    # -----------------------------------------------------
    # SCALE INPUT
    # -----------------------------------------------------

    scaled_input = scaler.transform(input_df)


    # -----------------------------------------------------
    # MAKE PREDICTION
    # -----------------------------------------------------

    prediction = model.predict(scaled_input)[0]


    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    st.divider()

    st.header("Prediction Result")


    if prediction == 1:

        st.error(
            "⚠️ High Risk of Heart Disease"
        )

        st.warning(
            """
            The SVM model classified this patient as having
            heart disease.

            This prediction is generated by a machine-learning
            model and is not a medical diagnosis.
            """
        )


    else:

        st.success(
            "✅ Low Risk of Heart Disease"
        )

        st.info(
            """
            The SVM model classified this patient as not having
            heart disease.

            This prediction is generated by a machine-learning
            model and is not a medical diagnosis.
            """
        )


    # -----------------------------------------------------
    # PATIENT SUMMARY
    # -----------------------------------------------------

    st.subheader("📋 Patient Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Age",
            "Sex",
            "Chest Pain Type",
            "Resting BP",
            "Cholesterol",
            "Fasting Blood Sugar",
            "Resting ECG",
            "Maximum Heart Rate",
            "Exercise Angina",
            "Oldpeak",
            "ST Slope"
        ],

        "Value": [
            Age,
            Sex,
            ChestPainType,
            RestingBP,
            Cholesterol,
            fasting_bs,
            resting_ecg,
            max_hr,
            exercise_angina,
            oldpeak,
            st_slope
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# MODEL INFORMATION
# =========================================================

st.divider()

st.header("📊 Model Performance")

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "Accuracy",
    "89.13%"
)

metric2.metric(
    "Recall",
    "95.10%"
)

metric3.metric(
    "F1 Score",
    "90.65%"
)

metric4.metric(
    "ROC-AUC",
    "0.9285"
)


st.markdown(
    """
    **Model:** Support Vector Machine (SVM)

    **Dataset:** 918 patient records

    The project includes exploratory data analysis, correlation
    analysis, hypothesis testing, model comparison and deployment
    using Streamlit.
    """
)


# =========================================================
# DISCLAIMER
# =========================================================

st.divider()

st.caption(
    "⚠️ This application is intended for educational and "
    "demonstration purposes only and should not be used as "
    "a substitute for professional medical advice or diagnosis."
)
