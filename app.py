import asyncio
import os
import time

from dotenv import load_dotenv
from flask import Flask
from apis.weather import currentWeather, report_weather
from lib.bulb import Bulb
from lib.signal_handler import SignalHandler

load_dotenv()

async def main():
    signal_handler = SignalHandler()
    bulb = Bulb(os.getenv("BULB_HOST"))
    await bulb.turn_on()

    while signal_handler.KEEP_ALIVE:
        # call the weather API
        current_weather = currentWeather()

        await log_status(bulb, current_weather)
        time.sleep(int(os.getenv("INTERVAL_SECONDS")))

    await bulb.turn_off()

async def log_status(bulb, current_weather):
    os.system("clear")
    await Bulb.report_bulb_state(bulb)
    await report_weather(current_weather)

if __name__ == "__main__":
    asyncio.run(main())
