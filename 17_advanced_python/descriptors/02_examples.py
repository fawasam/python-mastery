"""
Advanced Descriptors: Lazy Property Evaluation Descriptor.
"""

from typing import Any, Callable, TypeVar

T = TypeVar("T")


class lazy_property:
    """Descriptor that computes property value once on first access, then caches it on the instance."""
    def __init__(self, func: Callable[[Any], T]) -> None:
        self.func = func
        self.name = func.__name__

    def __get__(self, instance: Any, owner: type) -> T:
        if instance is None:
            return self  # type: ignore
        val = self.func(instance)
        # Store value directly in instance __dict__ to bypass descriptor on subsequent accesses!
        instance.__dict__[self.name] = val
        return val


class AnalyticsProcessor:
    def __init__(self, dataset: list[int]) -> None:
        self.dataset = dataset

    @lazy_property
    def total_sum(self) -> int:
        print("[Computing expensive sum...]")
        return sum(self.dataset)


if __name__ == "__main__":
    proc = AnalyticsProcessor(list(range(1000)))
    print("First Access:", proc.total_sum)
    print("Second Access (Cached):", proc.total_sum)
