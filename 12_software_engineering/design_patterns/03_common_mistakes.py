"""
Design Patterns Anti-Patterns and Over-Engineering.
"""


class OverEngineeredSingleton:
    """
    MISTAKE: Over-using Singleton pattern for stateful global data in Python.
    WHY: In Python, simple module-level singletons or dependency injection are cleaner.
    Singletons introduce hidden global state and make unit testing difficult.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# Better Pythonic approach: Simple module-level state or dependency injection instead of complex singletons.


if __name__ == "__main__":
    s1 = OverEngineeredSingleton()
    s2 = OverEngineeredSingleton()
    print("Are instances identical?", s1 is s2)
