Heart Health Prediction Web Application

Project Overview
This project is a Heart Health Prediction Web Application developed using Machine Learning and Web Technologies.
The application predicts the risk of heart disease based on basic medical parameters entered by the user.

The main goal of this project is to provide an easy and user-friendly system for early heart disease risk assessment.
The system displays both the risk category and the risk probability percentage.

This project is intended for educational and academic purposes.

Objectives

To predict heart disease risk using machine learning

To provide a simple and user-friendly web interface

To display heart risk as Low Risk or High Risk

To show real risk percentage based on model probability

To integrate frontend and backend into a complete working system

Dataset Information
The project uses the UCI Heart Disease Dataset obtained from Kaggle / UCI Machine Learning Repository.

Dataset details:

Number of records: Approximately 300

Features include age, blood pressure, cholesterol, ECG results, heart rate, and other medical parameters

Target column indicates presence or absence of heart disease

Target values:

0 indicates no heart disease

1 indicates presence of heart disease

Machine Learning Model
The Random Forest Classifier is used for heart disease prediction.

Reason for choosing Random Forest:

Provides good accuracy for medical datasets

Handles non-linear relationships effectively

Robust and reliable model

Model evaluation is performed using accuracy and classification metrics.

System Architecture
The application follows a simple three-layer architecture:

User Interface
Frontend built using HTML, CSS, and JavaScript collects user input.

Backend API
Flask backend receives input data, processes it, and sends it to the ML model.

Machine Learning Model
The trained Random Forest model predicts heart disease risk and probability.

Technology Stack

Frontend Technologies
HTML
CSS
JavaScript

Backend Technologies
Python
Flask
Flask-CORS

Machine Learning Libraries
Scikit-learn
Pandas
NumPy
Joblib

Project Folder Structure

heart-health-prediction
ml
heart_disease_uci.csv
preprocess.py
train_model.py
model.pkl

backend
app.py
requirements.txt

frontend
index.html
style.css
script.js

README file

How to Run the Project

Step 1: Install required Python packages
Navigate to backend folder and run:
pip install -r requirements.txt

Step 2: Train the Machine Learning model
Navigate to ml folder and run:
python train_model.py

Step 3: Start the Flask backend server
Navigate to backend folder and run:
python app.py

The backend will run on:
http://127.0.0.1:5000

Step 4: Run the frontend
Open frontend/index.html in a web browser or use VS Code Live Server.

API Usage

Endpoint:
POST /predict

Sample input format (JSON):
age, sex, chest pain type, blood pressure, cholesterol, fasting blood sugar, ECG result, heart rate, exercise angina, oldpeak, slope, CA, thal

Sample output:
Prediction result (Low Risk or High Risk)
Risk probability percentage

Key Features

Dropdown-based user inputs

Input validation to prevent incorrect values

Real-time prediction

Displays risk category and probability

Clean and modern user interface

Fast response from backend

Disclaimer
This application is developed for academic and learning purposes only.
It does not replace professional medical diagnosis or treatment.

Future Enhancements

User login and health history tracking

Mobile application version

Cloud deployment

Advanced machine learning models

Doctor recommendation feature

Author
Shivani Kumbaji
B.Tech Computer Science and Engineering
Full-Stack Developer and Machine Learning Enthusiast

Conclusion
This project demonstrates the successful integration of machine learning with web development to build a real-world healthcare application focused on early heart disease risk prediction and user accessibility.
