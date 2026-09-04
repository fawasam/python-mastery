"""
Solutions: AI Projects Exercises.
"""


def calculate_token_cost(input_tokens: int, output_tokens: int) -> float:
    return (input_tokens / 1000.0) * 0.001 + (output_tokens / 1000.0) * 0.003


if __name__ == "__main__":
    cost = calculate_token_cost(5000, 2000)
    print(f"Calculated AI Token Cost: ${cost:.4f}")
