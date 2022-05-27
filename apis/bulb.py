from flask import Blueprint, Response
from lib.bulb import Bulb
from jsonpickle import encode
import os

bulb_api = Blueprint('bulb_api', __name__, url_prefix='/api/bulb')

@bulb_api.route('/')
async def current_bulb_state():
    bulb = Bulb(os.getenv("BULB_HOST"))
    await bulb.update()
    return Response(encode(bulb, unpicklable=False), mimetype='application/json')
