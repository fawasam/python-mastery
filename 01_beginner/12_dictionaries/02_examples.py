"""
Topic: Nested Dictionary Parsing (API Payload Pattern)
File: 02_examples.py
"""

def parse_nested_api_response() -> None:
    api_response = {
        "status": 200,
        "data": {
            "user": {
                "id": "usr_9981",
                "profile": {
                    "first_name": "Elena",
                    "last_name": "Rostova",
                },
                "subscriptions": [
                    {"plan": "pro_annual", "active": True},
                    {"plan": "ai_addon", "active": False},
                ],
            }
        },
    }

    # Safe deep extraction using .get() chaining
    user_data = api_response.get("data", {}).get("user", {})
    profile = user_data.get("profile", {})

    first_name = profile.get("first_name", "")
    last_name = profile.get("last_name", "")
    full_name = f"{first_name} {last_name}".strip()

    subscriptions = user_data.get("subscriptions", [])
    active_plans = [s["plan"] for s in subscriptions if s.get("active")]

    print(f"Full Name:    {full_name}")
    print(f"Active Plans: {active_plans}")


if __name__ == "__main__":
    parse_nested_api_response()
