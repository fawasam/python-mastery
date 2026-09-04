"""
Topic: Polymorphism Solutions
File: 05_solution.py
"""
from typing import Any

class Dog:
    def speak(self) -> str:
        return "Woof!"


class Cat:
    def speak(self) -> str:
        return "Meow!"


def animal_sound(animal: Any) -> None:
    print(f"Sound: {animal.speak()}")


class S3Storage:
    def upload(self, filename: str, data: bytes) -> str:
        res = f"s3://my-bucket/{filename} ({len(data)} bytes)"
        print(f"[S3 Upload] {res}")
        return res


class LocalStorage:
    def upload(self, filename: str, data: bytes) -> str:
        res = f"/var/data/uploads/{filename} ({len(data)} bytes)"
        print(f"[Local Save] {res}")
        return res


def upload_user_avatar(storage_provider: Any, filename: str, data: bytes) -> str:
    return storage_provider.upload(filename, data)


if __name__ == "__main__":
    print("--- Level 1 ---")
    animal_sound(Dog())
    animal_sound(Cat())

    print("\n--- Level 4 ---")
    raw_bytes = b"avatar binary data"
    upload_user_avatar(S3Storage(), "avatar_101.png", raw_bytes)
    upload_user_avatar(LocalStorage(), "avatar_101.png", raw_bytes)
