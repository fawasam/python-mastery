"""
Common Algorithmic Performance Traps and Pitfalls.
"""


def mistake_1_string_concatenation_in_loop() -> str:
    """
    MISTAKE: Repeatedly concatenating strings with += in a loop.
    WHY: Strings in Python are immutable. Each += creates a brand new string and copies data,
    leading to O(n^2) total allocation cost.
    """
    words = ["word"] * 1000
    res = ""
    for w in words:
        res += w + " "  # Bad: creates new string on every iteration
    return res


def fix_1_string_join() -> str:
    """
    FIX: Use str.join() on a sequence.
    WHY: Allocates memory once for the total length, running in O(n) time.
    """
    words = ["word"] * 1000
    return " ".join(words) + " "


def mistake_2_repeated_sorting() -> None:
    """
    MISTAKE: Sorting an entire list inside a loop just to find the min/max or top k elements.
    WHY: Sorting costs O(n log n) per iteration, resulting in O(m * n log n) overall.
    """
    data = [5, 2, 8, 1, 9, 3]
    # Bad: sorting just to get minimum
    minimum = sorted(data)[0]  # Wasteful O(n log n) when min() is O(n)
    _ = minimum


def fix_2_use_min_or_heap() -> None:
    """
    FIX: Use built-in min()/max() or heapq module for top-K elements.
    WHY: min() operates in O(n) linear scan without modifying or copying the list.
    """
    data = [5, 2, 8, 1, 9, 3]
    minimum = min(data)  # Optimal O(n)
    _ = minimum


if __name__ == "__main__":
    print("Executed mistake analysis module successfully.")
