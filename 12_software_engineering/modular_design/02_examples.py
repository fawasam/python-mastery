"""
Advanced Modular Design: Plugin Architecture with Dynamic Registration.
"""

from typing import Callable, TypeVar

T = TypeVar("T")


class PluginRegistry:
    """Decoupled plugin system allowing modules to register capabilities dynamically."""
    def __init__(self) -> None:
        self._plugins: dict[str, Callable[..., Any]] = {}

    def register(self, name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            self._plugins[name] = func
            return func
        return decorator

    def execute(self, name: str, *args: Any, **kwargs: Any) -> Any:
        if name not in self._plugins:
            raise KeyError(f"Plugin '{name}' not found.")
        return self._plugins[name](*args, **kwargs)


registry = PluginRegistry()


@registry.register("csv_exporter")
def export_as_csv(data: list[dict[str, Any]]) -> str:
    return "csv_row_1,csv_row_2"


@registry.register("json_exporter")
def export_as_json(data: list[dict[str, Any]]) -> str:
    return '{"data": "json_content"}'


if __name__ == "__main__":
    sample_data = [{"a": 1}]
    print("CSV Output:", registry.execute("csv_exporter", sample_data))
    print("JSON Output:", registry.execute("json_exporter", sample_data))
