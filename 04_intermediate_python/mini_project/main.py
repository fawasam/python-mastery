"""
Extensible Data Validation & Plugin Processing Engine.
"""

from abc import ABC, abstractmethod
import functools
import time
from typing import Any, Callable, Protocol, TypeVar


# 1. DESCRIPTORS FOR DECLARATIVE FIELD VALIDATION
class ValidatedField:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: type | None = None) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)


class StringField(ValidatedField):
    def __init__(self, min_length: int = 1) -> None:
        self.min_length = min_length

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Expected string, got {type(value).__name__}")
        if len(value) < self.min_length:
            raise ValueError(f"String must be at least {self.min_length} chars long")
        setattr(instance, self.storage_name, value)


class IntegerField(ValidatedField):
    def __init__(self, min_val: int = 0) -> None:
        self.min_val = min_val

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected integer, got {type(value).__name__}")
        if value < self.min_val:
            raise ValueError(f"Integer must be >= {self.min_val}")
        setattr(instance, self.storage_name, value)


# 2. DATA MODEL USING DESCRIPTORS
class UserRecord:
    username = StringField(min_length=3)
    age = IntegerField(min_val=18)

    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age

    def __repr__(self) -> str:
        return f"<UserRecord username='{self.username}', age={self.age}>"


# 3. PROTOCOL & ABC FOR PROCESSOR PLUGINS
class ProcessorPlugin(Protocol):
    """Structural protocol for pipeline processing plugins."""

    def process(self, record: UserRecord) -> UserRecord:
        ...


class BaseProcessor(ABC):
    """Nominal Abstract Base Class for processor plugins."""

    @abstractmethod
    def process(self, record: UserRecord) -> UserRecord:
        pass


# 4. DECORATOR REGISTRY FOR PLUGINS
F = TypeVar("F", bound=Callable[..., Any])
PLUGIN_REGISTRY: list[ProcessorPlugin] = []


def register_plugin(cls: type) -> type:
    """Class decorator registering plugin classes in the global registry."""
    instance = cls()
    PLUGIN_REGISTRY.append(instance)
    print(f"[REGISTRY] Registered plugin: {cls.__name__}")
    return cls


def measure_execution_time(func: F) -> F:
    """Decorator tracking step timing."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        print(f"[METRIC] Step '{func.__name__}' completed in {duration:.3f}ms")
        return result

    return wrapper  # type: ignore[return-value]


# 5. PLUGIN IMPLEMENTATIONS
@register_plugin
class SanitizerPlugin(BaseProcessor):
    def process(self, record: UserRecord) -> UserRecord:
        record.username = record.username.strip().lower()
        return record


# 6. CLOSURE FOR PIPELINE FACTORY
def make_pipeline_runner(plugins: list[ProcessorPlugin]) -> Callable[[UserRecord], UserRecord]:
    """Returns a stateful closure processing a record through all registered plugins."""

    @measure_execution_time
    def run_pipeline(record: UserRecord) -> UserRecord:
        print(f"\n--- Running Pipeline for {record} ---")
        current_record = record
        for plugin in plugins:
            current_record = plugin.process(current_record)
        return current_record

    return run_pipeline


if __name__ == "__main__":
    # Create record with descriptor validation
    user = UserRecord("  ALICE_SMITH  ", 28)
    print(f"Initial record: {user}")

    # Build and execute pipeline closure
    pipeline = make_pipeline_runner(PLUGIN_REGISTRY)
    processed_user = pipeline(user)

    print(f"Final processed record: {processed_user}")
