import yaml

class Scorer():
    def __init__(self, weather_stats):
        self.weather_stats = weather_stats
        self.preferences = self.load_preferences()
        self.score = self.score()

    def load_preferences(self):
        with open("data/preferences.yml", "r") as file:
            return yaml.safe_load(file)

    def score(self):
        # score all metrics individually here
        # and then weight them based on preferences
        # to determine the final score
        return self.score_temperature()

    def score_temperature(self):
        current_temp = self.weather_stats.tempF.get("temp")
        min_temp_pref = self.preferences.get("weather").get("temperature").get("ideal_min")
        max_temp_pref = self.preferences.get("weather").get("temperature").get("ideal_max")
        return self.determine_score(
            range_min=-10,
            range_max=110,
            pref_min=min_temp_pref,
            pref_max=max_temp_pref,
            current=current_temp)

    def determine_score(self, **kwargs):
        range_min = kwargs.get("range_min")
        range_max = kwargs.get("range_max")
        pref_min = kwargs.get("pref_min")
        pref_max = kwargs.get("pref_max")
        current = kwargs.get("current")
        total_range = range_max - range_min
        in_ideal_range = pref_min <= current <= pref_max

        if in_ideal_range:
            return 10

        if current > pref_max:
            diff = current - pref_max
        elif current < pref_min:
            diff = current - pref_min

        percentage_diff = abs(diff) / total_range

        if percentage_diff < 0.1:
            return 9
        elif percentage_diff < 0.2:
            return 8
        elif percentage_diff < 0.3:
            return 7
        elif percentage_diff < 0.4:
            return 6
        elif percentage_diff < 0.5:
            return 5
        elif percentage_diff < 0.6:
            return 4
        elif percentage_diff < 0.7:
            return 3
        elif percentage_diff < 0.8:
            return 2
        elif percentage_diff < 0.9:
            return 1
        elif percentage_diff < 1:
            return 0

    async def report(self):
        print("\n====== Running Score ======")
        print(f"Score:          {self.score}/10")
        print(f"Ideal Min Temp: {self.preferences.get('weather').get('temperature').get('ideal_min')}")
        print(f"Ideal Max Temp: {self.preferences.get('weather').get('temperature').get('ideal_max')}")
