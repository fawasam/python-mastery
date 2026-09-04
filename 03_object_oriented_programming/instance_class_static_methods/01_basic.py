"""
Topic: Three Method Types Comparison
File: 01_basic.py
"""

class MathHelper:
    base_unit = "meter"

    def __init__(self, value: float) -> None:
        self.value = value

    # 1. Instance method (operates on self)
    def to_centimeters(self) -> float:
        return self.value * 100.0

    # 2. Class method (operates on cls)
    @classmethod
    def get_base_unit(cls) -> str:
        return f"Base unit is {cls.base_unit}"

    # 3. Static method (pure utility)
    @staticmethod
    def is_positive(num: float) -> bool:
        return num > 0


if __name__ == "__main__":
    m = MathHelper(5.0)

    print(f"Instance method: {m.to_centimeters()} cm")
    print(f"Class method:    {MathHelper.get_base_unit()}")
    print(f"Static method:   is 5 positive? {MathHelper.is_positive(5.0)}")
