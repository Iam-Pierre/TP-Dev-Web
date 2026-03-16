from flask import Flask, render_template, request, send_file,session
from io import BytesIO
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from werkzeug.security import generate_password_hash, check_password_hash

USERS = {}

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

@app.route("/api/login")
def exercice1():
    return render_template('login.html')


@app.route("/api/predict", methods=['POST'])
def predict():
    data = request.get_json()
    features = [float(data[features]) for features in feature_names]
    prediction = MODEL.predict_proba([features])[0][1]
    return {'prediction': prediction[0][1]}


# @app.route("/api/explain", methods=['GET'])
# def explain() :
#     features = [float(request.args get(features)) for features in FEATURES]
#     shap_values=EXPLAINER([features])


@app.route("/api/login",methods=['POST'])
def register():
    data = request.get_json()
    u = data.get("username","")
    p = data.get("password","")

    if u in USERS:
        return{"error": "Nom d'utilisateur déja pris"},400
    
    USERS[u] = generate_password_hash(p)
    session["user"] = u
    return {"ok": True}

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4000, debug=True)