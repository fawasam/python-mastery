"""
Topic: Comprehensions (List, Set, Dict) Basics
File: 01_basic.py
"""

def demonstrate_comprehensions() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 1. List Comprehension
    squared_evens = [x**2 for x in numbers if x % 2 == 0]
    print(f"Squared Evens: {squared_evens}")

    # 2. Dict Comprehension
    word_lengths = {word: len(word) for word in ["python", "data", "comprehension"]}
    print(f"Word Lengths Dict: {word_lengths}")

    # 3. Set Comprehension
    names = ["Alice", "BOB", "alice", "Charlie", "bob"]
    clean_unique_names = {name.title() for name in names}
    print(f"Clean Unique Names Set: {clean_unique_names}")


if __name__ == "__main__":
    demonstrate_comprehensions()
