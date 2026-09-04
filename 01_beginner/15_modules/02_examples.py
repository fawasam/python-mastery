"""
Topic: Inspecting sys.path & collections Module
File: 02_examples.py
"""
import sys
from collections import Counter, defaultdict

def demonstrate_collections_and_sys() -> None:
    # 1. Inspecting Python search paths
    print("--- sys.path Search Locations ---")
    for idx, path in enumerate(sys.path[:3], 1):
        print(f"  {idx}. {path}")

    # 2. collections.Counter for fast frequency counting
    items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counts = Counter(items)
    print(f"\nCounter result: {counts}")
    print(f"Most common 2: {counts.most_common(2)}")

    # 3. collections.defaultdict for safe grouping
    grouped: defaultdict[str, list[int]] = defaultdict(list)
    grouped["even"].append(2)
    grouped["even"].append(4)
    grouped["odd"].append(1)
    print(f"\ndefaultdict grouping: {dict(grouped)}")


if __name__ == "__main__":
    demonstrate_collections_and_sys()
