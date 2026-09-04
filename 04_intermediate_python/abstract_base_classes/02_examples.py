"""
Topic: Abstract Properties with @property @abstractmethod
File: 02_examples.py
"""
from abc import ABC, abstractmethod

class BaseConfig(ABC):
    @property
    @abstractmethod
    def environment(self) -> str:
        pass


class ProdConfig(BaseConfig):
    @property
    def environment(self) -> str:
        return "PRODUCTION"


if __name__ == "__main__":
    cfg = ProdConfig()
    print(f"Environment: {cfg.environment}")
