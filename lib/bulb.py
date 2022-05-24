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
        if score == 10:
            hue, saturation, value = [120, 100, 50]
        elif score == 9:
            hue, saturation, value = [108, 100, 50]
        elif score == 8:
            hue, saturation, value = [96, 100, 50]
        elif score == 7:
            hue, saturation, value = [84, 100, 50]
        elif score == 6:
            hue, saturation, value = [72, 100, 50]
        elif score == 5:
            hue, saturation, value = [60, 100, 50]
        elif score == 4:
            hue, saturation, value = [48, 100, 50]
        elif score == 3:
            hue, saturation, value = [36, 100, 50]
        elif score == 2:
            hue, saturation, value = [24, 100, 50]
        elif score == 1:
            hue, saturation, value = [12, 100, 50]
        elif score == 0:
            hue, saturation, value = [0, 100, 50]

        await self.update()
        await self.set_hsv(hue, saturation, value)
