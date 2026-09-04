"""
Topic: Common Mistakes with ABCs
File: 03_common_mistakes.py
"""

def mistake_1_forgetting_to_inherit_abc() -> None:
    from abc import abstractmethod
    # ❌ WRONG: Class defines @abstractmethod without inheriting from ABC!
    # class BadABC: @abstractmethod def foo(self): pass
    # Instantiating BadABC() succeeds without error because ABC metaclass is missing!

    # ✅ CORRECT: Class MUST inherit from ABC (or use metaclass=ABCMeta)
    print("Always inherit from abc.ABC when defining abstract methods.")


if __name__ == "__main__":
    mistake_1_forgetting_to_inherit_abc()
