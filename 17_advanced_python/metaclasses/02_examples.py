"""
Advanced Metaclasses: Modern __init_subclass__ Registry.
"""


class PluginBase:
    """Base plugin class auto-registering all subclasses using Python 3.6+ __init_subclass__."""
    _registry: dict[str, type["PluginBase"]] = {}

    def __init_subclass__(cls, plugin_name: str, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        cls._registry[plugin_name] = cls


class AudioPlugin(PluginBase, plugin_name="audio"):
    pass


class VideoPlugin(PluginBase, plugin_name="video"):
    pass


if __name__ == "__main__":
    print("Auto-registered Plugins via __init_subclass__:")
    for name, plugin_cls in PluginBase._registry.items():
        print(f"Plugin '{name}': {plugin_cls.__name__}")
