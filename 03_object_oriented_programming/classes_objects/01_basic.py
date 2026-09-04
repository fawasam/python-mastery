"""
Topic: Classes & Objects Basics
File: 01_basic.py
"""

class Car:
    # Class attribute shared across all Car instances
    wheels: int = 4

    def __init__(self, make: str, model: str, year: int) -> None:
        # Instance attributes unique to each Car instance
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment: int) -> None:
        self.speed += increment
        print(f"Accelerated {self.make} {self.model} to {self.speed} km/h")


if __name__ == "__main__":
    car1 = Car("Tesla", "Model 3", 2024)
    car2 = Car("Porsche", "911", 2023)

    print(f"Car 1: {car1.year} {car1.make} {car1.model}")
    car1.accelerate(50)
    print(f"Car 2 speed (independent): {car2.speed} km/h")
