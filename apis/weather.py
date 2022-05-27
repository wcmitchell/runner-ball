from flask import Blueprint, Response
from lib.weather import WeatherStats
from jsonpickle import encode

weather_api = Blueprint('weather_api', __name__, url_prefix='/weather')

@weather_api.route('/')
def current_weather():
    current_weather = WeatherStats()
    return Response(encode(current_weather, unpicklable=False), mimetype='application/json')

@weather_api.route('/forecast')
def forecast():
    forecasts = stats.get_weather()
    weathers = []
    for weather in forecasts:
        weathers.append[WeatherStats(weather.weather)]
    #return jsonify(weathers)
