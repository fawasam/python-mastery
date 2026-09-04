"""
Challenge 01: Palindrome Check

Difficulty: ⭐
Topics: Strings, Two Pointers

Problem:
Given a string s, return True if it is a palindrome (reads the same forward and backward), ignoring case and non-alphanumeric characters.

Input: "A man, a plan, a canal: Panama"
Expected Output: True

Constraints:
- 1 <= len(s) <= 2 * 10^5

Hints:
- Filter alphanumeric characters using char.isalnum()
- Convert to lower case before comparing
"""


def is_palindrome(s: str) -> bool:
    """Implement your solution below."""
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_str = "A man, a plan, a canal: Panama"
    print(f"Is '{test_str}' a palindrome? {is_palindrome(test_str)}")
