"""
Topic: Protocol vs ABC Comparison
File: 02_examples.py
"""
from typing import Protocol

class Dumper(Protocol):
    def dump() -> str:
        ...

# Protocols do not force tight inheritance coupling
class JSONDumper:
    def dump(self) -> str:
        return "{}"


if __name__ == "__main__":
    dumper = JSONDumper()
    print(f"Dumped: {dumper.dump()}")
