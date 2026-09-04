"""
Topic: @property & Computed Attributes
File: 01_basic.py
"""

class Circle:
    def __init__(self, radius: float) -> None:
        self._radius = max(0.0, radius)

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, val: float) -> None:
        if val < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = val

    # Computed property (derived dynamically)
    @property
    def area(self) -> float:
        import math
        return round(math.pi * (self._radius ** 2), 2)


if __name__ == "__main__":
    c = Circle(5.0)
    print(f"Radius: {c.radius} | Area: {c.area}")

    c.radius = 10.0
    print(f"Updated Radius: {c.radius} | New Area: {c.area}")
