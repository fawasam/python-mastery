"""
Topic: JSON Serialization & Deserialization
File: 01_basic.py
"""
import json

def demonstrate_json_basics() -> None:
    # Python dictionary structure
    user_payload = {
        "user_id": 9901,
        "username": "sarah_dev",
        "roles": ["admin", "editor"],
        "is_active": True,
        "balance": None,
    }

    # 1. Serialize Python dict to JSON String (dumps)
    json_str = json.dumps(user_payload, indent=2, sort_keys=True)
    print(f"Serialized JSON String:\n{json_str}")

    # 2. Deserialize JSON String to Python dict (loads)
    reconstructed = json.loads(json_str)
    print(f"\nReconstructed Dict Type: {type(reconstructed).__name__}")
    print(f"Username from dict:     {reconstructed['username']}")


if __name__ == "__main__":
    demonstrate_json_basics()
