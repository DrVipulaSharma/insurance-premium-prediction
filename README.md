# Insurance Premium Prediction

## Project Overview
This project predicts insurance premiums based on customer data using machine learning. It includes:

- **Exploratory Data Analysis (EDA)**  
- **Hypothesis Testing**  
- **Machine Learning Modeling**  
- **Deployment** via **Flask API** and **Streamlit App**  

The model helps estimate premiums for individuals given their demographic and health data.

---

## File Structure

insurance-premium-prediction/
├── insurance_analysis.ipynb # EDA + ML notebook
├── insurance_premium_model.pkl # Trained model
├── streamlit_app.py # Streamlit frontend
├── app.py # Flask API backend
├── requirements.txt # Dependencies
├── README.md

---

## Features Used for Prediction
The model requires the following features in JSON format:

- `Age`  
- `Weight`  
- `BMI`  
- `AnyChronicDiseases` (0 or 1)  
- `NumberOfMajorSurgeries`  
- `SeverelyObese` (0 or 1)  
- `BMI_RiskScore`  
- `HighSurgeryRisk` (0 or 1)  
- `AgeGroup` (e.g., 'Young', 'Middle', 'Senior')  

Target variable: `PremiumPrice`

---

## How to Run the Flask API

### 1️⃣ Clone the repository
```bash
git clone https://github.com/DrVipulaSharma/insurance-premium-prediction.git
cd insurance-premium-prediction

 2️⃣ Create a virtual environment 
python -m venv flask_new
flask_new\Scripts\activate    # Windows
# OR
source flask_new/bin/activate # macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Flask app
python app.py

5️⃣ Example API Request

Using curl:
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d "{
    \"Age\":40,
    \"Weight\":75,
    \"BMI\":24.5,
    \"AnyChronicDiseases\":0,
    \"NumberOfMajorSurgeries\":1,
    \"SeverelyObese\":0,
    \"BMI_RiskScore\":1.2,
    \"HighSurgeryRisk\":0,
    \"AgeGroup\":\"Middle\"
}"
Response:
{
  "predicted_premium": 26625.0
}
Streamlit App

Run the Streamlit frontend with:
streamlit run streamlit_app.py
This launches a web interface where users can input their details and get premium predictions.
## Model & Performance

| Model               | RMSE     | MAE      | R²      |
|--------------------|----------|----------|---------|
| RandomForest        | 3871.43  | 2035.93  | 0.6085  |
| GradientBoosting    | 3967.68  | 2293.31  | 0.5895  |
| LinearRegression    | 4021.89  | 2719.17  | 0.5817  |
| NeuralNetwork       | 4376.62  | 3051.32  | 0.5054  |
| DecisionTree        | 5256.96  | 2162.87  | 0.2794  |

**Best Model:** `RandomForestRegressor(n_estimators=200, random_state=42)`

## Requirements

All dependencies are listed in requirements.txt. It includes Flask, Streamlit, pandas, scikit-learn, and other necessary packages.


## Notes & Usage

- **File Placement**: Make sure `insurance_premium_model.pkl` and `app.py` are in the same directory before running the Flask API.

- **Flask API**:
  - The API provides endpoints to get insurance premium predictions.
  - Required features must be included in the JSON input. The API returns an error if any required columns are missing.
  - Example cURL request:
    ```bash
    curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"Age":40,"Weight":75,"BMI":24.5,"AnyChronicDiseases":0,"NumberOfMajorSurgeries":1,"SeverelyObese":0,"BMI_RiskScore":1.2,"HighSurgeryRisk":0,"AgeGroup":"Middle"}'
    ```
  - Example response:
    ```json
    {"predicted_premium": 26625.0}
    ```

- **Streamlit App**:
  - Provides a user-friendly interface for inputting values and getting predictions.
  - Simply run `streamlit run streamlit_app.py` in your terminal while in the project folder.

- **Dependencies**:
  - Install all dependencies via `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

Author

Dr. Vipula Sharma

