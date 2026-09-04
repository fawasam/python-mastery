"""
Common Mistakes in Memory Optimization with __slots__.
"""


class BaseSlotted:
    __slots__ = ("x",)


class DerivedWithoutSlots(BaseSlotted):
    # DANGER: If a derived child class does NOT declare __slots__, Python automatically
    # re-introduces instance __dict__ for child objects, losing the memory savings!
    pass


if __name__ == "__main__":
    print("Always declare __slots__ = () or __slots__ = ('child_attr',) in child classes inheriting from slotted base classes!")
