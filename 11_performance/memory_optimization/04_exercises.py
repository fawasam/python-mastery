"""
Memory Optimization Exercises.
"""


# Exercise 1 (Easy): Create a Slotted Data Class
# Define a class SlottedNode with __slots__ = ("key", "val")
class SlottedNode:
    __slots__ = ("key", "val")

    def __init__(self, key: str, val: int) -> None:
        raise NotImplementedError("Implement SlottedNode __init__")
