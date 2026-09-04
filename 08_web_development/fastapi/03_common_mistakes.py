"""
Common Mistakes in FastAPI Applications.
"""


# MISTAKE 1: Blocking sync calls inside async def route handlers
# In FastAPI:
# - Plain 'def' handlers run in an external thread pool (safe for blocking I/O like standard database calls or time.sleep).
# - 'async def' handlers run directly on the event loop (blocking I/O inside async def freezes the ENTIRE event loop for all users!).
def mistake_async_blocking() -> None:
    pass


if __name__ == "__main__":
    print("If your route handler performs synchronous blocking I/O (e.g. standard time.sleep or sync DB query), declare it as plain 'def route()', NOT 'async def route()'!")
