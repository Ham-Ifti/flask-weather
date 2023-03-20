import weather
from datetime import datetime
from flask import Flask, request
import pandas as pd
from joblib import load
from sklearn.metrics import mean_absolute_error, mean_squared_error

model = load("./model-v2.joblib")

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

@app.route("/")
def dashboard():
    X = pd.read_csv("./Data/test.csv")
    Y = X.pop("Target")
    metrics = {}
    metrics["predictions"] = model.predict(X.values).tolist()

    r2_score = model.score(X.values, Y.values)
    mae = mean_absolute_error(Y.values, metrics["predictions"])
    mse = mean_squared_error(Y.values, metrics["predictions"])

    metrics["R^2 Score:"] = round(r2_score, 3)
    metrics["Mean Absolute Error:"] = round(mae, 3)
    metrics["Mean Squared Error:"] = round(mse, 3)
    metrics["Root Mean Squared Error:"] = round(mse ** 0.5, 3)
    return metrics

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        X = request.get_json()
        X = [[X["date"], X["temp"], X["temp_min"], X["temp_max"], X["percipitation"], X["wind_deg"], X["wind_speed"], X["pressure"]]]
        return {"prediction": round(model.predict(X)[0], 3)}
    
    w = weather.currentWeather(app.config["WEATHERAPI_KEY"])
    print(w)
    X = [[]]
    X[0].append(int(datetime.now().strftime("%Y%m%d")))
    X[0].append(w["main"]["temp"])
    X[0].append(w["main"]["temp_min"])
    X[0].append(w["main"]["temp_max"])
    X[0].append(0.6) #Percipitation
    X[0].append(w["wind"]["deg"])
    X[0].append(w["wind"]["speed"])
    X[0].append(w["main"]["pressure"])

    forecast = {}
    forecast["Tomorrow's Forecast:"] = round(model.predict(X)[0], 3)
    return forecast

