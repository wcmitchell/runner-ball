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

### Installing

```bash
$ pipenv --python 3.9
$ pipenv shell
$ pipenv install
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Future Improvements

* Power with a Raspberry Pi to run on boot
* Power the user-driven data with a UI

## Resources

* [Kasa API](https://github.com/python-kasa/python-kasa)
* [Kasa API Docs](https://python-kasa.readthedocs.io/en/latest/smartdevice.html)
