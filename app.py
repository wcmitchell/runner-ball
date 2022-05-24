import asyncio
import os
import time

from dotenv import load_dotenv
from flask import Flask
from apis.weather import current_weather
from lib.bulb import Bulb
from lib.scorer import Scorer
from lib.signal_handler import SignalHandler

load_dotenv()

async def main():
    signal_handler = SignalHandler()
    bulb = Bulb(os.getenv("BULB_HOST"))
    await bulb.turn_on()

    while signal_handler.KEEP_ALIVE:
        weather_stats = current_weather()
        scorer = Scorer(weather_stats)

        await report(bulb, weather_stats, scorer)
        time.sleep(int(os.getenv("INTERVAL_SECONDS")))

    await bulb.turn_off()

async def report(bulb, weather_stats, scorer):
    os.system("clear")
    await scorer.report()
    await weather_stats.report()
    await bulb.report()

if __name__ == "__main__":
    asyncio.run(main())
