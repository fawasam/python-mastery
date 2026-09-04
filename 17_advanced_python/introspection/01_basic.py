"""
Introspection Basics: Dynamic Attribute Access with getattr and hasattr.
"""


class ConfigContainer:
    def __init__(self) -> None:
        self.db_host = "localhost"
        self.db_port = 5432


def safe_get_attribute(obj: object, attr_name: str, default: Any = None) -> Any:
    """Safely inspect and retrieve attribute value from object at runtime."""
    if hasattr(obj, attr_name):
        return getattr(obj, attr_name)
    return default


if __name__ == "__main__":
    cfg = ConfigContainer()
    print("Inspected db_host:", safe_get_attribute(cfg, "db_host"))
    print("Inspected missing_param:", safe_get_attribute(cfg, "missing_param", "DEFAULT_FALLBACK"))
