"""
Command Line Tools Basics: Exit Codes and Stderr vs Stdout Separation.
"""

import sys


def process_input_stream(lines: list[str]) -> int:
    """
    Process lines from stream, writing results to stdout and logs to stderr.
    
    Returns exit code (0 for success, 1 for error).
    """
    if not lines:
        sys.stderr.write("Error: No input lines provided to process.\n")
        return 1

    processed_count = 0
    for line in lines:
        cleaned = line.strip().upper()
        if cleaned:
            sys.stdout.write(f"PROCESSED: {cleaned}\n")
            processed_count += 1

    sys.stderr.write(f"Successfully processed {processed_count} lines.\n")
    return 0


if __name__ == "__main__":
    test_lines = ["hello world", "  python cli tool  "]
    exit_code = process_input_stream(test_lines)
    print(f"Executed with Exit Code: {exit_code}")
