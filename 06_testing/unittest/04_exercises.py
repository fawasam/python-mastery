"""
Unittest Exercises.
"""

import unittest


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


# Exercise 1 (Easy): Write a TestCase for is_palindrome
class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_valid(self) -> None:
        raise NotImplementedError("Implement test_palindrome_valid")

    def test_palindrome_invalid(self) -> None:
        raise NotImplementedError("Implement test_palindrome_invalid")


if __name__ == "__main__":
    unittest.main()
