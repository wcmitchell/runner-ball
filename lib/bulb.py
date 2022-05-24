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
