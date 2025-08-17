# Insurance Premium Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-API-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

---

## Quick Demo

🔹 **Streamlit App (User Interface)**  
Easily input customer details and get real-time premium predictions.

🔗 **Try the Live Streamlit App:**  
[https://insurance-premium-prediction-ehrjlq6mmmxdvhunwl3acr.streamlit.app/](https://insurance-premium-prediction-ehrjlq6mmmxdvhunwl3acr.streamlit.app/)

![Streamlit Demo Screenshot](Streamlit%20screenshot.png)  
*Example Streamlit output showing premium prediction.*

---

🔹 **Flask API (JSON Request/Response)**  
Send customer details and get predictions via REST API.

**Request:**

<details>
<summary>Example JSON Request Body</summary>

{
"Age": 40,
"Weight": 75,
"BMI": 24.5,
"AnyChronicDiseases": 0,
"NumberOfMajorSurgeries": 1,
"SeverelyObese": 0,
"BMI_RiskScore": 1.2,
"HighSurgeryRisk": 0,
"AgeGroup": "Middle"
}

</details>

<details>
<summary>Example curl Command</summary>

curl -X POST http://127.0.0.1:5000/predict
-H "Content-Type: application/json"
-d '{
"Age": 40,
"Weight": 75,
"BMI": 24.5,
"AnyChronicDiseases": 0,
"NumberOfMajorSurgeries": 1,
"SeverelyObese": 0,
"BMI_RiskScore": 1.2,
"HighSurgeryRisk": 0,
"AgeGroup": "Middle"
}'
</details>

---

## Project Overview

This project predicts **insurance premiums** based on customer data using machine learning.

It includes:
- Exploratory Data Analysis (EDA)
- Hypothesis Testing
- Machine Learning Modeling
- Deployment via Flask API and Streamlit App

The model helps estimate premiums for individuals based on their demographic and health data.

---

## File Structure

insurance-premium-prediction/
├── insurance_analysis.ipynb # EDA + ML notebook
├── insurance_premium_model.pkl # Trained model
├── streamlit_app.py # Streamlit frontend
├── app.py # Flask API backend
├── input_columns.pkl # Model input columns
├── requirements.txt # Dependencies
├── README.md
├── Streamlit screenshot.png


---

## Features Used for Prediction

The model requires the following features in **JSON format**:
- Age
- Weight
- BMI
- AnyChronicDiseases (0 or 1)
- NumberOfMajorSurgeries
- SeverelyObese (0 or 1)
- BMI_RiskScore
- HighSurgeryRisk (0 or 1)
- AgeGroup (e.g., 'Young', 'Middle', 'Senior')

**Target variable:** `PremiumPrice`

---

## How to Run the Flask API

1. **Clone the repository:**
git clone https://github.com/DrVipulaSharma/insurance-premium-prediction.git
cd insurance-premium-prediction

2. **Create a virtual environment:**
python -m venv flask_new

3. **Activate the environment:**
- On Windows:
  ```
  flask_new\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source flask_new/bin/activate
  ```

4. **Install dependencies:**
pip install -r requirements.txt

5. **Run the Flask app:**
python app.py

6. **Example API Request:**
curl -X POST http://127.0.0.1:5000/predict
-H "Content-Type: application/json"
-d '{"Age":40,"Weight":75,"BMI":24.5,"AnyChronicDiseases":0,"NumberOfMajorSurgeries":1,"SeverelyObese":0,"BMI_RiskScore":1.2,"HighSurgeryRisk":0,"AgeGroup":"Middle"}'

**Example Response:**
{"predicted_premium": 26625.0}

---

## Streamlit App

Launch the frontend with:

streamlit run streamlit_app.py

This opens a web UI for interactive insurance premium predictions.

---

## Model & Performance

| Model              | RMSE     | MAE      | R²      |
|--------------------|----------|----------|---------|
| RandomForest       | 3871.43  | 2035.93  | 0.6085  |
| GradientBoosting   | 3967.68  | 2293.31  | 0.5895  |
| LinearRegression   | 4021.89  | 2719.17  | 0.5817  |
| NeuralNetwork      | 4376.62  | 3051.32  | 0.5054  |
| DecisionTree       | 5256.96  | 2162.87  | 0.2794  |

**Best Model:**  
`RandomForestRegressor(n_estimators=200, random_state=42)`

---

## Requirements

Install all dependencies with:

pip install -r requirements.txt

Core dependencies:
- Flask
- Streamlit
- pandas
- scikit-learn
- joblib
- numpy
- (and other necessary packages)

---

## Notes & Usage

- **File Placement:** Ensure `insurance_premium_model.pkl` and `app.py` are in the same directory before running the Flask API.
- **Flask API:**  
  - Exposes endpoints for insurance premium predictions.
  - All required fields must be included in JSON input.
  - Missing fields will return an error.
- **Streamlit App:**  
  - Run via: `streamlit run streamlit_app.py`  
  - Provides a user-friendly interface for users.

---

## Author

**Dr. Vipula Sharma**






























