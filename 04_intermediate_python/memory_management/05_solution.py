"""
Solution for Memory Management Exercises.
"""

import weakref


class TreeNode:
    def __init__(self, value: str, parent: "TreeNode | None" = None) -> None:
        self.value = value
        self._parent_ref: weakref.ref[TreeNode] | None = None
        self.children: list[TreeNode] = []

        if parent is not None:
            self.set_parent(parent)

    def set_parent(self, parent: "TreeNode") -> None:
        self._parent_ref = weakref.ref(parent)
        parent.children.append(self)

    def get_parent(self) -> "TreeNode | None":
        if self._parent_ref is None:
            return None
        return self._parent_ref()  # Returns dereferenced parent object or None if deallocated


if __name__ == "__main__":
    root = TreeNode("Root")
    child = TreeNode("Child", parent=root)

    print(f"Child value: {child.value}")
    print(f"Child parent value: {child.get_parent().value if child.get_parent() else 'None'}")

    del root
    # Since child holds a weak reference to root, root was freed!
    print(f"Child parent after root deleted: {child.get_parent()}")
