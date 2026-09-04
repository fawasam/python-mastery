"""
Topic: Context Manager Solutions
File: 05_solution.py
"""
import io
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator

@contextmanager
def temporary_setting(settings: dict[str, Any], key: str, temp_value: Any) -> Generator[None, None, None]:
    original_value = settings.get(key)
    settings[key] = temp_value
    try:
        yield
    finally:
        if original_value is not None:
            settings[key] = original_value
        else:
            settings.pop(key, None)


class DatabaseTransactionManager:
    def __enter__(self) -> "DatabaseTransactionManager":
        print("  [DB] BEGIN TRANSACTION")
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool | None:
        if exc_type is not None:
            print(f"  [DB] ❌ ROLLBACK TRANSACTION due to {exc_val}")
            return False  # Do not suppress exception
        print("  [DB] ✅ COMMIT TRANSACTION")
        return None


@contextmanager
def redirect_stdout_to_string() -> Generator[io.StringIO, None, None]:
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout


@contextmanager
def atomic_write(file_path: Path) -> Generator[io.TextIOWrapper, None, None]:
    temp_path = file_path.with_suffix(file_path.suffix + ".tmp")
    f = temp_path.open("w", encoding="utf-8")
    try:
        yield f
    except Exception as e:
        f.close()
        if temp_path.exists():
            temp_path.unlink()
        raise e
    else:
        f.close()
        temp_path.replace(file_path)


if __name__ == "__main__":
    print("--- Level 1 ---")
    config = {"theme": "light"}
    with temporary_setting(config, "theme", "dark"):
        print("Inside block config:", config)
    print("Outside block config:", config)

    print("\n--- Level 2 ---")
    with DatabaseTransactionManager():
        print("Executing SQL mutations...")

    print("\n--- Level 3 ---")
    with redirect_stdout_to_string() as buf:
        print("Captured stdout line 1")
        print("Captured stdout line 2")
    captured = buf.getvalue()
    print(f"Captured Buffer:\n{captured}")

    print("--- Level 4 ---")
    target_path = Path("atomic_test.txt")
    with atomic_write(target_path) as f:
        f.write("Atomic file content\n")
    if target_path.exists():
        print(f"Atomic file verified: {target_path.read_text().strip()}")
        target_path.unlink()
