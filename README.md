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
LOCATION="your location for weather results"
```

Run:
```
$ python3 ./app.py
```

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
