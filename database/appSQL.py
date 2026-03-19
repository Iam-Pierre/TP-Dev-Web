from flask import Flask, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

import secrets
import hashlib
import random

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = "dev-secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY"] = db
Session(app)

class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    quota_used = db.Column(db.Integer, default=0)
    quota_max = db.Column(db.Integer, default=100)  # Exemple de quota maximum
