import asyncio
from asyncio.subprocess import Process

async def main():
    program=["python3","listing_13_4_many_outputs.py"]
    process:Process=await asyncio.create_subprocess_exec(*program,
        stdout=asyncio.subprocess.PIPE)
    print(f"process pid is:{process.pid}")
    return_code=await process.wait()
    print(f"process returned:{return_code}")

asyncio.run(main())