"""
Topic: Set Solutions
File: 05_solution.py
"""

def level_1_easy() -> None:
    raw_list = [10, 20, 10, 30, 20, 40]
    num_set = set(raw_list)
    has_30 = 30 in num_set
    print(f"Set: {num_set} | Contains 30? {has_30}")


def level_2_medium() -> set[str]:
    required = {"read", "write", "execute"}
    granted = {"read", "write"}
    missing = required - granted
    print(f"Missing permissions: {missing}")
    return missing


def level_3_hard(sys_a: list[str], sys_b: list[str]) -> tuple[set[str], set[str], set[str]]:
    set_a = set(sys_a)
    set_b = set(sys_b)
    common = set_a & set_b
    unique_a = set_a - set_b
    unique_b = set_b - set_a
    print(f"Common: {common} | Unique A: {unique_a} | Unique B: {unique_b}")
    return common, unique_a, unique_b


def level_4_real_world(text: str, banned_words: set[str]) -> str:
    words = text.split()
    censored_words = ["***" if word.strip(".,!?:;").lower() in banned_words else word for word in words]
    result = " ".join(censored_words)
    print(f"Censored Text: '{result}'")
    return result


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard(["a@x.com", "b@x.com"], ["b@x.com", "c@x.com"])

    print("\n--- Level 4 ---")
    level_4_real_world("This spam contains bad text", {"spam", "bad"})
