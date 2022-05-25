from kasa import SmartBulb

class Bulb(SmartBulb):
    async def report(self):
        await self.update()

        print("\n====== Bulb Status ======")
        print(f'Power: {"on" if self.is_on else "off"}')
        print(f'Hue:   {self.hsv[0]}')
        print(f'Sat:   {self.hsv[1]}')
        print(f'Val:   {self.hsv[2]}')
        print(f'Temp:  {self.color_temp}')

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
        await self.set_hsv(hue, saturation, value)
