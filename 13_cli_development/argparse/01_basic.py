"""
Argparse Basics: Defining Positional and Optional CLI Arguments.
"""

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Construct argument parser for a file grepper CLI."""
    parser = argparse.ArgumentParser(
        description="Search for keywords inside text files."
    )
    
    # Positional argument (required)
    parser.add_argument("keyword", type=str, help="Search keyword")
    parser.add_argument("file_path", type=str, help="Target file path")
    
    # Optional flags
    parser.add_argument(
        "-i", "--ignore-case", action="store_true", help="Perform case-insensitive search"
    )
    parser.add_argument(
        "-n", "--line-number", action="store_true", help="Print line numbers with matches"
    )
    
    return parser


if __name__ == "__main__":
    # Test parser programmatically with test args
    parser = build_parser()
    args = parser.parse_args(["error", "server.log", "--ignore-case", "-n"])
    
    print("Parsed CLI Arguments:")
    print(f"Keyword: {args.keyword}")
    print(f"File Path: {args.file_path}")
    print(f"Ignore Case: {args.ignore_case}")
    print(f"Line Numbers: {args.line_number}")
