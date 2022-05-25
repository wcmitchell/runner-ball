from kasa import SmartBulb
from lib.reporter import Reporter
import time

class Bulb(SmartBulb):
    async def report(self):
        await self.update()
        power = "on" if self.is_on else "off"
        data = {
            "Power": power,
            "Hue": self.hsv[0],
            "Sat": self.hsv[1],
            "Val": self.hsv[2],
            "Temp": self.color_temp
        }
        Reporter(title="Bulb Status", data=data).report()


    async def update_from_score(self, scorer):
        score = scorer.score
        saturation = 100
        value = 50

        if score == 5:
            hue = 120
        elif score == 4:
            hue = 96
        elif score == 3:
            hue = 72
        elif score == 2:
            hue = 48
        elif score == 1:
            hue = 24
        elif score == 0:
            hue = 0

        await self.update()
        await self.blink(hue, saturation)
        await self.set_hsv(hue, saturation, value)

    async def blink(self, hue, saturation):
        await self.set_hsv(hue, saturation, 0, transition=1000)
        time.sleep(1)
