import streamlit as st
import joblib
import numpy as np

# Load scaler and model
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

# Page config
st.set_page_config(page_title="Customer Churn Prediction", page_icon="", layout="centered")

# Apply custom style
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 24px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stSelectbox, .stNumberInput {
            font-size: 16px;
        }
        .result {
            font-size: 24px;
            font-weight: bold;
            color: #ff4b4b;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("Customer Churn Prediction System")
st.subheader("Predict whether a customer is likely to churn")

st.info("Please fill out the customer details below and click **Predict** to see the result.")

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=10, max_value=100, value=30)
        gender = st.selectbox("Gender", ["Male", "Female"])

    with col2:
        tenure = st.number_input("Tenure (months)", min_value=0, max_value=130, value=10)
        monthlycharge = st.number_input("Monthly Charge ($)", min_value=30, max_value=150)

    submitted = st.form_submit_button("Predict")

# Prediction logic
if submitted:
    gender_encoded = 1 if gender == "Female" else 0
    x = [age, gender_encoded, tenure, monthlycharge]
    x_scaled = scaler.transform([x])
    prediction = model.predict(x_scaled)[0]
    result = "Yes, the customer is likely to churn." if prediction == 1 else "No, the customer is not likely to churn."

    st.markdown("---")
    st.success("Prediction Result")
    st.markdown(f"<p class='result'>{result}</p>", unsafe_allow_html=True)
    st.balloons()
