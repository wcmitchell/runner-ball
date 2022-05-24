from dotenv import load_dotenv
from flask import Blueprint, jsonify
from pyowm import OWM
import json

import os

#weather_api = Blueprint('weather_api', url_prefix='/weather')

# Setup
load_dotenv()
owm = OWM(os.getenv("OWM_APIKEY"))
mgr = owm.weather_manager()

class WeatherStats():
    def __init__(self, currentWeather):
        self.uv_index = currentWeather.uvi
        self.heat_index = currentWeather.heat_index
        self.status = currentWeather.detailed_status
        self.tempC = currentWeather.temperature('celsius')
        self.tempF = currentWeather.temperature('fahrenheit')
        self.humidity = currentWeather.humidity
        self.cloudpct = currentWeather.clouds
        self.snow = currentWeather.snow
        self.rain = currentWeather.rain

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

#@weather_api.route('/')
def currentWeather():
    current = mgr.weather_at_place(os.getenv("LOCATION"))
    stats = WeatherStats(current.weather)
    #return jsonify(stats)
    print(stats.toJSON())

#@weather_api.route('/forecast')
def forecast():
    forecasts = mgr.forecast_at_place(os.getenv("LOCATION"))
    weathers = []
    for weather in forecasts:
        weathers.append[WeatherStats(weather.weather)]
    #return jsonify(weathers)

currentWeather()
