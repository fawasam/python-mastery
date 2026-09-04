"""
Exercises: Implementing Design Patterns in Python.
"""

from typing import Protocol


class TargetPrinter(Protocol):
    def print_text(self, text: str) -> None:
        ...


class OldPrinter:
    def legacy_print(self, msg: str) -> None:
        print(f"OLD: {msg}")


def create_printer_adapter(old_printer: OldPrinter) -> TargetPrinter:
    """
    Exercise 1: Create an Adapter wrapping OldPrinter so it satisfies TargetPrinter.
    
    Level 1 - Easy
    """
    raise NotImplementedError("Implement OldPrinter to TargetPrinter Adapter")


class StrategyInterface(Protocol):
    def format(self, text: str) -> str:
        ...


def apply_formatting_strategy(strategy: StrategyInterface, text: str) -> str:
    """
    Exercise 2: Apply strategy to format text.
    
    Level 1 - Easy
    """
    raise NotImplementedError("Apply strategy to text")
