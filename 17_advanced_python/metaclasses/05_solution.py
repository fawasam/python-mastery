"""
Solutions: Metaclasses Exercises.
"""


def count_registered_subclasses(base_cls: type) -> int:
    return len(base_cls.__subclasses__())


if __name__ == "__main__":
    class Parent:
        pass

    class ChildA(Parent):
        pass

    class ChildB(Parent):
        pass

    print("Subclass count:", count_registered_subclasses(Parent))
