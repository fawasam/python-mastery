"""
Solution for Garbage Collection Exercises.
"""

import gc


def get_gc_summary() -> dict[int, int]:
    counts = gc.get_count()
    return {gen: count for gen, count in enumerate(counts)}


if __name__ == "__main__":
    summary = get_gc_summary()
    print(f"Current GC Object Counts across Generations: {summary}")
