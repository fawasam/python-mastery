"""
Topic: Composition Basics ("Has-A" Architecture)
File: 01_basic.py
"""

class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

    def start(self) -> str:
        return f"Engine ({self.horsepower} HP) started."


class Computer:
    def __init__(self, cpu_model: str, ram_gb: int) -> None:
        self.cpu_model = cpu_model
        self.ram_gb = ram_gb


class Car:
    def __init__(self, make: str, engine: Engine, computer: Computer) -> None:
        self.make = make
        self.engine = engine      # Car HAS AN Engine
        self.computer = computer  # Car HAS A Computer

    def start_car(self) -> None:
        print(f"[{self.make}] Booting onboard CPU {self.computer.cpu_model}...")
        print(f"[{self.make}] {self.engine.start()}")


if __name__ == "__main__":
    v8_engine = Engine(450)
    ecu_computer = Computer("ARM-v8-ECU", 16)

    sports_car = Car("Porsche", v8_engine, ecu_computer)
    sports_car.start_car()
