"""
Defensive Programming Example: Validating External Payload Boundaries.
"""

from typing import Any


def parse_and_validate_payload(raw_payload: Any) -> dict[str, Any]:
    """
    Defensively validates external JSON/Dict payloads against unexpected types or missing keys.
    """
    if not isinstance(raw_payload, dict):
        raise TypeError(f"Payload must be a dictionary, got {type(raw_payload).__name__}")

    # Guard clause: check required keys
    required_keys = {"event_id", "timestamp", "data"}
    missing_keys = required_keys - raw_payload.keys()
    if missing_keys:
        raise ValueError(f"Payload is missing required keys: {missing_keys}")

    data_block = raw_payload["data"]
    if not isinstance(data_block, dict):
        raise TypeError("Payload 'data' field must be a nested dictionary")

    return {
        "event_id": str(raw_payload["event_id"]),
        "timestamp": int(raw_payload["timestamp"]),
        "data": data_block.copy(),
    }


if __name__ == "__main__":
    valid_data = {"event_id": "EVT-101", "timestamp": 1700000000, "data": {"status": "SUCCESS"}}
    validated = parse_and_validate_payload(valid_data)
    print(f"Validated Payload: {validated}")
