import asyncio
import os
import time

from dotenv import load_dotenv
from apis.bulb import Bulb
from lib.signal_handler import SignalHandler

load_dotenv()

async def main():
    signal_handler = SignalHandler()
    bulb = Bulb(os.getenv("BULB_HOST"))
    await bulb.turn_on()

    while signal_handler.KEEP_ALIVE:
        # call the weather API
        current_weather = {}

        await log_status(bulb)
        time.sleep(int(os.getenv("INTERVAL_SECONDS")))

    await bulb.turn_off()

async def log_status(bulb):
    os.system("clear")
    await Bulb.report_bulb_state(bulb)
    # report weather

if __name__ == "__main__":
    asyncio.run(main())
