"""
Topic: Inheritance Solutions
File: 05_solution.py
"""
import math

class Vehicle:
    def __init__(self, brand: str, speed: float) -> None:
        self.brand = brand
        self.speed = speed

    def drive(self) -> str:
        return f"{self.brand} driving at {self.speed} km/h"


class ElectricCar(Vehicle):
    def __init__(self, brand: str, speed: float, battery_capacity: int) -> None:
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity

    def drive(self) -> str:
        return f"{self.brand} EV (Battery: {self.battery_capacity}kWh) driving silently at {self.speed} km/h"


class Shape:
    def area(self) -> float:
        return 0.0


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return round(self.width * self.height, 2)


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return round(math.pi * (self.radius ** 2), 2)


class BaseAuth:
    def authenticate(self, credentials: dict) -> bool:
        raise NotImplementedError


class JWTAuth(BaseAuth):
    def __init__(self, secret: str) -> None:
        self.secret = secret

    def authenticate(self, credentials: dict) -> bool:
        token = credentials.get("token")
        is_valid = bool(token and token.startswith("bearer_"))
        print(f"JWT Authentication for token '{token}': {is_valid}")
        return is_valid


if __name__ == "__main__":
    print("--- Level 1 ---")
    ev = ElectricCar("Tesla", 120.0, 85)
    print(ev.drive())

    print("\n--- Level 2 ---")
    r = Rectangle(10.0, 5.0)
    c = Circle(7.0)
    print(f"Rectangle Area: {r.area()} | Circle Area: {c.area()}")

    print("\n--- Level 4 ---")
    jwt = JWTAuth("secret_key_123")
    jwt.authenticate({"token": "bearer_abc123"})
