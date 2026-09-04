"""
Topic: Common Mistakes with Method Types
File: 03_common_mistakes.py
"""

def mistake_1_forgetting_self_or_cls_argument() -> None:
    class BadMethods:
        # ❌ WRONG: Instance method missing `self` as first parameter!
        # def do_something(): pass -> Calling obj.do_something() passes obj automatically, causing TypeError: takes 0 positional args but 1 was given!
        pass

    print("Instance methods require `self`, classmethods require `cls`.")


if __name__ == "__main__":
    mistake_1_forgetting_self_or_cls_argument()
