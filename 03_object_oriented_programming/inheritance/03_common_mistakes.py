"""
Topic: Common Mistakes with Inheritance
File: 03_common_mistakes.py
"""

def mistake_1_forgetting_super_init() -> None:
    class Parent:
        def __init__(self, name: str) -> None:
            self.name = name

    class ChildBuggy(Parent):
        def __init__(self, name: str, age: int) -> None:
            # ❌ WRONG: Forgetting super().__init__(name)!
            # self.name is never initialized on Parent instance attribute!
            self.age = age

    c = ChildBuggy("Alice", 10)
    print(f"Child age: {c.age} | Has 'name'? {hasattr(c, 'name')}")


if __name__ == "__main__":
    mistake_1_forgetting_super_init()
