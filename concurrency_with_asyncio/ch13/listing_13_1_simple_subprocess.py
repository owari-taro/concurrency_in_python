import asyncio
from asyncio.subprocess import Process
import time


async def main():
    process:Process=await asyncio.create_subprocess_exec("sleep","10")
    print(f"process pid is :{process.pid}")
    print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
    status_code=await process.wait()
    print(f"status code:{status_code}")

asyncio.run(main())