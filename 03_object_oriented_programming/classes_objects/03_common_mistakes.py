"""
Topic: Common Mistakes with Classes
File: 03_common_mistakes.py
"""

def mistake_1_mutable_class_attribute() -> None:
    class Student:
        # ❌ WRONG: Mutable class attribute shared across all instances!
        # items = []

        def __init__(self, name: str) -> None:
            self.name = name
            # ✅ CORRECT: Define mutable attributes inside __init__ attached to self!
            self.items: list[str] = []

    s1 = Student("Alice")
    s2 = Student("Bob")
    s1.items.append("Notebook")

    print(f"s1 items: {s1.items}")
    print(f"s2 items (independent): {s2.items}")


if __name__ == "__main__":
    mistake_1_mutable_class_attribute()
