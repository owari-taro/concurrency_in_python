import asyncio
import functools
from typing import Callable,Any
import time
async def delay(seconds:int)->int:
    print(f"sleeping for {seconds}")
    await asyncio.sleep(seconds)
    print(f"finisihed sleeping for {seconds}")
    return seconds


def async_timed():
    def wrapper(func:Callable)->Callable:
        async def wrapped(*args,**kwargs)->Any:
            print(f"starting {func} with args {args} {kwargs}")
            start=time.time()
            try:
                return await func(*args,**kwargs)
            finally:
                end=time.time()
                total=end-start
                print(f"finished {func} in {total:.4f} seconds")
        return wrapped
    return wrapper