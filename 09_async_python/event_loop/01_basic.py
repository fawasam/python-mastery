"""
Basic Event Loop Access and Callback Scheduling.
"""

import asyncio


def sync_callback(msg: str) -> None:
    print(f"[CALLBACK] Executed: {msg}")


async def main() -> None:
    # Obtain reference to current running event loop
    loop = asyncio.get_running_loop()

    # Schedule non-blocking sync callbacks on event loop queue
    loop.call_soon(sync_callback, "Immediate Callback")
    loop.call_later(0.05, sync_callback, "Delayed Callback (50ms)")

    print("[MAIN] Event loop running main coroutine...")
    await asyncio.sleep(0.1)  # Allow scheduled callbacks to fire
    print("[MAIN] Main coroutine completed.")


if __name__ == "__main__":
    asyncio.run(main())
