import requests

def currentWeather(API_key, city = "Islamabad", country = "PK"):
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}"
           f"&APPID={API_key}&units=metric")

    response = requests.get(url)
    try:
        data = response.json()
        return data
    except:
        return "Error calling Weather API"