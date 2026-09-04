"""
Solutions: Introspection Exercises.
"""

from typing import Any


def list_public_methods(obj: Any) -> list[str]:
    return [attr for attr in dir(obj) if not attr.startswith("_") and callable(getattr(obj, attr))]


if __name__ == "__main__":
    class Dummy:
        def foo(self) -> None: pass
        def bar(self) -> None: pass
        _secret = 42

    print("Public methods:", list_public_methods(Dummy()))
