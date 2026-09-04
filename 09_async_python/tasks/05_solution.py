"""
Solutions for Task Exercises.
"""

import asyncio


async def delayed_square(x: int) -> int:
    await asyncio.sleep(0.01)
    return x * x


async def run_parallel_squares(values: list[int]) -> list[int]:
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(delayed_square(v)) for v in values]
    return [t.result() for t in tasks]


async def main() -> None:
    res = await run_parallel_squares([2, 3, 4])
    assert res == [4, 9, 16]
    print(f"Parallel TaskGroup squares result: {res}")


if __name__ == "__main__":
    asyncio.run(main())
