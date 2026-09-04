"""
Solutions for Memory Optimization Exercises.
"""


class SlottedNode:
    __slots__ = ("key", "val")

    def __init__(self, key: str, val: int) -> None:
        self.key = key
        self.val = val


if __name__ == "__main__":
    node = SlottedNode("item1", 42)
    assert node.key == "item1"
    assert node.val == 42
    assert not hasattr(node, "__dict__")  # Confirms instance __dict__ is eliminated!
    print("SlottedNode exercise passed successfully!")
