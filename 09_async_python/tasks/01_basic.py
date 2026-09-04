"""
Basic Background Task Scheduling with asyncio.create_task().
"""

import asyncio


async def background_telemetry_logger(event_name: str) -> str:
    print(f"[TASK] Logging event '{event_name}' in background...")
    await asyncio.sleep(0.05)
    return f"Logged: {event_name}"


async def main() -> None:
    # Schedule background task
    task1 = asyncio.create_task(background_telemetry_logger("USER_LOGIN"))
    task2 = asyncio.create_task(background_telemetry_logger("CHECKOUT_COMPLETE"))

    print("[MAIN] Main routine continues immediately while background tasks execute...")
    assert task1.done() is False

    # Await results when ready
    res1 = await task1
    res2 = await task2

    assert task1.done() is True
    print(f"[MAIN] Background Task Results: {res1} | {res2}")


if __name__ == "__main__":
    asyncio.run(main())
