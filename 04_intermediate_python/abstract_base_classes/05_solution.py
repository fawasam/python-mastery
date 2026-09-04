"""
Topic: ABC Solutions
File: 05_solution.py
"""
import json
from abc import ABC, abstractmethod
from typing import Any

class Serializer(ABC):
    @abstractmethod
    def serialize(self, data: dict[str, Any]) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, data: dict[str, Any]) -> str:
        return json.dumps(data)


class BaseHealthCheck(ABC):
    @property
    @abstractmethod
    def service_name(self) -> str:
        pass

    @abstractmethod
    def check_health(self) -> bool:
        pass


class DatabaseHealthCheck(BaseHealthCheck):
    @property
    def service_name(self) -> str:
        return "PostgreSQL Primary"

    def check_health(self) -> bool:
        print(f"[{self.service_name}] Pinging DB host... OK")
        return True


if __name__ == "__main__":
    print("--- Level 1 ---")
    s = JSONSerializer()
    print("Serialized:", s.serialize({"a": 1}))

    print("\n--- Level 4 ---")
    hc = DatabaseHealthCheck()
    print(f"Health check for '{hc.service_name}': {hc.check_health()}")
