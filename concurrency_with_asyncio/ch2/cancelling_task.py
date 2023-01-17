import asyncio
from asyncio import CancelledError
from utils import delay

async def main():
    #
    long_task=asyncio.create_task(delay(10))