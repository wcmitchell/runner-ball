import json

from lib.reporter import Reporter

class WeatherStats():
    def __init__(self, current_weather):
        self.uv_index = current_weather.uvi
        self.heat_index = current_weather.heat_index
        self.status = current_weather.detailed_status
        self.tempC = current_weather.temperature('celsius')
        self.tempF = current_weather.temperature('fahrenheit')
        self.humidity = current_weather.humidity
        self.cloudpct = current_weather.clouds
        self.dewpoint = current_weather.dewpoint
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
            "Dew Point (F)": self.dewpoint,
            "Humidity": self.humidity,
            "Cloud Cover": self.cloudpct,
            "Snow": self.snow,
            "Rain": self.rain
        }
        Reporter(title="Weather Status", data=data).report()