"""
Topic: Recursive Tree Directory Walker Example
File: 02_examples.py
"""
from typing import Any

nested_category_tree = {
    "Electronics": {
        "Computers": {"Laptops": {}, "Desktops": {}},
        "Audio": {"Headphones": {}},
    },
    "Apparel": {"Men": {}, "Women": {}},
}

def print_tree(tree: dict[str, Any], depth: int = 0) -> None:
    for key, value in tree.items():
        indent = "  " * depth
        print(f"{indent}- {key}")
        if isinstance(value, dict) and value:
            print_tree(value, depth + 1)


if __name__ == "__main__":
    print("Traversing nested tree recursively:")
    print_tree(nested_category_tree)
