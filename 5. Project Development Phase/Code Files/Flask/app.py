# importing the necessary dependencies
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('HDI.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Prediction', methods=['POST', 'GET'])
def prediction():
    return render_template('indexnew.html')

@app.route('/Home', methods=['POST', 'GET'])
def my_home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Reading inputs from form
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    # Must match training features exactly
    features_name = [
        'Life expectancy',
        'Expected years of schooling',
        'Mean years of schooling',
        'Gross national income (GNI) per capita'
    ]

    df = pd.DataFrame(features_value, columns=features_name)

    output = model.predict(df)
    y_pred = round(float(output[0]), 2)

    print('Predicted HDI:', y_pred)

    if y_pred >= 0.3 and y_pred < 0.4:
        result = 'Low HDI ' + str(y_pred)
    elif y_pred >= 0.4 and y_pred < 0.7:
        result = 'Medium HDI ' + str(y_pred)
    elif y_pred >= 0.7 and y_pred < 0.8:
        result = 'High HDI ' + str(y_pred)
    elif y_pred >= 0.8 and y_pred <= 0.94:
        result = 'Very High HDI ' + str(y_pred)
    else:
        result = 'Out of range - check your input values'

    return render_template('resultnew.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)