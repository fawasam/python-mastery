"""
Topic: Hello World & Printing Basics
File: 02_examples.py

This file demonstrates realistic examples of printing formatted text,
multiline output, and controlling separator and end characters.
"""

def demonstrate_printing_variations() -> None:
    # 1. Printing multiple items separated by space by default
    print("Python", "is", "awesome!")

    # 2. Custom separator using the `sep` parameter
    # Useful when generating CSV lines or custom formatted logs.
    print("2026", "09", "04", sep="-")

    # 3. Custom ending using the `end` parameter
    # By default, print() appends a newline character (\n).
    # We can override `end` to keep printing on the same terminal line.
    print("Loading application assets...", end=" ")
    print("[DONE]")

    # 4. Multiline string output using triple quotes (""" or ''')
    banner = """
    ========================================
             SYSTEM MONITOR CLI v1.0        
    ========================================
    Status: Operational
    Engine: Python 3.12+
    ========================================
    """
    print(banner)


if __name__ == "__main__":
    demonstrate_printing_variations()
