"""
Common Mistakes in Python Mocking.
"""

from unittest.mock import MagicMock


# MISTAKE 1: Calling non-existent assert methods on MagicMock
def mistake_invalid_assert_method() -> None:
    mock_obj = MagicMock()
    mock_obj.do_something()

    # DANGER: MagicMock creates attributes dynamically on the fly!
    # Methods like assert_called_once() work, but typos like assert_called_once_with_typo()
    # will silently return a NEW MagicMock object WITHOUT failing the test!
    mock_obj.assert_called_once_with_typo()  # SILENT BUG! Never asserts anything!


if __name__ == "__main__":
    mistake_invalid_assert_method()
    print("Typo method on MagicMock passed silently because MagicMock auto-creates missing methods!")
