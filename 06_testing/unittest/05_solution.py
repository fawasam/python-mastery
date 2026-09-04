"""
Solutions for Unittest Exercises.
"""

import unittest


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_valid(self) -> None:
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_palindrome_invalid(self) -> None:
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("hello world"))


if __name__ == "__main__":
    unittest.main()
