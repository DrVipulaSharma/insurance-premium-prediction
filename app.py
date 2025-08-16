from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("insurance_premium_model.pkl")

# List of required input features
required_features = [
    'Age', 'Weight', 'BMI', 'AnyChronicDiseases', 
    'NumberOfMajorSurgeries', 'SeverelyObese', 
    'BMI_RiskScore', 'HighSurgeryRisk', 'AgeGroup'
]

@app.route('/')
def home():
    return "Insurance Premium Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Check for missing features
    missing_features = [f for f in required_features if f not in data]
    if missing_features:
        return jsonify({"error": f"Missing features: {missing_features}"}), 400
    
    # Convert input to DataFrame and predict
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    
    return jsonify({"predicted_premium": prediction})

if __name__ == "__main__":
    app.run(debug=True)
