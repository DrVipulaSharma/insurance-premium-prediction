import streamlit as st
import pandas as pd
import joblib

# Load model and columns
@st.cache_resource
def load_artifacts():
    model = joblib.load("insurance_premium_model.pkl")
    input_columns = joblib.load("input_columns.pkl")
    return model, input_columns

model, input_columns = load_artifacts()

st.title("💰 Insurance Premium Estimator")
st.write("Fill in the details below to estimate your insurance premium.")

# Create input form
with st.form("premium_form"):
    Age = st.number_input("Age", min_value=18, max_value=100, value=30)
    Weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    Height = st.number_input("Height (cm)", min_value=120, max_value=220, value=170)
    AnyChronicDiseases = st.selectbox("Any Chronic Diseases?", options=[0, 1])
    NumberOfMajorSurgeries = st.number_input("Number of Major Surgeries", min_value=0, max_value=10, value=0)

    submitted = st.form_submit_button("Estimate Premium")

if submitted:
    # Derived features
    BMI = round(Weight / ((Height / 100) ** 2), 1)
    SeverelyObese = 1 if BMI >= 35 else 0

    if BMI < 18.5:
        BMI_RiskScore = 1
    elif 18.5 <= BMI < 25:
        BMI_RiskScore = 2
    elif 25 <= BMI < 30:
        BMI_RiskScore = 5
    elif 30 <= BMI < 35:
        BMI_RiskScore = 7
    else:
        BMI_RiskScore = 10

    HighSurgeryRisk = 1 if NumberOfMajorSurgeries >= 3 else 0

    if Age < 40:
        AgeGroup = "Young"
    elif 40 <= Age < 60:
        AgeGroup = "Middle-aged"
    else:
        AgeGroup = "Senior"

    # Create dict with all features in input_columns
    feature_dict = {col: 0 for col in input_columns}
    feature_dict.update({
        "Age": Age,
        "Weight": Weight,
        "BMI": BMI,
        "AnyChronicDiseases": AnyChronicDiseases,
        "NumberOfMajorSurgeries": NumberOfMajorSurgeries,
        "SeverelyObese": SeverelyObese,
        "BMI_RiskScore": BMI_RiskScore,
        "HighSurgeryRisk": HighSurgeryRisk,
        "AgeGroup": AgeGroup
    })

    # Create dataframe for prediction
    input_data = pd.DataFrame([feature_dict])

    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Premium: ${prediction:,.2f}")

    # Show derived metrics
    st.write(f"**Calculated BMI:** {BMI}")
    st.write(f"**BMI Risk Score:** {BMI_RiskScore}")
    st.write(f"**Severely Obese:** {'Yes' if SeverelyObese else 'No'}")
    st.write(f"**High Surgery Risk:** {'Yes' if HighSurgeryRisk else 'No'}")
    st.write(f"**Age Group:** {AgeGroup}")
