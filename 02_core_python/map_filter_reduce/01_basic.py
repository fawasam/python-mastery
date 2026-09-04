"""
Topic: Map, Filter, and Reduce Basics
File: 01_basic.py
"""
from functools import reduce

def demonstrate_functional_primitives() -> None:
    raw_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 1. map(): Transform elements
    squared = list(map(lambda x: x**2, raw_data))
    print(f"map (squared):    {squared}")

    # 2. filter(): Select matching elements
    odds = list(filter(lambda x: x % 2 != 0, raw_data))
    print(f"filter (odds):    {odds}")

    # 3. reduce(): Accumulate values
    total_sum = reduce(lambda acc, val: acc + val, raw_data, 0)
    print(f"reduce (total):   {total_sum}")


if __name__ == "__main__":
    demonstrate_functional_primitives()
