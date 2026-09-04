"""
Topic: Protocol Basics (Static Duck Typing)
File: 01_basic.py
"""
from typing import Protocol, runtime_checkable

@runtime_checkable
class Speaker(Protocol):
    def speak(self) -> str:
        ...


class Dog:
    def speak(self) -> str:
        return "Woof"


class Robot:
    def speak(self) -> str:
        return "Beep Boop"


def make_it_speak(speaker: Speaker) -> None:
    print(f"Speech: {speaker.speak()}")


if __name__ == "__main__":
    d = Dog()
    r = Robot()

    # Neither Dog nor Robot inherit from Speaker, yet both satisfy Speaker Protocol!
    make_it_speak(d)
    make_it_speak(r)
    print(f"Is Robot runtime checkable Speaker? {isinstance(r, Speaker)}")
