"""
Solutions: SOLID Exercises.
"""

from typing import Protocol


class LoggerProtocol(Protocol):
    def log(self, message: str) -> None:
        ...


class ConsoleLogger:
    def log(self, message: str) -> None:
        print(f"[LOG]: {message}")


def refactor_dip(logger: LoggerProtocol, message: str) -> None:
    """
    DIP Solution: Functions rely on LoggerProtocol abstraction.
    """
    logger.log(message)


class AreaCalculable(Protocol):
    def area(self) -> float:
        ...


class Rectangle:
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * (self.radius ** 2)


def total_area(shapes: list[AreaCalculable]) -> float:
    """
    OCP Solution: Operates over polymorphic area() calls without type checking.
    """
    return sum(shape.area() for shape in shapes)


if __name__ == "__main__":
    refactor_dip(ConsoleLogger(), "DIP verified successfully.")
    
    shapes: list[AreaCalculable] = [Rectangle(4, 5), Circle(2)]
    print(f"Total calculated area: {total_area(shapes):.2f}")
