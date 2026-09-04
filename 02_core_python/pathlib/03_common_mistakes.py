"""
Topic: Common Mistakes with Pathlib
File: 03_common_mistakes.py
"""

def mistake_1_string_concatenation_paths() -> None:
    # ❌ WRONG: path = "logs/" + "2026/" + "app.log" (Fails on Windows due to slash direction)

    # ✅ CORRECT: Use Path objects with / operator
    from pathlib import Path
    path = Path("logs") / "2026" / "app.log"
    print(f"Cross-platform Path: {path}")


if __name__ == "__main__":
    mistake_1_string_string_concatenation_paths() if False else mistake_1_string_concatenation_paths()
