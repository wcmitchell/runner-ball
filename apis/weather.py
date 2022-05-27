from flask import Blueprint, Response
from lib.weather import WeatherStats
from jsonpickle import encode

weather_api = Blueprint('weather_api', __name__, url_prefix='/api/weather')

@weather_api.route('/')
def current_weather():
    weather_json = encode(WeatherStats().weather.current, unpicklable=False)
    return Response(weather_json, mimetype='application/json')

@weather_api.route('/forecast/')
def forecast():
    weather_json = encode(WeatherStats().weather, unpicklable=False)
    return Response(weather_json, mimetype='application/json')

@weather_api.route('/forecast/<forecast_type>')
def forecast_for(forecast_type):
    allowed_forecast_types = ['minutely', 'hourly', 'daily']
    if forecast_type and forecast_type not in allowed_forecast_types:
        return Response({f"Allowed forecast types are: {allowed_forecast_types}"}, 400, mimetype='application/json')

    if forecast_type == 'minutely':
        stats = WeatherStats().weather.forecast_minutely
    elif forecast_type == 'hourly':
        stats = WeatherStats().weather.forecast_hourly
    elif forecast_type == 'daily':
        stats = WeatherStats().weather.forecast_daily

    weather_json = encode(stats, unpicklable=False)
    return Response(weather_json, mimetype='application/json')
