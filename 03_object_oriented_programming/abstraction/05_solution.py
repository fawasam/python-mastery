"""
Topic: Abstraction Solutions
File: 05_solution.py
"""
from abc import ABC, abstractmethod
from typing import Any

class Animal(ABC):
    @abstractmethod
    def sound(self) -> str:
        pass


class Dog(Animal):
    def sound(self) -> str:
        return "Woof"


class Cat(Animal):
    def sound(self) -> str:
        return "Meow"


class BaseDataPipeline(ABC):
    @abstractmethod
    def extract(self) -> list[Any]:
        pass

    @abstractmethod
    def transform(self, raw_data: list[Any]) -> list[Any]:
        pass

    @abstractmethod
    def load(self, clean_data: list[Any]) -> None:
        pass

    def run(self) -> None:
        """Template method orchestrating ETL steps sequentially."""
        print("🚀 Starting ETL Pipeline...")
        raw = self.extract()
        clean = self.transform(raw)
        self.load(clean)
        print("✅ Pipeline execution complete.")


class UserETLPipeline(BaseDataPipeline):
    def extract(self) -> list[Any]:
        return ["  alice@dev.io  ", "BOB@DEV.IO  "]

    def transform(self, raw_data: list[Any]) -> list[Any]:
        return [str(email).strip().lower() for email in raw_data]

    def load(self, clean_data: list[Any]) -> None:
        print(f"Loaded clean users into database: {clean_data}")


if __name__ == "__main__":
    print("--- Level 1 ---")
    print(f"Dog sound: {Dog().sound()} | Cat sound: {Cat().sound()}")

    print("\n--- Level 4 (Template Method Pipeline) ---")
    pipeline = UserETLPipeline()
    pipeline.run()
