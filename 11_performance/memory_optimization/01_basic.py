"""
Basic Class Memory Optimization with __slots__.
"""

import sys


class PointStandard:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class PointSlotted:
    __slots__ = ("x", "y")  # Suppresses instance __dict__ creation!

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


def compare_memory_usage() -> None:
    p_std = PointStandard(10.0, 20.0)
    p_slot = PointSlotted(10.0, 20.0)

    # Standard instance has both object overhead AND __dict__ overhead!
    std_bytes = sys.getsizeof(p_std) + sys.getsizeof(p_std.__dict__)
    slot_bytes = sys.getsizeof(p_slot)

    print(f"Standard Point Instance Size : {std_bytes} bytes")
    print(f"Slotted Point Instance Size  : {slot_bytes} bytes")
    print(f"Memory reduction per object : {(1.0 - slot_bytes / std_bytes) * 100:.1f}%")


if __name__ == "__main__":
    compare_memory_usage()
