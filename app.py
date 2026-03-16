from flask import Flask, render_template, request, send_file
from io import BytesIO
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

app = Flask(__name__)



with open('explainer/feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)

with open('explainer/rf_model.pkl', 'rb') as f:
    MODEL = pickle.load(f)

with open('explainer/shap_explainer.pkl', 'rb') as f:
    EXPLAINER = pickle.load(f)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('template.html', FEATURES=feature_names)


@app.route("/api/predict", methods=['POST'])
def predict():
    data = request.get_json()
    features = [float(data[features]) for features in FEATURES]
    prediction = MODEL.predict_proba([features])[0][1]
    return {'prediction': prediction[0][1]}


# @app.route("/api/explain", methods=['GET'])
# def explain() :
#     features = [float(request.args get(features)) for features in FEATURES]
#     shap_values=EXPLAINER([features])




if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4000, debug=True)