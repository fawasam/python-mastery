"""
Topic: Common Mistakes with Dataclasses
File: 03_common_mistakes.py
"""

def mistake_1_mutable_default_in_dataclass() -> None:
    # ❌ WRONG: items: list[str] = []
    # ValueError: mutable default <class 'list'> for field items is not allowed: use default_factory

    # ✅ CORRECT: Use field(default_factory=list)
    print("Always use field(default_factory=list) or field(default_factory=dict) for mutable defaults.")


if __name__ == "__main__":
    mistake_1_mutable_default_in_dataclass()
