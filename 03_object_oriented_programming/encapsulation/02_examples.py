"""
Topic: Encapsulated State Management
File: 02_examples.py
"""

class UserAccount:
    def __init__(self, username: str, password_hash: str) -> None:
        self.username = username
        self.__password_hash = password_hash

    def update_password(self, current_hash: str, new_hash: str) -> bool:
        if self.__password_hash == current_hash:
            self.__password_hash = new_hash
            print("Password updated successfully.")
            return True
        print("Error: Invalid current password verification.")
        return False


if __name__ == "__main__":
    u = UserAccount("alice", "hash_v1")
    u.update_password("hash_v1", "hash_v2")
