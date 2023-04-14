from flask import Flask, render_template,request,redirect,url_for
# from flask_ngrok import run_with_ngrok
from joblib import load
import pandas as pd

app = Flask(__name__,template_folder="Project_ML")

@app.route("/")
def index():
    return render_template("model.html")

@app.route("/model",methods=['GET', 'POST'])
def model_page():


  output_text = 'Initial'

  if request.method == 'POST':
      gender = request.form.get('gender')
      SeniorCitizen = request.form.get('SeniorCitizen')
      Partner = request.form.get('Partner')
      Dependents  = request.form.get('Dependents')
      PhoneService = request.form.get('PhoneService')
      MultipleLines = request.form.get('MultipleLines')
      InternetService = request.form.get('InternetService')
      OnlineSecurity = request.form.get('OnlineSecurity')
      OnlineBackup = request.form.get('OnlineBackup')
      DeviceProtection = request.form.get('DeviceProtection')
      TechSupport = request.form.get('TechSupport')
      StreamingTV = request.form.get('StreamingTV')
      StreamingMovies = request.form.get('StreamingMovies')
      Contract = request.form.get('Contract')
      PaperlessBilling = request.form.get('PaperlessBilling')
      PaymentMethod = request.form.get('PaymentMethod')
      MonthlyCharges = request.form.get('MonthlyCharges')
      TotalCharges = request.form.get('TotalCharges')
      tenure_group = request.form.get('tenure_group')

      df = pd.DataFrame({
          'gender':[gender],
          'SeniorCitizen':[SeniorCitizen],
          'Partner':[Partner],
          'Dependents':[Dependents],
          'PhoneService':[PhoneService],
          'MultipleLines':[MultipleLines],
          'InternetService':[InternetService],
          'OnlineSecurity':[OnlineSecurity],
          'OnlineBackup':[OnlineBackup],
          'DeviceProtection':[DeviceProtection],
          'TechSupport':[TechSupport],
          'StreamingTV':[StreamingTV],
          'StreamingMovies':[StreamingMovies],
          'Contract':[Contract],
          'PaperlessBilling':[PaperlessBilling],
          'PaymentMethod':[PaymentMethod],
          'MonthlyCharges':[MonthlyCharges],
          'TotalCharges':[TotalCharges],
          'tenure_group':[tenure_group]
      })


      randomForestClassifier = load('Project_ML/random_forest.joblib')
      y_pred = randomForestClassifier.predict(df)

      if y_pred == 0.0:
          pred = " User Will Not Churn "
      else:
          pred = " User Will Churn "

      return render_template('output.html', output_text=pred)
