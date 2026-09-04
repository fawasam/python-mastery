"""
Topic: Custom Class Context Manager Basics
File: 01_basic.py
"""
from types import TracebackType
from typing import Self

class ManagedFile:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file_handle = None

    def __enter__(self) -> Self:
        print(f"  [__enter__] Opening file: {self.filename}")
        self.file_handle = open(self.filename, self.mode, encoding="utf-8")
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None:
        print(f"  [__exit__] Closing file: {self.filename}")
        if self.file_handle:
            self.file_handle.close()
        return False  # Do not suppress exceptions


if __name__ == "__main__":
    from pathlib import Path
    test_path = Path("temp_cm_test.txt")
    
    with ManagedFile(str(test_path), "w") as f:
        print("  Inside with block writing data...")

    if test_path.exists():
        test_path.unlink()
