import asyncio
import time


async def fetch(name: str, delay: float) -> str:
    print(f"开始请求 {name}")
    await asyncio.sleep(delay)  # 用 sleep 模拟等待网络响应
    print(f"收到 {name} 的响应")
    return f"{name} 的数据"


async def main() -> None:
    started_at = time.perf_counter()

    # 两个协程都会被调度；总耗时接近较慢的那一个，而不是两者之和。
    user, orders = await asyncio.gather(
        fetch("用户服务", 1),
        fetch("订单服务", 2),
    )

    print(user, orders)
    print(f"耗时：{time.perf_counter() - started_at:.1f} 秒")


if __name__ == "__main__":
    asyncio.run(main())
