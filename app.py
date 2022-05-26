import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from flask import Flask
from apis.weather import current_weather
from kasa.exceptions import SmartDeviceException
from lib.bulb import Bulb
from lib.scorer import Scorer
from lib.signal_handler import SignalHandler
from pyowm.commons.exceptions import InvalidSSLCertificateError, TimeoutError

load_dotenv()

async def main():
    signal_handler = SignalHandler()
    bulb = Bulb(os.getenv("BULB_HOST"))
    await bulb.turn_on()

    while signal_handler.KEEP_ALIVE:
        try:
            weather_stats = current_weather()
            scorer = Scorer(weather_stats)
            await bulb.update_from_score(scorer)
            await report(bulb, weather_stats, scorer)
        except SmartDeviceException as e:
            print(f"Failed to connect to bulb with: {e}")
        except InvalidSSLCertificateError as e:
            print(f"Failed to connect to weather API with: {e}")
        except TimeoutError as e:
            print(f"Connection to weather API timed out with: {e}")
        time.sleep(int(os.getenv("INTERVAL_SECONDS")))

    await bulb.turn_off()

async def report(bulb, weather_stats, scorer):
    os.system("clear")
    await scorer.report()
    await weather_stats.report()
    await bulb.report()

if __name__ == "__main__":
    asyncio.run(main())
