"""
Generators Basics: Two-Way Communication with generator.send().
"""

from typing import Generator


def accumulative_averager() -> Generator[float, float, None]:
    """
    Generator coroutine keeping a running average of values pushed via send().
    """
    total = 0.0
    count = 0
    average = 0.0

    while True:
        # Receive value pushed from caller via generator.send()
        val = yield average
        if val is not None:
            total += val
            count += 1
            average = total / count


if __name__ == "__main__":
    coro = accumulative_averager()
    next(coro)  # Prime generator to first yield statement

    print("Avg after sending 10.0:", coro.send(10.0))
    print("Avg after sending 20.0:", coro.send(20.0))
    print("Avg after sending 30.0:", coro.send(30.0))
