from kasa import SmartBulb

class Bulb(SmartBulb):
    async def report_bulb_state(bulb):
        await bulb.update()

        print("\n====== Bulb Status ======")
        print(f'Power: {"on" if bulb.is_on else "off"}')
        print(f'Hue:   {bulb.hsv[0]}')
        print(f'Sat:   {bulb.hsv[1]}')
        print(f'Val:   {bulb.hsv[2]}')
        print(f'Temp:  {bulb.color_temp}')
