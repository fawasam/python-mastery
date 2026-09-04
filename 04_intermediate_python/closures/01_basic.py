"""
Basic Closures and Nonlocal Variables in Python.
"""

from typing import Callable


def make_multiplier(factor: float) -> Callable[[float], float]:
    """
    Function factory returning a closure that multiplies its input by 'factor'.
    """

    def multiply(number: float) -> float:
        # 'factor' comes from the enclosing scope of make_multiplier.
        # Even after make_multiplier returns, multiply retains access to 'factor'.
        return number * factor

    return multiply


def make_accumulator(initial_total: float = 0.0) -> Callable[[float], float]:
    """
    Stateful closure using the 'nonlocal' keyword to modify state across calls.
    """
    total = initial_total

    def add(amount: float) -> float:
        nonlocal total  # Tells Python 'total' belongs to outer enclosing scope
        total += amount
        return total

    return add


if __name__ == "__main__":
    double = make_multiplier(2.0)
    triple = make_multiplier(3.0)

    print(f"double(5) = {double(5.0)}")  # 10.0
    print(f"triple(5) = {triple(5.0)}")  # 15.0

    # Inspect closure cell contents
    if double.__closure__:
        print(f"Captured variable in 'double': {double.__closure__[0].cell_contents}")

    acc = make_accumulator(10.0)
    print(f"Accumulator + 5 -> {acc(5.0)}")  # 15.0
    print(f"Accumulator + 20 -> {acc(20.0)}")  # 35.0
