"""
Common Mistakes in Python Memory Management.
"""

import sys


# MISTAKE 1: Relying on 'del' to instantly free memory when other references exist
def mistake_del_assumption() -> None:
    data = ["Heavy", "Data", "Block"]
    ref1 = data
    ref2 = data

    print(f"Ref count before del: {sys.getrefcount(data) - 1}")
    del data  # Deletes only the name 'data'. ref1 and ref2 still hold the object!
    print(f"ref1 still exists and contains: {ref1}")


# MISTAKE 2: Strong Circular References without weak references or GC
class NodeBad:
    def __init__(self, name: str) -> None:
        self.name = name
        self.peer = None


def mistake_circular_reference() -> None:
    n1 = NodeBad("Node 1")
    n2 = NodeBad("Node 2")

    # Creates a circular reference loop: n1 -> n2 -> n1
    n1.peer = n2
    n2.peer = n1

    # Dropping local variables leaves ref count of both objects at 1!
    # Simple reference counting cannot free these; Python's cyclic garbage collector is needed.


if __name__ == "__main__":
    print("--- Mistake 1: Assumptions about 'del' ---")
    mistake_del_assumption()

    print("\n--- Mistake 2: Circular References ---")
    mistake_circular_reference()
    print("Circular references require cyclic GC pass to collect.")
