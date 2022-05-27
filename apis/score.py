from flask import Blueprint, Response
from lib.scorer import Scorer
from lib.weather import WeatherStats
from jsonpickle import encode

score_api = Blueprint('score_api', __name__, url_prefix='/api/score')

@score_api.route('/')
def current_score():
    weather_stats = WeatherStats()
    scorer = Scorer(weather_stats)
    return Response(encode(scorer, unpicklable=False), mimetype='application/json')
