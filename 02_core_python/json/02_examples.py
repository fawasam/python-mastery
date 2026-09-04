"""
Topic: Custom JSON Encoder for Non-Standard Objects
File: 02_examples.py
"""
import json
from datetime import datetime, timezone
from typing import Any

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder handling datetime, set, and tuple objects."""
    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)


if __name__ == "__main__":
    event = {
        "event_id": "evt_404",
        "timestamp": datetime.now(timezone.utc),
        "tags": {"security", "audit"},
    }

    serialized = json.dumps(event, cls=CustomJSONEncoder, indent=2)
    print(f"Custom Encoders Serialized Output:\n{serialized}")
