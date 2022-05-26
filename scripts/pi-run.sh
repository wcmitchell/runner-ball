#!/bin/bash

PIPENV_PIPFILE=/home/pi/runner-ball/Pipfile /home/pi/.local/bin/pipenv install && PIPENV_PIPFILE=/home/pi/runner-ball/Pipfile /home/pi/.local/bin/pipenv run python3 /home/pi/runner-ball/app.py
