"""
Common Mistakes in Async HTTP Client Usage.
"""

import httpx


# MISTAKE 1: Re-instantiating httpx.AsyncClient inside tight request loops
async def mistake_recreating_clients(urls: list[str]) -> None:
    # DANGER: Instantiating 'async with httpx.AsyncClient()' inside the loop destroys connection pooling!
    # Always create ONE shared AsyncClient instance outside the loop for all requests!
    pass


if __name__ == "__main__":
    print("Reuse a single shared 'async with httpx.AsyncClient() as client:' session across concurrent batch requests!")
