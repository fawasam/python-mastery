"""
Profiling Context Manager for Inline Function Block Analysis.
"""

import cProfile
from contextlib import contextmanager
import pstats


@contextmanager
def profile_block(title: str = "Code Block"):
    profiler = cProfile.Profile()
    profiler.enable()
    try:
        yield
    finally:
        profiler.disable()
        print(f"\n================ PROFILE RESULTS FOR: '{title}' ================")
        stats = pstats.Stats(profiler).sort_stats("tottime")
        stats.print_stats(5)
        print("====================================================================")


def heavy_task() -> list[int]:
    return [x**2 for x in range(200_000)]


if __name__ == "__main__":
    with profile_block("Heavy Square List Generation"):
        res = heavy_task()
    print(f"Generated {len(res)} items under profile block.")
