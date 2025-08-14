import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load model & input columns
# -----------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("insurance_premium_model.pkl")
    input_columns = joblib.load("input_columns.pkl")
    return model, input_columns

model, input_columns = load_artifacts()

st.title("💰 Insurance Premium Estimator")
st.write("Enter customer details to estimate their insurance premium.")

# -----------------------------
# Create input widgets dynamically
# -----------------------------
user_data = {}

for col in input_columns:
    if col.lower() in ["age"]:
        user_data[col] = st.number_input(f"{col}", min_value=0, max_value=120, value=30)
    elif col.lower() in ["bmi"]:
        user_data[col] = st.number_input(f"{col}", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    elif col.lower().startswith("number") or col.lower().endswith("count"):
        user_data[col] = st.number_input(f"{col}", min_value=0, max_value=20, value=0)
    elif col.lower().startswith("has") or col.lower().startswith("is_"):
        user_data[col] = st.selectbox(f"{col}", ["No", "Yes"])
        user_data[col] = 1 if user_data[col] == "Yes" else 0
    elif col.lower() in ["gender"]:
        user_data[col] = st.selectbox(f"{col}", ["Male", "Female"])
    elif col.lower() in ["region"]:
        user_data[col] = st.selectbox(f"{col}", ["northwest", "northeast", "southwest", "southeast"])
    else:
        # Default to text or number input
        user_data[col] = st.text_input(f"{col}", "")

# -----------------------------
# Convert to DataFrame
# -----------------------------
input_df = pd.DataFrame([user_data])

# Ensure column order matches training
input_df = input_df[input_columns]

# -----------------------------
# Predict
# -----------------------------
if st.button("Estimate Premium"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Premium: **${prediction:,.2f}**")

