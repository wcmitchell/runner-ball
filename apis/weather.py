from flask import Blueprint, jsonify
from pyowm import OWM
import json
import os
from lib.reporter import Reporter
from lib.weather import WeatherStats

#weather_api = Blueprint('weather_api', url_prefix='/weather')

# Setup
stats = WeatherStats()


#@weather_api.route('/')
def current_weather():
    current_weather = stats.update_stats()
    return stats

#@weather_api.route('/forecast')
def forecast():
    forecasts = stats.get_weather()
    weathers = []
    for weather in forecasts:
        weathers.append[WeatherStats(weather.weather)]
    #return jsonify(weathers)
