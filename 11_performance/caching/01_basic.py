"""
Basic Memoization with functools.lru_cache.
"""

import functools
import time


@functools.lru_cache(maxsize=128)
def heavy_database_query_sim(user_id: int) -> dict[str, str | int]:
    time.sleep(0.05)  # Simulate slow query
    return {"id": user_id, "name": f"User_{user_id}"}


def main() -> None:
    # First call: Cache MISS (takes 0.05s)
    t0 = time.perf_counter()
    res1 = heavy_database_query_sim(101)
    t_miss = time.perf_counter() - t0

    # Second call: Cache HIT (instantaneous O(1) response!)
    t1 = time.perf_counter()
    res2 = heavy_database_query_sim(101)
    t_hit = time.perf_counter() - t1

    assert res1 == res2
    print(f"Cache MISS duration: {t_miss * 1000:.2f} ms")
    print(f"Cache HIT  duration: {t_hit * 1000:.4f} ms")

    info = heavy_database_query_sim.cache_info()
    print(f"Cache Info: Hits={info.hits}, Misses={info.misses}, MaxSize={info.maxsize}")


if __name__ == "__main__":
    main()
