import streamlit as st
import pandas as pd
import joblib

# -------------------
# Load Model & Columns
# -------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("insurance_premium_model.pkl")
    input_cols = joblib.load("input_columns.pkl")
    return model, input_cols

model, input_columns = load_artifacts()

# -------------------
# Streamlit App Title
# -------------------
st.title("💰 Insurance Premium Estimator")
st.write("Enter customer details below to estimate the insurance premium.")

# -------------------
# User Input Form
# -------------------
with st.form("premium_form"):

    # Numerical inputs
    Age = st.number_input("Age", min_value=18, max_value=100, value=30)
    Weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    Height = st.number_input("Height (cm)", min_value=120, max_value=220, value=170)
    BMI = Weight / ((Height / 100) ** 2)

    # Health and medical history
    AnyChronicDiseases = st.selectbox("Any Chronic Diseases?", ["No", "Yes"])
    NumberOfMajorSurgeries = st.number_input("Number of Major Surgeries", min_value=0, max_value=10, value=0)

    # Derived fields
    bmi_category = (
        "Underweight" if BMI < 18.5 else
        "Normal" if BMI < 25 else
        "Overweight" if BMI < 30 else
        "Obese" if BMI < 35 else
        "Severely Obese"
    )

    AgeGroup = (
        "18-25" if 18 <= Age <= 25 else
        "26-35" if 26 <= Age <= 35 else
        "36-45" if 36 <= Age <= 45 else
        "46-55" if 46 <= Age <= 55 else
        "56-66"
    )

    bmi_risk_map = {
        'Underweight': 1, 'Normal': 2, 'Overweight': 3, 'Obese': 4, 'Severely Obese': 5
    }
    BMI_RiskScore = bmi_risk_map[bmi_category]
    HighSurgeryRisk = 1 if NumberOfMajorSurgeries >= 2 else 0

    # Submit button
    submitted = st.form_submit_button("Estimate Premium")

# -------------------
# Prediction
# -------------------
if submitted:
    # Create input DataFrame with all features in correct order
    user_data = pd.DataFrame([[Age, Weight, Height, BMI, bmi_category,
                               AnyChronicDiseases, NumberOfMajorSurgeries,
                               AgeGroup, BMI_RiskScore, HighSurgeryRisk]],
                             columns=input_columns)

    # Predict
    prediction = model.predict(user_data)[0]

    st.subheader("Estimated Insurance Premium")
    st.success(f"₹ {prediction:,.2f}")

    # Show internal data for debugging
    with st.expander("Show Processed Input Data"):
        st.write(user_data)
