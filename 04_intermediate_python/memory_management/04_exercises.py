"""
Memory Management Exercises.
"""

from typing import Any
import weakref


# Exercise 1 (Medium): Weak Ref Parent Link
# Implement a TreeNode class where child nodes use weakref to reference their parent node,
# preventing strong circular references between parents and children.
class TreeNode:
    def __init__(self, value: str, parent: "TreeNode | None" = None) -> None:
        self.value = value
        self._parent_ref: weakref.ref[TreeNode] | None = None
        self.children: list[TreeNode] = []

        if parent is not None:
            self.set_parent(parent)

    def set_parent(self, parent: "TreeNode") -> None:
        raise NotImplementedError("Implement set_parent using weakref.ref")

    def get_parent(self) -> "TreeNode | None":
        raise NotImplementedError("Implement get_parent returning dereferenced weakref")
