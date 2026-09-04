"""
Topic: Common Mistakes with Abstraction
File: 03_common_mistakes.py
"""
from abc import ABC, abstractmethod

def mistake_1_instantiating_abstract_class() -> None:
    class AbstractShape(ABC):
        @abstractmethod
        def area(self) -> float:
            pass

    # ❌ WRONG: s = AbstractShape()
    # TypeError: Can't instantiate abstract class AbstractShape with abstract method area

    # ✅ CORRECT: Instantiate concrete subclasses that implement ALL abstract methods!
    print("Cannot instantiate abstract class directly. Concrete subclasses must implement all @abstractmethods.")


if __name__ == "__main__":
    mistake_1_instantiating_abstract_class()
