"""
Topic: Common Mistakes with Protocols
File: 03_common_mistakes.py
"""
from typing import Protocol

class MistakeProtocol(Protocol):
    def run(self) -> None:
        ...

def mistake_1_using_isinstance_without_runtime_checkable() -> None:
    class Runner:
        def run(self) -> None: pass

    r = Runner()
    # ❌ WRONG: isinstance(r, MistakeProtocol) -> TypeError: Instance and class checks can only be used with @runtime_checkable protocols!
    print("Add @runtime_checkable to Protocol definition to allow isinstance() checks.")


if __name__ == "__main__":
    mistake_1_using_isinstance_without_runtime_checkable()
