"""
Topic: Regex Solutions
File: 05_solution.py
"""
import re

def level_1_easy(text: str) -> list[str]:
    phones = re.findall(r"\b\d{3}-\d{3}-\d{4}\b", text)
    print(f"Extracted phones: {phones}")
    return phones


def level_2_medium(password: str) -> bool:
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    is_valid = bool(re.match(pattern, password))
    print(f"Password '{password}' valid? {is_valid}")
    return is_valid


def level_3_hard(md_text: str) -> str:
    html_text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", md_text)
    print(f"MD: '{md_text}' -> HTML: '{html_text}'")
    return html_text


def level_4_real_world(url: str) -> dict[str, str]:
    matches = re.findall(r"[?&](?P<key>[\w-]+)=(?P<value>[\w-]+)", url)
    result = dict(matches)
    print(f"Extracted URL query params: {result}")
    return result


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy("Call 555-123-4567 or emergency 800-555-9999 today.")

    print("\n--- Level 2 ---")
    level_2_medium("StrongP@ss1")
    level_2_medium("weak")

    print("\n--- Level 3 ---")
    level_3_hard("This is **bold** text and **important**.")

    print("\n--- Level 4 ---")
    level_4_real_world("https://api.dev.io/search?category=books&page=2&sort=asc")
