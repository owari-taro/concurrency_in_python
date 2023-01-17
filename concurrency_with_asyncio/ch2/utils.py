import asyncio

async def delay(seconds:int)->int:
    print(f"sleeping for {seconds}")
    await asyncio.sleep(seconds)
    print(f"finisihed sleeping for {seconds}")
    return seconds

    