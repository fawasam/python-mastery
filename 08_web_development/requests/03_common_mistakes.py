"""
Common Mistakes when making HTTP Client Requests.
"""

import httpx


# MISTAKE 1: Making un-timed HTTP requests in production
def mistake_no_timeout() -> None:
    # DANGER: httpx.get("https://...") without timeout defaults to unbounded waiting or long defaults.
    # Always specify timeout=5.0!
    pass


if __name__ == "__main__":
    print("Always specify timeouts and use context managers 'with httpx.Client() as client:' for connection pooling!")
