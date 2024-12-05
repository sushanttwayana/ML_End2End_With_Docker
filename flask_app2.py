from flask import Flask, request
import pandas as pd
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)  # Corrected initialization

# Load the classifier
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route('/')
def home():
    return "Hello, My name is Sushant!!!"

@app.route('/predict', methods=["GET"])
def predict_note_authenticator():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
    """
    variance = request.args.get('variance', type=float)
    skewness = request.args.get('skewness', type=float)
    curtosis = request.args.get('curtosis', type=float)
    entropy = request.args.get('entropy', type=float)
    
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted value is " + str(prediction[0])

@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description: The output values
    """
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "The predicted values are " + str(list(prediction))

if __name__ == "__main__":
    app.run(debug=True)
