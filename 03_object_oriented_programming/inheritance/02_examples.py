"""
Topic: Multiple Inheritance & Method Resolution Order (MRO)
File: 02_examples.py
"""

class Loggable:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class Serializable:
    def to_dict(self) -> dict[str, str]:
        return {"type": self.__class__.__name__}


class AuditUser(Loggable, Serializable):
    def __init__(self, username: str) -> None:
        self.username = username

    def to_dict(self) -> dict[str, str]:
        d = super().to_dict()
        d["username"] = self.username
        return d


if __name__ == "__main__":
    user = AuditUser("sarah_m")
    user.log("User profile loaded.")
    print(f"Serialized user: {user.to_dict()}")
    print(f"MRO Order: {[cls.__name__ for cls in AuditUser.mro()]}")
