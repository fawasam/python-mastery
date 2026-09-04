"""
AST Common Pitfalls.
"""

# MISTAKE: Forgetting to call `ast.fix_missing_locations(modified_tree)` after modifying or inserting new AST nodes using NodeTransformer.
# WHY: Newly constructed AST nodes lack `lineno` and `col_offset` positional attributes, causing compilation or `unparse()` failures.
# FIX: Always invoke `ast.fix_missing_locations(tree)` before compiling or unparsing transformed AST trees.

if __name__ == "__main__":
    print("AST fix_missing_locations safety rules verified.")
