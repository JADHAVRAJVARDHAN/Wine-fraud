import json
import pickle

from flask import Flask, request, app, jsonify, url_for, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

try:
    with open('Xgboost_Classification_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: File not found.")

with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
        print("Scaler loaded successfully!")
        
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    
 try:
    # Get JSON data from the request
     df = request.json['data']
     print("Received data: ", df)
    
     new_data = pd.DataFrame(df, index=[0])

        # Feature scaling (using the same scaler used during training)
     num_cols = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 
                    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 
                    'pH', 'sulphates', 'alcohol']
     new_data[num_cols] = scaler.transform(new_data[num_cols])

        # Make predictions
     prediction = loaded_model.predict(new_data)
     return jsonify({'prediction': int(prediction[0])})
 except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
