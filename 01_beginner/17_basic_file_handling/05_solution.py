"""
Topic: File Handling Solutions
File: 05_solution.py
"""
import json
from pathlib import Path

def level_1_easy() -> None:
    temp_file = Path("notes.txt")
    with temp_file.open("w", encoding="utf-8") as f:
        f.write("Python Mastery Course\n")

    with temp_file.open("r", encoding="utf-8") as f:
        content = f.read().strip()
    print(f"Read content: '{content}'")

    if temp_file.exists():
        temp_file.unlink()


def level_2_medium(path: Path) -> int:
    if not path.exists():
        return 0
    line_count = 0
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                line_count += 1
    print(f"File '{path.name}' non-empty lines: {line_count}")
    return line_count


def level_3_hard(log_file: Path, output_errors_file: Path) -> int:
    error_count = 0
    if not log_file.exists():
        return 0

    with log_file.open("r", encoding="utf-8") as fin, output_errors_file.open("w", encoding="utf-8") as fout:
        for line in fin:
            if "ERROR" in line:
                fout.write(line)
                error_count += 1

    print(f"Extracted {error_count} ERROR lines to '{output_errors_file.name}'")
    return error_count


def level_4_real_world(log_path: Path, entry: dict) -> None:
    formatted_entry = json.dumps(entry) + "\n"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(formatted_entry)
    print(f"Appended JSON log entry to '{log_path.name}'")


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    script_path = Path(__file__)
    level_2_medium(script_path)

    print("\n--- Level 4 ---")
    test_json_file = Path("audit_log.json")
    level_4_real_world(test_json_file, {"event": "USER_LOGIN", "user_id": 9901})
    if test_json_file.exists():
        test_json_file.unlink()
