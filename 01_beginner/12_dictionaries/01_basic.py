"""
Topic: Dictionary Basics & Methods
File: 01_basic.py
"""

def demonstrate_dictionary_basics() -> None:
    # 1. Initialization
    user_profile: dict[str, str | int | list[str]] = {
        "user_id": 4021,
        "username": "coder_alex",
        "email": "alex@dev.io",
        "skills": ["Python", "Docker", "SQL"],
    }

    # 2. Accessing & Updating
    print(f"Username: {user_profile['username']}")
    
    # Safe lookup with default value
    phone = user_profile.get("phone", "NOT_PROVIDED")
    print(f"Phone (optional field): {phone}")

    # Adding & updating entries
    user_profile["status"] = "ACTIVE"
    user_profile["email"] = "alex.new@dev.io"

    # 3. Iterating over items
    print("\n--- User Profile Entries ---")
    for key, value in user_profile.items():
        print(f"  {key:<12}: {value}")


if __name__ == "__main__":
    demonstrate_dictionary_basics()
