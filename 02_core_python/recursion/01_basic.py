"""
Topic: Recursion Basics
File: 01_basic.py
"""

def factorial(n: int) -> int:
    """Calculate factorial of n recursively."""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers.")
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Step
    return n * factorial(n - 1)


if __name__ == "__main__":
    num = 5
    result = factorial(num)
    print(f"Factorial of {num}! = {result}")
