import asyncio
from asyncio.subprocess import Process

async def main():
    process:Process=await asyncio.create_subprocess_exec("sleep","3")
    print(f"process pid is:{process.pid}")
    try:
        status_code=await asyncio.wait_for(process.wait(),timeout=1.0)
    except asyncio.TimeoutError as e:
        process.terminate()
        print(e)
        status_code=await process.wait()
        print(status_code)

asyncio.run(main())