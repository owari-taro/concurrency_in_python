import asyncio
from utils import delay

async def main():
    sleep=asyncio.create_task(delay(3))
    sleep_again=asyncio.create_task(delay(3))
    sleep_last=asyncio.create_task(delay(3))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    await sleep
    await sleep_again
    await sleep_last

asyncio.run(main())
