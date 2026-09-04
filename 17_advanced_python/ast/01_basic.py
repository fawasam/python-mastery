"""
AST Basics: Building a Static Code Analysis Linter with ast.NodeVisitor.
"""

import ast


class FunctionNameLinter(ast.NodeVisitor):
    """AST NodeVisitor checking if all function definitions follow snake_case naming."""
    def __init__(self) -> None:
        self.violations: list[str] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        if any(c.isupper() for c in node.name):
            self.violations.append(f"Line {node.lineno}: Function '{node.name}' should be snake_case!")
        self.generic_visit(node)


def analyze_source_code(source: str) -> list[str]:
    tree = ast.parse(source)
    linter = FunctionNameLinter()
    linter.visit(tree)
    return linter.violations


if __name__ == "__main__":
    code = """
def valid_function_name():
    pass

def InvalidCamelCaseFunction():
    pass
"""
    violations = analyze_source_code(code)
    print("Static AST Linter Violations:")
    for v in violations:
        print(" -", v)
