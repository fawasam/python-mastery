"""
Topic: Property Solutions
File: 05_solution.py
"""
from datetime import datetime, timedelta, timezone

class Rectangle:
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    @property
    def area(self) -> float:
        return self.w * self.h


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, val: float) -> None:
        if val < 30000.0:
            raise ValueError("Salary cannot be below minimum threshold ($30,000).")
        self._salary = val


class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, val: float) -> None:
        self._celsius = val

    @property
    def fahrenheit(self) -> float:
        return round(self._celsius * 1.8 + 32, 2)

    @fahrenheit.setter
    def fahrenheit(self, f_val: float) -> None:
        self._celsius = (f_val - 32) / 1.8


class CachedAPIResponse:
    def __init__(self, payload: dict, ttl_seconds: int = 60) -> None:
        self.payload = payload
        self.ttl_seconds = ttl_seconds
        self._fetched_at = datetime.now(timezone.utc)

    @property
    def is_expired(self) -> bool:
        elapsed = (datetime.now(timezone.utc) - self._fetched_at).total_seconds()
        return elapsed > self.ttl_seconds


if __name__ == "__main__":
    print("--- Level 1 ---")
    r = Rectangle(10, 5)
    print(f"Area: {r.area}")

    print("\n--- Level 3 ---")
    t = Temperature(0.0)
    print(f"0°C in °F: {t.fahrenheit}°F")
    t.fahrenheit = 212.0
    print(f"212°F in °C: {t.celsius}°C")

    print("\n--- Level 4 ---")
    cache = CachedAPIResponse({"data": "test"}, ttl_seconds=1)
    print(f"Is cached API response expired? {cache.is_expired}")
