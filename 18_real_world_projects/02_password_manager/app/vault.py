"""
Password Vault Storage Engine.
"""

from dataclasses import dataclass, field
import os
from app.crypto import hash_password, verify_password


@dataclass
class VaultEntry:
    service_name: str
    username: str
    password: str


class PasswordVault:
    def __init__(self, master_password: str) -> None:
        self.salt = os.urandom(16)
        self.master_hash = hash_password(master_password, self.salt)
        self._entries: dict[str, VaultEntry] = {}

    def authenticate(self, master_password: str) -> bool:
        return verify_password(master_password, self.salt, self.master_hash)

    def add_entry(self, service: str, username: str, secret: str) -> None:
        self._entries[service.lower()] = VaultEntry(service_name=service, username=username, password=secret)

    def get_entry(self, service: str) -> VaultEntry | None:
        return self._entries.get(service.lower())
