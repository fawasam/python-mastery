"""
Basic Reference Counting and Object Identity in Python.
"""

import sys


def demonstrate_ref_counts() -> None:
    # Create an initial list object
    data = ["Python", "Memory", "Management"]
    # sys.getrefcount includes the temporary reference passed to getrefcount itself
    print(f"Initial ref count of 'data': {sys.getrefcount(data) - 1}")

    alias = data
    print(f"Ref count after alias assignment: {sys.getrefcount(data) - 1}")

    container = [data]
    print(f"Ref count after inserting into list container: {sys.getrefcount(data) - 1}")

    del alias
    print(f"Ref count after deleting 'alias': {sys.getrefcount(data) - 1}")

    del container
    print(f"Ref count after deleting 'container': {sys.getrefcount(data) - 1}")


def demonstrate_integer_caching() -> None:
    # Python caches small integers in the range [-5, 256]
    a = 100
    b = 100
    print(f"a is b (Small Int 100): {a is b}")  # True - Same memory address

    x = 1000
    y = 1000
    print(f"x is y (Large Int 1000): {x is y}")  # False in standard Python runtime evaluation


if __name__ == "__main__":
    print("--- Reference Count Demonstration ---")
    demonstrate_ref_counts()

    print("\n--- Small Integer Caching Demonstration ---")
    demonstrate_integer_caching()
