from dotenv import load_dotenv
from flask import Blueprint, jsonify
from pyowm import OWM
import os

from lib import WeatherStats

#weather_api = Blueprint('weather_api', url_prefix='/weather')

# Setup
load_dotenv()
owm = OWM(os.getenv("OWM_APIKEY"))
mgr = owm.weather_manager()


#@weather_api.route('/')
def current_weather():
    current = mgr.weather_at_place(os.getenv("LOCATION"))
    stats = WeatherStats(current.weather)
    return stats.report()

#@weather_api.route('/forecast')
def forecast():
    forecasts = mgr.forecast_at_place(os.getenv("LOCATION"))
    weathers = []
    for weather in forecasts:
        weathers.append[WeatherStats(weather.weather)]
    #return jsonify(weathers)
