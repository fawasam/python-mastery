"""
Inspecting Native Coroutine States.
"""

import asyncio
import inspect


async def sample_coroutine() -> str:
    print("[COROUTINE] Running inside event loop...")
    await asyncio.sleep(0.05)
    return "Finished"


def demo_coroutine_states() -> None:
    # 1. Instantiate coroutine (State: CORO_CREATED)
    coro = sample_coroutine()
    print(f"State upon instantiation: {inspect.getcoroutinestate(coro)}")

    # 2. Run coroutine to completion
    asyncio.run(coro)

    # 3. State after completion: CORO_CLOSED
    print(f"State after completion: {inspect.getcoroutinestate(coro)}")


if __name__ == "__main__":
    demo_coroutine_states()
