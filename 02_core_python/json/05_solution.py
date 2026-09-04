"""
Topic: JSON Solutions
File: 05_solution.py
"""
import json
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Any

def level_1_easy() -> str:
    data = {"app": "Mastery", "version": 1.0}
    json_str = json.dumps(data, indent=4)
    print(f"Indented JSON:\n{json_str}")
    return json_str


def level_2_medium(json_text: str) -> dict[str, Any] | None:
    try:
        parsed = json.loads(json_text)
        print(f"Parsed JSON: {parsed}")
        return parsed
    except json.JSONDecodeError as err:
        print(f"Failed to parse JSON: {err}")
        return None


class ExtendedJSONEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)


def level_3_hard() -> str:
    payload = {"price": Decimal("99.95"), "created_on": date(2026, 9, 4)}
    res = json.dumps(payload, cls=ExtendedJSONEncoder)
    print(f"Extended JSON serialization: {res}")
    return res


def level_4_real_world(file_path: Path, key: str, value: Any) -> None:
    data = {}
    if file_path.exists():
        try:
            with file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    data[key] = value
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Updated '{key}' in '{file_path.name}' successfully.")


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium('{"name": "Alice"}')
    level_2_medium('invalid json')

    print("\n--- Level 3 ---")
    level_3_hard()

    print("\n--- Level 4 ---")
    target = Path("test_config.json")
    level_4_real_world(target, "debug", True)
    if target.exists():
        target.unlink()
