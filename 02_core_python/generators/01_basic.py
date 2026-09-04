"""
Topic: Generator Basics with yield
File: 01_basic.py
"""
import sys

def number_sequence_generator(limit: int):
    """Yield numbers 1 to limit lazily without storing them in memory."""
    print("  [Generator started]")
    for i in range(1, limit + 1):
        yield i
    print("  [Generator finished]")


if __name__ == "__main__":
    gen = number_sequence_generator(3)
    print(f"Generator object: {gen}")

    print("Consuming values one by one:")
    for num in gen:
        print(f"  Received: {num}")

    # Memory comparison: List vs Generator
    list_mem = sys.getsizeof([x for x in range(1_000_000)])
    gen_mem = sys.getsizeof((x for x in range(1_000_000)))

    print(f"\nMemory for 1,000,000 ints in List:      {list_mem:,} bytes")
    print(f"Memory for 1,000,000 ints in Generator: {gen_mem:,} bytes")
