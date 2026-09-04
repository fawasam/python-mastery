"""
TDD Example: Building a Bounded Stack Data Structure.
"""


class StackEmptyError(Exception):
    pass


class BoundedStack:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self._items: list[int] = []

    def push(self, val: int) -> None:
        if len(self._items) >= self.capacity:
            raise OverflowError("Stack capacity reached")
        self._items.append(val)

    def pop(self) -> int:
        if not self._items:
            raise StackEmptyError("Cannot pop from empty stack")
        return self._items.pop()

    def size(self) -> int:
        return len(self._items)


def test_bounded_stack_lifecycle() -> None:
    stack = BoundedStack(capacity=2)
    assert stack.size() == 0

    stack.push(10)
    stack.push(20)
    assert stack.size() == 2

    try:
        stack.push(30)
        assert False, "Should raise OverflowError"
    except OverflowError:
        pass

    assert stack.pop() == 20
    assert stack.pop() == 10

    try:
        stack.pop()
        assert False, "Should raise StackEmptyError"
    except StackEmptyError:
        pass

    print("TDD BoundedStack lifecycle test passed successfully!")


if __name__ == "__main__":
    test_bounded_stack_lifecycle()
