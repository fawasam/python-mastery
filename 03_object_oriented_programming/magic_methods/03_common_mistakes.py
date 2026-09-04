"""
Topic: Common Mistakes with Magic Methods
File: 03_common_mistakes.py
"""

def mistake_1_forgetting_to_implement_repr() -> None:
    # ❌ WRONG: Implementing __str__ without __repr__.
    # When items are inside a list `[obj1, obj2]`, Python calls __repr__! Without __repr__, you get `<__main__.Obj object at 0x...>`!

    # ✅ CORRECT: Always implement __repr__ first. If __str__ is missing, Python falls back to __repr__ automatically!
    print("Best Practice: Implement __repr__ first; __str__ falls back to __repr__ cleanly.")


if __name__ == "__main__":
    mistake_1_forgetting_to_implement_repr()
