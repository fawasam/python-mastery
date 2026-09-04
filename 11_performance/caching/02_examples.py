"""
Custom TTL (Time-To-Live) Cache Decorator Implementation.
"""

import functools
import time
from typing import Any, Callable


def ttl_cache(ttl_seconds: float = 2.0) -> Callable[..., Any]:
    """
    Decorator implementing a custom Time-To-Live (TTL) cache eviction policy.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        cache: dict[tuple, tuple[float, Any]] = {}

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()

            if key in cache:
                timestamp, result = cache[key]
                if now - timestamp < ttl_seconds:
                    return result

            result = func(*args, **kwargs)
            cache[key] = (now, result)
            return result

        return wrapper

    return decorator


@ttl_cache(ttl_seconds=0.1)
def fetch_timestamped_data() -> float:
    return time.time()


if __name__ == "__main__":
    t1 = fetch_timestamped_data()
    t2 = fetch_timestamped_data()
    assert t1 == t2  # Cache hit within TTL window!

    time.sleep(0.12)  # Wait for TTL to expire
    t3 = fetch_timestamped_data()
    assert t3 != t1  # Cache expired -> New calculation!

    print("TTL cache decorator verification passed successfully!")
