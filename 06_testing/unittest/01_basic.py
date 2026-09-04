"""
Basic unittest.TestCase Example.
"""

import unittest


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestCalculatorFunctions(unittest.TestCase):
    def test_multiply_valid(self) -> None:
        self.assertEqual(multiply(3.0, 4.0), 12.0)
        self.assertAlmostEqual(multiply(0.1, 0.2), 0.02, places=4)

    def test_divide_valid(self) -> None:
        self.assertEqual(divide(10.0, 2.0), 5.0)

    def test_divide_by_zero_raises_error(self) -> None:
        # assertRaises verifies that a specific exception is raised
        with self.assertRaises(ValueError):
            divide(10.0, 0.0)


if __name__ == "__main__":
    unittest.main()
