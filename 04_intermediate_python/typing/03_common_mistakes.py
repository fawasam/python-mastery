"""
Topic: Common Mistakes with Typing Module
File: 03_common_mistakes.py
"""

def mistake_1_overusing_any() -> None:
    # ❌ WRONG: def process(data: Any) -> Any:
    # Overusing `Any` turns off static type checking completely for those variables!
    
    # ✅ CORRECT: Use TypeVar for generic relationships or Union/Protocol types!
    print("Avoid 'Any' whenever possible; use TypeVar or concrete Unions.")


if __name__ == "__main__":
    mistake_1_overusing_any()
