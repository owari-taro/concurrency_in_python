import asyncio
from utils import delay

async def hello_every_second(seconds:int):
    for i in range(2):
        await asyncio.sleep(seconds)
        print(" Im running other code while Im wating")

async def main():
    firest=asyncio.create_task(delay(3))
    second=asyncio.create_task(delay(3))
    await asyncio.sleep(6)
    await hello_every_second(5)
    await firest
    await second
    print("ka;lfkasd;lfkaldfkasd;lfk")
if __name__=="__main__":

    asyncio.run(main())