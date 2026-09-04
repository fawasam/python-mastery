"""
Solutions: LLM API Exercises.
"""


def format_prompt_template(system_prompt: str, user_question: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_question}
    ]


if __name__ == "__main__":
    msgs = format_prompt_template("You are a helpful bot.", "What is Python?")
    print("Formatted prompt messages:", msgs)
