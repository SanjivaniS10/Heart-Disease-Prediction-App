import streamlit as st
import pandas as pd
import joblib
import os
print(os.getcwd())
# -------------------------------
# Load Model and Files
# -------------------------------
model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# -------------------------------
# App Title
# -------------------------------
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.title("💓 Heart Disease Prediction App")
st.markdown("### 👩‍⚕️ Developed by Sanjivani")
st.write("Enter patient details below to predict heart disease risk.")

st.divider()

# -------------------------------
# User Inputs
# -------------------------------

age = st.number_input("Age", min_value=18, max_value=100, value=40)
sex = st.selectbox("Sex", ["Male", "Female"])
chest_pain = st.selectbox("Chest Pain Type ", ["ATA","TA","ASY"])
resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol Level", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
max_hr = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", [0, 1, 2])

# Convert Sex
sex = 1 if sex == "Male" else 0

# -------------------------------
# Prediction Button
# -------------------------------

if st.button("🔍 Predict"):

    # Create DataFrame
    input_data = {
        'Age':age,
        'chest_pain':chest_pain,
        'resting_bp': resting_bp,
         'chol':chol,
        'Fasting_BS ':fbs,
         'Resting_ecg ':restecg,
         'Max_Heartrate':max_hr,
          'exang':exang,
        'oldpeak':oldpeak,
        'slope':slope
    }


    input_df = pd.DataFrame([input_data])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]
    # -------------------------------
    # Result Display
    # -------------------------------
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease Detected")

    else:
        st.success("✅ Low Risk of Heart Disease")
    st.info("⚡ Note: This prediction is based on Machine Learning model and not a medical diagnosis.")
