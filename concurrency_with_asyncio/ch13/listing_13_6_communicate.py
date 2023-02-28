import asyncio
from asyncio.subprocess import Process

async def main():
    program=["python3","listing_13_4_many_outputs.py"]
    process:Process=await asyncio.create_subprocess_exec(*program,stdout=asyncio.subprocess.PIPE)
    print(f" process pid is:{process.pid}")
    stdout,stderr=await process.communicate()
    print(stdout)
    print(stderr)
    print(f"process returned:{process.returncode}")
asyncio.run(main())