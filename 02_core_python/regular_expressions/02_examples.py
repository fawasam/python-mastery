"""
Topic: Named Capturing Groups
File: 02_examples.py
"""
import re

def parse_log_line(log_line: str) -> dict[str, str] | None:
    pattern = r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+\[(?P<level>\w+)\]\s+(?P<message>.+)$"
    match = re.match(pattern, log_line)
    if match:
        return match.groupdict()
    return None


if __name__ == "__main__":
    sample_log = "2026-09-04 14:30:00 [ERROR] Connection timeout to database host"
    parsed = parse_log_line(sample_log)
    print("Parsed Log Group Dict:")
    if parsed:
        for k, v in parsed.items():
            print(f"  {k:<10}: {v}")
