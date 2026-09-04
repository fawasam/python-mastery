"""
Common Mistakes in Standard Unittest.
"""

import unittest


# MISTAKE 1: Forgetting test_ prefix on test methods
class BadTestClass(unittest.TestCase):
    def check_addition(self) -> None:  # DANGER: Ignored by test runner because no test_ prefix!
        self.assertEqual(1 + 1, 3)

    def test_correct_addition(self) -> None:
        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
