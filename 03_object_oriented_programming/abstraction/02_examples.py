"""
Topic: Plugin Architecture Contract with ABC
File: 02_examples.py
"""
from abc import ABC, abstractmethod

class BasePlugin(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def execute(self, payload: dict) -> dict:
        pass


class AnalyticsPlugin(BasePlugin):
    @property
    def name(self) -> str:
        return "Analytics Engine v1"

    def execute(self, payload: dict) -> dict:
        payload["analytics_processed"] = True
        return payload


if __name__ == "__main__":
    plugin = AnalyticsPlugin()
    print(f"Plugin Name: {plugin.name}")
    print(f"Execution:   {plugin.execute({'user_id': 42})}")
