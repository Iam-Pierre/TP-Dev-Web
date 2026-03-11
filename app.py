from flask import Flask, render_template, request, send_file
from io import BytesIO
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

feature = pd.reak_pkl

app = Flask(__name__)





if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4000, debug=True)