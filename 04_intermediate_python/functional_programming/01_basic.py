"""
Topic: functools.partial & Pure Functions
File: 01_basic.py
"""
from functools import partial

def power(base: float, exponent: float) -> float:
    """Pure function calculating base raised to exponent."""
    return base ** exponent


# Pre-binding exponent to 2 (square) and 3 (cube)
square = partial(power, exponent=2.0)
cube = partial(power, exponent=3.0)

if __name__ == "__main__":
    print(f"square(5): {square(5.0)}")
    print(f"cube(3):   {cube(3.0)}")
