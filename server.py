import weather
from datetime import datetime
from flask import Flask, request, send_from_directory
import pandas as pd
from joblib import load
from sklearn.metrics import mean_absolute_error, mean_squared_error
import os

model = load("./model-v2.joblib")

app = Flask(__name__, static_folder='static')
app.config.from_object("config.DevelopmentConfig")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/dashboard")
def dashboard():
    X = pd.read_csv("./Data/test.csv")
    Y = X.pop("Target")
    metrics = {}
    metrics["predictions"] = model.predict(X.values).tolist()

    r2_score = model.score(X.values, Y.values)
    mae = mean_absolute_error(Y.values, metrics["predictions"])
    mse = mean_squared_error(Y.values, metrics["predictions"])

    metrics["rsq"] = round(r2_score, 3)
    metrics["mae"] = round(mae, 3)
    metrics["mse"] = round(mse, 3)
    metrics["rmse"] = round(mse ** 0.5, 3)
    return metrics

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        X = request.get_json()
        X = [[int(datetime.now().strftime("%Y%m%d")), float(X["temp"]), float(X["temp_min"]), float(X["temp_max"]), float(X["percipitation"]), float(X["wind_deg"]), float(X["wind_speed"]), int(X["pressure"])]]
        print(X)
        pred = model.predict(X)[0]
        print(pred)
        return {"prediction": round(model.predict(X)[0], 3)}
    
    w = weather.currentWeather(app.config["WEATHERAPI_KEY"])
    X = [[]]
    X[0].append(int(datetime.now().strftime("%Y%m%d")))
    X[0].append(w["main"]["temp"])
    X[0].append(w["main"]["temp_min"])
    X[0].append(w["main"]["temp_max"])
    X[0].append(0.6) #Percipitation
    X[0].append(w["wind"]["deg"])
    X[0].append(w["wind"]["speed"])
    X[0].append(w["main"]["pressure"])
    # [['20220321', '20', '15', '25', '0.4', '120', '10', '1015']]
    # [[20230320, 24.91, 24.91, 24.91, 0.6, 208, 2.13, 1005]]
    print("X:", X)

    forecast = {}
    forecast["data"] = round(model.predict(X)[0], 3)
    return forecast
