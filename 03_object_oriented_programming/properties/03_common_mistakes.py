"""
Topic: Common Mistakes with Properties
File: 03_common_mistakes.py
"""

def mistake_1_infinite_recursion_in_setter() -> None:
    class InfiniteSetter:
        def __init__(self, val: int) -> None:
            self.val = val

        @property
        def val(self) -> int:
            return self._val

        @val.setter
        def val(self, new_val: int) -> None:
            # ❌ WRONG: self.val = new_val -> Calls setter recursively! RecursionError!
            # ✅ CORRECT: Modify internal backing variable self._val!
            self._val = new_val

    obj = InfiniteSetter(10)
    print(f"Correctly initialized backing variable: {obj.val}")


if __name__ == "__main__":
    mistake_1_infinite_recursion_in_setter()
