💓 Heart Disease Prediction App

An interactive Machine Learning web application built using Streamlit that predicts the risk of heart disease based on patient medical parameters.

📌 Project Overview

Heart disease is one of the leading causes of death worldwide.
This project uses a K-Nearest Neighbors (KNN) machine learning model to predict whether a patient is at high or low risk of heart disease.

The application allows users to enter patient details and get instant predictions.

🚀 Features

📊 Interactive UI using Streamlit

🤖 Machine Learning model (KNN Classifier)

⚙️ Data preprocessing & feature scaling

🔍 Real-time prediction

📈 Scalable & deployment-ready structure

🧠 Uses trained model (.pkl files)

🛠️ Tech Stack

Python

Pandas

Scikit-learn

Joblib

Streamlit

📂 Project Structure
Heart_disease/
│
├── app.py
├── KNN_heart_model.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
📊 Input Features


The model takes the following medical inputs:

Age

Sex

Chest Pain Type

Resting Blood Pressure

Cholesterol Level

Fasting Blood Sugar

Resting ECG

Maximum Heart Rate

Exercise Induced Angina

Oldpeak (ST Depression)

Slope of ST Segment

![First Page](https://github.com/SanjivaniS10/Heart-Disease-Prediction-App/blob/main/Screenshot%202026-02-26%20142221.png))
![Second Page](https://github.com/SanjivaniS10/Heart-Disease-Prediction-App/blob/main/Screenshot%202026-02-26%20142124.png))

🧠 Machine Learning Workflow

Data Cleaning & Preprocessing

Feature Encoding

Feature Scaling using StandardScaler

Model Training using KNN Classifier

Model Evaluation

Model Saving using Joblib

Deployment using Streamlit

▶️ How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Requirements
pip install -r requirements.txt
4️⃣ Run the App
streamlit run app.py
📦 Requirements

Create a requirements.txt file with:

streamlit
pandas
scikit-learn
joblib
📈 Model Output

✅ Low Risk of Heart Disease

⚠️ High Risk of Heart Disease

⚡ Note: This prediction is based on a Machine Learning model and should not be considered a medical diagnosis.

🌍 Future Improvements

Add Probability Score Display

Improve UI Design

Deploy on Streamlit Cloud

Add Medical Report PDF Generation

Improve model with advanced algorithms

👩‍💻 Author

Sanjivani Santosh Suryawanshi
Machine Learning & Data Science Enthusiast
