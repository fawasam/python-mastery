"""
Topic: Common Recursion Mistakes (RecursionError)
File: 03_common_mistakes.py
"""
import sys

def mistake_1_missing_base_case() -> None:
    # ❌ WRONG: Function calls itself without stopping condition!
    # def infinite_rec(n): return infinite_rec(n + 1)
    # RecursionError: maximum recursion depth exceeded in comparison

    limit = sys.getrecursionlimit()
    print(f"Python default recursion limit: {limit} frames")


if __name__ == "__main__":
    mistake_1_missing_base_case()
