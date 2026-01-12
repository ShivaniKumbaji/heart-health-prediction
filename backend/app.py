from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load trained model
MODEL_PATH = os.path.join("..", "ml", "model.pkl")
model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return "Heart Health Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([[
        data["age"],
        data["sex"],
        data["cp"],
        data["trestbps"],
        data["chol"],
        data["fbs"],
        data["restecg"],
        data["thalach"],
        data["exang"],
        data["oldpeak"],
        data["slope"],
        data["ca"],
        data["thal"]
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]  # risk probability

    risk_percent = round(probability * 100, 2)

    result = "High Risk" if prediction == 1 else "Low Risk"

    return jsonify({
        "prediction": result,
        "risk_percentage": risk_percent
    })

if __name__ == "__main__":
    app.run(debug=True)
