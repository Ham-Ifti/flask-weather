import requests

def currentWeather(city = "Islamabad", country = "PK"):
    API_key = "335307ae2fab5d5f3fa6e5cdf6d79f02"
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}"
           f"&APPID={API_key}&units=metric")

    response = requests.get(url)
    try:
        data = response.json()
        return data
    except:
        return "Error calling Weather API"