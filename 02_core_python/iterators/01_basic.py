"""
Topic: Iteration Protocol Basics
File: 01_basic.py
"""

def demonstrate_iteration_protocol() -> None:
    numbers = [10, 20, 30]

    # 1. Obtain an iterator from iterable
    number_iterator = iter(numbers)
    print(f"Iterator object: {number_iterator}")

    # 2. Call next() explicitly
    print(f"next(): {next(number_iterator)}")
    print(f"next(): {next(number_iterator)}")
    print(f"next(): {next(number_iterator)}")

    # 3. Next call raises StopIteration exception
    try:
        next(number_iterator)
    except StopIteration:
        print("Caught StopIteration: Iterator is fully exhausted!")


if __name__ == "__main__":
    demonstrate_iteration_protocol()
