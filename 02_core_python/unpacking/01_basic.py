"""
Topic: Unpacking & Dictionary Merging
File: 01_basic.py
"""

def demonstrate_unpacking() -> None:
    # 1. Extended starred unpacking
    numbers = [10, 20, 30, 40, 50, 60]
    head, *middle, tail = numbers
    print(f"Head: {head} | Middle: {middle} | Tail: {tail}")

    # 2. Merging dictionaries with ** and | operator (PEP 584)
    defaults = {"host": "localhost", "port": 8080, "timeout": 30}
    overrides = {"port": 9090, "debug": True}

    # Python 3.9+ union operator |
    merged_union = defaults | overrides
    print(f"Merged (Union |): {merged_union}")


if __name__ == "__main__":
    demonstrate_unpacking()
