"""
Common Mistakes with the Event Loop.
"""

import asyncio


# MISTAKE 1: Calling asyncio.get_event_loop() outside of running context in 3.10+
def mistake_get_event_loop() -> None:
    # Deprecated/Disencouraged: Use asyncio.get_running_loop() inside coroutines or asyncio.run()!
    pass


if __name__ == "__main__":
    print("Inside coroutines, always use asyncio.get_running_loop() to retrieve the active loop!")
