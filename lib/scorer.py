import os
import yaml
from lib.reporter import Reporter

class Scorer():
    def __init__(self, weather_stats):
        self.weather_stats = weather_stats
        self.preferences = self.load_preferences()
        self.score = self.score()

    def load_preferences(self):
        file_path = os.getenv("PREFERENCES_FILE_PATH", "data/preferences.yml")
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def score(self):
        # score all metrics individually here
        # and then weight them based on preferences
        # to determine the final score
        temp_score = self.weighted_score(self.score_temperature(), "temperature")
        precip_score = self.weighted_score(self.score_precipitation(), "rain")
        dew_score = self.weighted_score(self.score_dewpoint(), "dewpoint")
        humidity_score = self.weighted_score(self.score_humidity(), "humidity")
        uvi_score = self.weighted_score(self.score_uvi(), "uvindex")
        cloud_score = self.weighted_score(self.score_clouds(), "cloudcover")
        score = (
            temp_score +
            precip_score +
            dew_score +
            humidity_score +
            uvi_score +
            cloud_score)
        final = round(score / self.total_weights())
        return final

    def total_weights(self):
        weather_preferences = self.preferences.get("weather")
        weights = [v.get("weight", 0) for v in weather_preferences.values()]
        return sum(weights)

    def weighted_score(self, score, preference_key):
        try:
            weight = self.preferences.get("weather").get(preference_key).get("weight")
            return score * weight
        except AttributeError:
            return 0

    def get_ideals(self, stat):
        try:
            ideal_min = self.preferences.get("weather").get(stat).get("ideal_min")
            ideal_max = self.preferences.get("weather").get(stat).get("ideal_max")
            return (ideal_min, ideal_max)
        except AttributeError:
            return None

    def score_bin_stat(self, stat, current):
        allowed = self.preferences.get("weather").get(stat).get("allowed")
        if (current and allowed) or not current:
            return 5
        else:
            return 0

    def score_range_stat(self, stat, current, range_min, range_max):
        try:
            min_stat_pref = self.preferences.get("weather").get(stat).get("ideal_min")
            max_stat_pref = self.preferences.get("weather").get(stat).get("ideal_max")
            return self.determine_score(
                range_min=range_min,
                range_max=range_max,
                pref_min=min_stat_pref,
                pref_max=max_stat_pref,
                current=current)
        except AttributeError:
            return 0

    def score_temperature(self):
        current_temp = self.weather_stats.tempF.get("temp")
        return self.score_range_stat(
            stat="temperature",
            current=current_temp,
            range_min=-10,
            range_max=110)

    def score_dewpoint(self):
        current_dewpoint = self.weather_stats.dewpoint
        return self.score_range_stat(
            stat="dewpoint",
            current=current_dewpoint,
            range_min=0,
            range_max=100)

    def score_precipitation(self):
        current_rain = self.weather_stats.rain
        return self.score_bin_stat(
            stat="rain",
            current=current_rain)

    def score_uvi(self):
        current_uvi = self.weather_stats.uv_index
        return self.score_range_stat(
            stat="uvindex",
            current=current_uvi,
            range_min=0,
            range_max=11
        )

    def score_humidity(self):
        current_humidity = self.weather_stats.humidity
        return self.score_range_stat(
            stat="humidity",
            current=current_humidity,
            range_min=0,
            range_max=100
        )

    def score_clouds(self):
        current_cloudpct = self.weather_stats.cloudpct
        return self.score_range_stat(
            stat="cloudcover",
            current=current_cloudpct,
            range_min=0,
            range_max=10
        )


    def determine_score(self, **kwargs):
        range_min = kwargs.get("range_min")
        range_max = kwargs.get("range_max")
        pref_min = kwargs.get("pref_min")
        pref_max = kwargs.get("pref_max")
        current = kwargs.get("current")
        total_range = range_max - range_min
        in_ideal_range = pref_min <= current <= pref_max

        if in_ideal_range:
            return 5

        if current > pref_max:
            diff = current - pref_max
        elif current < pref_min:
            diff = current - pref_min

        percentage_diff = abs(diff) / total_range

        if percentage_diff < 0.1:
            return 4
        elif percentage_diff < 0.2:
            return 3
        elif percentage_diff < 0.3:
            return 2
        elif percentage_diff < 0.4:
            return 1
        else:
            return 0


    async def report(self):
        ideal_temp = self.get_ideals("temperature")
        ideal_dewpoint = self.get_ideals("dewpoint")
        ideal_humidity = self.get_ideals("humidity")
        ideal_cloudpct = self.get_ideals("cloudcover")
        data = {
                "Score": f"{self.score}/5",
            }
        if ideal_temp:
            data["Ideal Min Temp"], data["Ideal Max Temp"] = ideal_temp
        if ideal_dewpoint:
            data["Ideal Min Dew Point"], data["Ideal Max Dew Point"] = ideal_dewpoint
        if ideal_humidity:
            data["Ideal Min Humidity"], data["Ideal Max Humidity"] = ideal_humidity
        if ideal_cloudpct:
            data["Ideal Min Cloud Cover"], data["Ideal Max Cloud Cover"] = ideal_cloudpct
        Reporter(title="Running Score", data=data).report()
