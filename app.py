# import required libraries 
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np 
import pandas as pd

# app 
app = Flask(__name__)

# load the model from the pickle file 
model = pickle.load(open("RegressionModel.pkl" , "rb"))

# load the scaler from the pickle file 
scaler = pickle.load(open("scaler.pkl", "rb"))

# Home page 
@app.route("/")
def home_page():
    return render_template("home.html")


# predict_api page 
@app.route("/predict_api", methods = ['POST'])
def predict_api():
    # load the data
    data = request.json['data']
    
    print(data)
    print(np.array(list(data.values())).reshape((1,-1)))

    data_scaled = scaler.transform(np.array(list(data.values())).reshape((1,-1)))

    # prediction
    pred = model.predict(data_scaled)
    # Convert the prediction result to a Python float
   
    prediction = float(pred[0])
    return jsonify(prediction)


if __name__ == "__main__":
    # running the app 
    app.run(debug= True)