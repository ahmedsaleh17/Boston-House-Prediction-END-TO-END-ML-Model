import requests
import json

# Define the URL of the API endpoint
url = 'http://127.0.0.1:5000/predict_api'

# Define the data to be sent to the API
data = {
    "CRIM": 0.00632,
    "ZN": 18.0,
    "INDUS": 2.31,
    "CHAS": 0,
    "NOX": 0.538,
    "RM": 6.575,
    "AGE": 65.2,
    "DIS": 4.0900,
    "RAD": 1,
    "TAX": 296.0,
    "PTRATIO": 15.3,
    "B": 396.90,
    "LSTAT": 4.98
}

# Convert data to JSON format
headers = {'Content-Type': 'application/json'}
data_json = json.dumps({"data": data})

# Make the POST request to the API
response = requests.post(url, headers=headers, data=data_json)

# Check the response
if response.status_code == 200:
    prediction = response.json()
    print(f"Prediction: {prediction}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)


