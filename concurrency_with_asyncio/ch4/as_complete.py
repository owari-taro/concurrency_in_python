import asyncio
import aiohttp
from utils import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        fetchers=[fetch_status(session,"https://example.com",1),
        fetch_status(session,"https://www.example.com",30),
        fetch_status(session,"https://www.example.com",3)]
        count=0
        for finished_task in asyncio.as_completed(fetchers):
            print("hoge")
            #終わったタスクからloopされる
            print(await finished_task)


asyncio.run(main())