"""
Solutions: AST Exercises.
"""

import ast


def count_functions_in_code(source_code: str) -> int:
    tree = ast.parse(source_code)
    return sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))


if __name__ == "__main__":
    code = "def f1(): pass\ndef f2(): pass\nx = 10"
    print("Function count in AST:", count_functions_in_code(code))
