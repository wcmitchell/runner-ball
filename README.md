# Runner Ball

A weather ball for runners.

## Description

This project is intended to initially integrate with a Kasa smart bulb and a
weather API, to give real-time feedback on the "score" or the current running conditions
(green to red) based on your local weather, and your ideal running conditions.

This feedback will be rendered via the Kasa bulb. Initially, location, ideal running
conditions, and other data will be sourced via YAML.

### Dependencies

* Python 3.9
* Pipenv

### Running the app

Install dependencies:
```bash
$ pipenv --python 3.9
$ pipenv shell
$ pipenv install
```

Set your environment by saving `.env-example` as `.env`:
```
BULB_HOST="the host of your smart bulb (see Kasa docs below)"
INTERVAL_SECONDS="how often the event loop should run in seconds"
OWM_APIKEY="your OpenWeather API key"
COUNTRY="two letter country code"
CITY="city name"
STATE="two letter state code"
```

#### Run the async process to update your bulb:
This will kick off a process that will continually ping the weather API based on
`INTERVAL_SECONDS` and update your score/bulb accordingly, at that interval. **It
is _not_ dependent on the Flask API to run.**
```
$ python3 ./app.py
```

#### Run the Flask API service:
This will expose APIs to render real-time data for weather, your bulb, and your
score context. **It is _not_ dependent on the async process to run.**
```
$ flask run
```
Available APIs:
| API                                          | Description                                                                |
| -------------------------------------------- | -------------------------------------------------------------------------- |
| /api/weather/                                | Current weather, based on location                                         |
| /api/weather/forecast/                       | Full weather forecast, based on location                                   |
| /api/weather/forecast/minutely|hourly|daily/ | Optional granular (minutely|hourly|daily) forecast, based on location      |
| /api/bulb/                                   | Current and historical data from your Kasa bulb                            |
| /api/score/                                  | Your current running score (and context), based on weather and preferences |

## Preferences
Ideal weather/running preferences are set in a yaml file, default location being
`/data/preferences.yml`. These preferences help drive the program to consider your
current local weather, against your preferences, to render a "score".

### Scoring
A "score" is a number, from 0-5, which represents how ideal the current weather is
for running, compared to your preferences. With 0 being the worst, and 5 being the
best, this score will be communicated through your smart bulb. A gradient from
red (0) through yellow, to green (5) will be illuminated based on the score.

Updating your `INTERVAL_SECONDS` environment variable will drive how often the
weather API is pinged to update your score/bulb. On each update, your bulb will
blink to give you visual feedback that the bulb and API are still communicating
with the service.

### Weighting
Scoring is influenced by weighting. In `/data/preferences.yml` for each weather
metric, you'll be able to add a `weight` with a value of 1-100. How you weight
each metric will influence the importance of the results as compared to your
current weather. A higher weight will give the comparison more impact on your
final score.

## Raspberry Pi
If you'd like to use a Raspberry Pi to run the program headless and control the bulb
in the background on boot, do the following:

- Clone this repo into `/home/pi/` on your Raspberry Pi
- Run `./scripts/pi-install.sh`

This will add a systemd unit file which will ensure internet connectivity prior
to starting the service, and will start the service immediately, and on boot.

- To stop the service: `systemctl stop runner-ball.service`
- To start the service manually: `systemctl stop runner-ball.service`
- To check service status: `systemctl status runner-ball.service`

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Future Improvements

* Power with a Raspberry Pi to run on boot
* Power the user-driven data with a UI
* Indicate forecasted changes (either positive or negative) with a short burst in either direction of the "score" gradient

## Resources

* [Kasa API Library](https://github.com/python-kasa/python-kasa)
* [Kasa API Docs](https://python-kasa.readthedocs.io/en/latest/smartdevice.html)
* [OpenWeather API Library](https://github.com/csparpa/pyowm)
* [OpenWeather API Docs](https://openweathermap.org/api)
