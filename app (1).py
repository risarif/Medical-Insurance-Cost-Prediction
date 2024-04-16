from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input from the form
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    bmi = float(request.form['bmi'])
    smoker = int(request.form['smoker'])
    region = int(request.form['region'])
    exercise_frequency = int(request.form['exercise_frequency'])
    chronic_conditions = int(request.form['chronic_conditions'])
    insurance_plan_type = int(request.form['insurance_plan_type'])
    distance_to_hospital = float(request.form['distance_to_hospital'])
    income_level = int(request.form['income_level'])
    family_medical_history = int(request.form['family_medical_history'])
    pcp_visits = int(request.form['pcp_visits'])
    mental_health_status = int(request.form['mental_health_status'])

    # Perform prediction
    input_features = np.array([[age, sex, bmi, smoker, region, exercise_frequency, chronic_conditions,
                                insurance_plan_type, distance_to_hospital, income_level, family_medical_history,
                                pcp_visits, mental_health_status]])
    prediction = model.predict(input_features)

    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
