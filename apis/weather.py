from dotenv import load_dotenv
from flask import Blueprint, jsonify
from pyowm import OWM
import json
import os
from lib.reporter import Reporter

#weather_api = Blueprint('weather_api', url_prefix='/weather')

# Setup
load_dotenv()
owm = OWM(os.getenv("OWM_APIKEY"))
mgr = owm.weather_manager()

class WeatherStats():
    def __init__(self, current_weather):
        self.uv_index = current_weather.uvi
        self.heat_index = current_weather.heat_index
        self.status = current_weather.detailed_status
        self.tempC = current_weather.temperature('celsius')
        self.tempF = current_weather.temperature('fahrenheit')
        self.humidity = current_weather.humidity
        self.cloudpct = current_weather.clouds
        self.snow = current_weather.snow
        self.rain = current_weather.rain

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    async def report(self):
        data = {
            "UV Index": self.uv_index,
            "Heat Index": self.heat_index,
            "Detailed Status": self.status,
            "Temp (C)": self.tempC['temp'],
            "Temp (F)": self.tempF['temp'],
            "Humidity": self.humidity,
            "Cloud Cover": self.cloudpct,
            "Snow": self.snow,
            "Rain": self.rain
        }
        Reporter(title="Weather Status", data=data).report()


#@weather_api.route('/')
def current_weather():
    current = mgr.weather_at_place(os.getenv("LOCATION"))
    stats = WeatherStats(current.weather)
    return stats

#@weather_api.route('/forecast')
def forecast():
    forecasts = mgr.forecast_at_place(os.getenv("LOCATION"))
    weathers = []
    for weather in forecasts:
        weathers.append[WeatherStats(weather.weather)]
    #return jsonify(weathers)
