"""
Exercises: Applying SOLID Principles in Python.
"""

from typing import Protocol


class LoggerProtocol(Protocol):
    def log(self, message: str) -> None:
        ...


def refactor_dip(logger: LoggerProtocol, message: str) -> None:
    """
    Exercise 1: Refactor to adhere to DIP.
    Accept any logger conforming to LoggerProtocol instead of instantiating concrete ConsoleLogger.
    
    Level 2 - Medium
    """
    raise NotImplementedError("Refactor to accept dependency interface")


class AreaCalculable(Protocol):
    def area(self) -> float:
        ...


def total_area(shapes: list[AreaCalculable]) -> float:
    """
    Exercise 2: Implement total area calculation following OCP & Polymorphism.
    Calculate total sum of areas for any shapes implementing AreaCalculable.
    
    Level 1 - Easy
    """
    raise NotImplementedError("Implement OCP shape area summation")
