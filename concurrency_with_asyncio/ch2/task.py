import asyncio
from utils import delay

async def main():
    sleep=asyncio.create_task(delay(3))
    print(type(sleep),"******************************************************")
    result=await sleep
    print(result)

if __name__=="__main__":
    asyncio.run(main())