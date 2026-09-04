"""
Topic: Common Mistakes with JSON
File: 03_common_mistakes.py
"""

def mistake_1_type_error_unserializable() -> None:
    from datetime import datetime
    data = {"created_at": datetime.now()}

    # ❌ WRONG: json.dumps(data) -> TypeError: Object of type datetime is not JSON serializable!

    # ✅ CORRECT: Pass custom encoder OR convert datetime to ISO string prior to serialization.
    data["created_at"] = data["created_at"].isoformat()
    import json
    print(f"Manually converted ISO string JSON: {json.dumps(data)}")


if __name__ == "__main__":
    mistake_1_type_error_unserializable()
