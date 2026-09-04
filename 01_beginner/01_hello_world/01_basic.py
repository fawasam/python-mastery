"""
Topic: Hello World & Python Syntax Fundamentals
File: 01_basic.py

This script demonstrates the absolute basic building blocks of Python:
1. Comments (used to document code intentions)
2. Printing text to the terminal standard output
3. Execution flow from top to bottom
"""

# Single-line comments start with a hash symbol (#).
# The Python interpreter completely ignores comments during execution.
# We use comments to explain the reasoning, assumptions, and design behind code.

def main() -> None:
    # print() is a built-in Python function that displays text on the screen.
    # Text inside quotes (single ' or double ") is called a string literal.
    print("Hello, World!")

    # Python executes statements sequentially, one after another.
    print("Welcome to the Python Mastery Curriculum.")
    print("This course will guide you from beginner to professional software engineer.")


# The entry point check: if this file is executed directly (not imported as a module),
# Python sets __name__ to "__main__", which triggers our main() function call.
if __name__ == "__main__":
    main()
