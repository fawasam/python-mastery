"""
Modular Design Basics: Controlling Exports and Package Interfaces.
"""

# Explicitly declare public API exported by this module
__all__ = ["CalculatorService"]


class CalculatorService:
    """Public service class intended for consumer import."""
    def add(self, a: float, b: float) -> float:
        return a + b


class _InternalHelper:
    """Private implementation detail omitted from __all__ export list."""
    def internal_math(self) -> None:
        pass


if __name__ == "__main__":
    calc = CalculatorService()
    print("Exported Calc Result:", calc.add(10, 20))
