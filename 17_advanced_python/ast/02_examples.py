"""
Advanced AST: Code Rewriting using ast.NodeTransformer and ast.unparse.
"""

import ast


class IntegerDoublerTransformer(ast.NodeTransformer):
    """AST Transformer that multiplies every integer literal in the source code by 2."""
    def visit_Constant(self, node: ast.Constant) -> ast.AST:
        if isinstance(node.value, int) and not isinstance(node.value, bool):
            return ast.Constant(value=node.value * 2)
        return node


def double_integer_literals(source_code: str) -> str:
    tree = ast.parse(source_code)
    transformer = IntegerDoublerTransformer()
    modified_tree = transformer.visit(tree)
    ast.fix_missing_locations(modified_tree)
    return ast.unparse(modified_tree)


if __name__ == "__main__":
    code = "val = 10 + 5"
    modified = double_integer_literals(code)
    print(f"Original Code: '{code}'")
    print(f"AST Transformed Code: '{modified}'")
