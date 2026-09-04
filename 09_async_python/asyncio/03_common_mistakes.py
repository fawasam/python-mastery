"""
Common Mistakes in asyncio.
"""

import asyncio


# MISTAKE 1: Nesting asyncio.run() calls
async def inner_coroutine() -> None:
    # DANGER: Calling asyncio.run() inside an already running event loop raises:
    # RuntimeError: asyncio.run() cannot be called from a running event loop!
    pass


if __name__ == "__main__":
    print("Call asyncio.run() ONCE as the top-level entrypoint of your script!")
