import asyncio
from utils import delay

async def hello_every_second(seconds:int):
    for i in range(4):
        await asyncio.sleep(seconds)
        print(" Im running other code while Im wating")

async def main():
    firest=asyncio.create_task(delay(3))
    second=asyncio.create_task(delay(3))
    await hello_every_second(2)
    await firest
    await second
if __name__=="__main__":

    asyncio.run(main())