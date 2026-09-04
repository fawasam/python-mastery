"""
Common Mistakes When Working with Python Descriptors.
"""


# MISTAKE 1: Storing state on the descriptor object itself
class BadDescriptor:
    def __init__(self) -> None:
        # DANGER: 'self.value' is shared across all instances of classes using this descriptor!
        self.value = None

    def __get__(self, instance, owner=None):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class PersonBad:
    age = BadDescriptor()


# CORRECT APPROACH: Store state on the target instance
class GoodDescriptor:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: object | None, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance: object, value: object) -> None:
        setattr(instance, self.storage_name, value)


class PersonGood:
    age = GoodDescriptor()


if __name__ == "__main__":
    print("--- Demonstration of Mistake 1: Shared Descriptor State ---")
    p1 = PersonBad()
    p2 = PersonBad()

    p1.age = 25
    print(f"p1 age set to 25 -> p1.age = {p1.age}")
    p2.age = 40
    print(f"p2 age set to 40 -> p2.age = {p2.age}")
    print(f"BUG! p1.age accidentally changed to: {p1.age}")

    print("\n--- Correct Behavior with GoodDescriptor ---")
    g1 = PersonGood()
    g2 = PersonGood()

    g1.age = 25
    g2.age = 40
    print(f"g1.age = {g1.age} (Expected 25)")
    print(f"g2.age = {g2.age} (Expected 40)")
