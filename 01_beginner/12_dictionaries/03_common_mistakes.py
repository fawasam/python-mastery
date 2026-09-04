"""
Topic: Common Mistakes with Dictionaries
File: 03_common_mistakes.py
"""

def mistake_1_direct_access_missing_key() -> None:
    config = {"theme": "dark", "version": "1.2.0"}

    # ❌ WRONG: port = config["port"] -> KeyError: 'port'
    # Direct bracket access crashes if the key does not exist!

    # ✅ CORRECT: Use .get() with default value OR check `if key in config`
    port = config.get("port", 8080)
    print(f"Safe port value: {port}")


def mistake_2_mutable_dictionary_keys() -> None:
    # ❌ WRONG: bad_dict = {[1, 2]: "value"}
    # TypeError: unhashable type: 'list'

    # ✅ CORRECT: Use tuple for compound key
    good_dict = {(1, 2): "value"}
    print(f"Valid tuple key dict: {good_dict}")


if __name__ == "__main__":
    mistake_1_direct_access_missing_key()
    mistake_2_mutable_dictionary_keys()
