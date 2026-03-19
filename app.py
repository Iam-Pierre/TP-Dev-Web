from flask import Flask, render_template, request, send_file, session, redirect, url_for, request
from functools import wraps  # ← manquant pour le wrapper
import pickle
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates') 

USERS = {
    "pierreWang": generate_password_hash("wangpierre")
}

app.secret_key = 'dev-secret'

with open('models/feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)
with open('models/rf_model.pkl', 'rb') as f:
    MODEL = pickle.load(f)
with open('models/shap_explainer.pkl', 'rb') as f:
    EXPLAINER = pickle.load(f)

# Wrapper corrigé avec @wraps
def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper


@app.route("/", methods=['GET'])
def index():
    if "user" not in session:
        return render_template('login.html')
    else :
        return render_template('template.html', FEATURES=feature_names)


@app.route("/api/login", methods=['POST'])
def login():
    data = request.get_json()
    u = data.get("username", "")
    p = data.get("password", "")

    if u not in USERS or not check_password_hash(USERS[u], p):
        return {"error": "identifiants invalides"}, 401

    
    session["user"] = u
    return {"ok": True}

@app.route("/api/logout", methods=['POST'])
def handleLogout():
    session.pop("user", None)   
    return {"ok": True}

@app.route("/api/predict", methods=['POST'])
@auth_required  
def predict():
    data = request.get_json()
    features = [float(data[f]) for f in feature_names]
    prediction = MODEL.predict_proba([features])[0][1]
    return {'prediction': prediction}

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4000, debug=True)