import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def open_connection():
    print("建立连接")
    await asyncio.sleep(0.1)
    connection = {"name": "reporting-db"}
    try:
        yield connection
    finally:
        print("关闭连接")
        await asyncio.sleep(0.1)


async def main() -> None:
    async with open_connection() as connection:
        print(f"查询 {connection['name']}")


if __name__ == "__main__":
    asyncio.run(main())
