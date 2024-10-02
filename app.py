from flask import Flask, render_template, url_for, request, redirect, jsonify, session
import requests
import os
from dotenv import load_dotenv
import weather_service

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

class City():
    def __init__(self, n):
        weather_forecast = weather_service.weather_forecast(n)
        self.name = weather_forecast["Name"]
        self.date = weather_forecast["Date"]
        self.weather = weather_forecast["Weather"]
        self.icon = weather_forecast["Icon"]
        self.temperature = weather_forecast["Temperature"]
        self.feels_like = weather_forecast["Feels Like"]
        self.humidity = weather_forecast["Humidity"]
        self.pressure = weather_forecast["Pressure"]
        self.cloudiness = weather_forecast["Cloudiness"]
        self.wind_speed = weather_forecast["Wind Speed"]
        self.visibility = weather_forecast["Visibility"]
        self.probability_of_precipitation = weather_forecast["Probability of Precipitation"]

    def __repr__(self):
        return '<City %r>' % self.name


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        city_name = request.form['city_name']
        try:
            city = City(city_name)
            session['city_name'] = city_name
            try:
                return render_template('index.html', city=city, i=0)
            except:
                return 'There was an issue searching for the city. Please try again.'
        except:
            return 'City not found!'
    else:
        session.pop('city_name', None)
        response = requests.get('https://ipinfo.io')
        data = response.json()
        city_name = data.get('city', 'Unknown')
        return render_template('index.html', city=City(city_name), i=0)

@app.route('/update_weather', methods=['POST'])
def update_weather():
    i = int(request.form.get('i', 0))
    city_name = session.get('city_name')
    if city_name == None:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        city_name = data.get('city', 'Unknown')
    city = City(city_name)

    return jsonify({
        'name': city.name,
        'date': city.date[i],
        'icon': city.icon[i],
        'temperature': city.temperature[i],
        'feels_like': city.feels_like[i],
        'probability_of_precipitation': city.probability_of_precipitation[i],
        'weather': city.weather[i],
        'humidity': city.humidity[i],
        'pressure': city.pressure[i],
        'cloudiness': city.cloudiness[i],
        'wind_speed': city.wind_speed[i],
        'visibility': city.visibility[i]
    })

if __name__ == "__main__":
    app.run(debug=True)