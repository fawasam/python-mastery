"""
Solutions: Argparse Exercises.
"""

import argparse


def create_calculator_parser() -> argparse.ArgumentParser:
    """
    Constructs CLI parser for a simple math calculator.
    """
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")
    parser.add_argument("num1", type=float, help="First operand")
    parser.add_argument("num2", type=float, help="Second operand")
    parser.add_argument(
        "-o", "--operation", type=str, default="add", choices=["add", "sub", "mul", "div"],
        help="Math operation to execute"
    )
    return parser


if __name__ == "__main__":
    parser = create_calculator_parser()
    args = parser.parse_args(["10.5", "4.5", "-o", "mul"])
    print(f"Parsed operands: {args.num1}, {args.num2}, Operation: {args.operation}")
