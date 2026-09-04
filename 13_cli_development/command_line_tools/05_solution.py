"""
Solutions: Command Line Tools Exercises.
"""


def filter_lines_by_keyword(lines: list[str], keyword: str) -> list[str]:
    kw_lower = keyword.lower()
    return [line for line in lines if kw_lower in line.lower()]


if __name__ == "__main__":
    sample = ["ERROR: Database connection reset", "INFO: Server started", "WARNING: High memory usage"]
    matches = filter_lines_by_keyword(sample, "error")
    print("Matched lines:", matches)
