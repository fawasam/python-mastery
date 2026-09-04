"""
Tests for Password Manager Vault.
"""

from app.vault import PasswordVault


def test_vault_auth_and_retrieval() -> None:
    vault = PasswordVault("master123")
    assert vault.authenticate("master123") is True
    assert vault.authenticate("wrong_pass") is False

    vault.add_entry("aws", "admin", "secret_key")
    entry = vault.get_entry("aws")
    assert entry is not None
    assert entry.password == "secret_key"
