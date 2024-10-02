import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENWEATHER_API_KEY')

def weather_forecast(city):
    payload = {"q": city, "appid": api_key, "units": "metric"}

    r = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=payload)
    
    info = {"Name": r.json()["city"]["name"],"Date": [],"Weather": [],"Icon": [],"Temperature": [],"Feels Like": [],"Humidity": [],"Pressure": [],"Cloudiness": [],"Wind Speed": [],"Visibility": [],"Probability of Precipitation": []}
    
    for i in range(len(r.json()["list"])):
        lst = r.json()["list"][i]
        main = lst["main"]
        weather = lst["weather"][0]
        info["Temperature"].append(int(main["temp"]))
        info["Feels Like"].append(int(main["feels_like"]))
        info["Pressure"].append(main["pressure"])
        info["Humidity"].append(main["humidity"])
        info["Weather"].append(weather["description"])
        info["Icon"].append(weather["icon"] + "@2x.png")
        info["Cloudiness"].append(lst["clouds"]["all"])
        info["Wind Speed"].append(lst["wind"]["speed"])
        info["Visibility"].append(int(lst["visibility"]) / 1000)
        info["Probability of Precipitation"].append(int(float(lst["pop"]) * 100))
        info["Date"].append(lst["dt_txt"])
    
    return info