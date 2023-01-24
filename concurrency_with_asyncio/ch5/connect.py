import asyncpg, asyncio


async def main():
    conn = await asyncpg.connect(
        host="localhost",
        port=5433,
        user="postgres",
        database="postgres",
        password="postgres",
    )
    version = conn.get_server_version()
    print(version)
    await conn.close()


asyncio.run(main())
