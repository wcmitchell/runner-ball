import yaml

class Scorer():
    def __init__(self, weather_stats):
        self.weather_stats = weather_stats
        self.preferences = self.load_preferences()

    def load_preferences(self):
        with open("data/preferences.yml", "r") as file:
            return yaml.safe_load(file)

    def score(self):
        return self.score_temperature()

    def score_temperature(self):
        temp_score = 0
        temp_low = -10
        temp_high = 110
        temp_range = temp_high - temp_low
        current_temp = self.weather_stats.tempF.get("temp")
        min_temp_pref = self.preferences.get("weather").get("temperature").get("ideal_min")
        max_temp_pref = self.preferences.get("weather").get("temperature").get("ideal_max")
        in_ideal_range = min_temp_pref <= current_temp <= max_temp_pref

        if in_ideal_range:
            temp_score = 10
        else:
            if current_temp > max_temp_pref:
                diff = current_temp - max_temp_pref

            if current_temp < min_temp_pref:
                diff = current_temp - min_temp_pref

            percentage_diff = abs(diff) / temp_range

            if percentage_diff < 0.1:
                temp_score = 9
            elif percentage_diff < 0.2:
                temp_score = 8
            elif percentage_diff < 0.3:
                temp_score = 7
            elif percentage_diff < 0.4:
                temp_score = 6
            elif percentage_diff < 0.5:
                temp_score = 5
            elif percentage_diff < 0.6:
                temp_score = 4
            elif percentage_diff < 0.7:
                temp_score = 3
            elif percentage_diff < 0.8:
                temp_score = 2
            elif percentage_diff < 0.9:
                temp_score = 1
            elif percentage_diff < 1:
                temp_score = 0

        return temp_score

    async def report_score(self):
        print("\n====== Running Score ======")
        print(f"Score:          {self.score()}/10")
        print(f"Ideal Min Temp: {self.preferences.get('weather').get('temperature').get('ideal_min')}")
        print(f"Ideal Max Temp: {self.preferences.get('weather').get('temperature').get('ideal_max')}")
