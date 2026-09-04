"""
Topic: Magic Methods & String Representations
File: 01_basic.py
"""

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # __str__ for human-readable print() string representation
    def __str__(self) -> str:
        return f"Point ({self.x}, {self.y})"

    # __repr__ for unambiguous debugging representation
    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    # __eq__ for custom equality comparison
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    p1 = Point(10.0, 20.0)
    p2 = Point(10.0, 20.0)

    print(f"str(p1):  {p1}")
    print(f"repr(p1): {repr(p1)}")
    print(f"p1 == p2? {p1 == p2}")
