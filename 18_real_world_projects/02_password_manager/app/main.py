"""
Password Manager CLI Main.
"""

from app.vault import PasswordVault


def main() -> None:
    print("=== Secure CLI Password Manager ===")
    master = "SecretMasterPassword123"
    vault = PasswordVault(master)
    
    vault.add_entry("github", "dev_user", "ghp_super_secret_token")
    
    if vault.authenticate(master):
        entry = vault.get_entry("github")
        if entry:
            print(f"Retrieved Service '{entry.service_name}': Username={entry.username}, Secret={entry.password}")


if __name__ == "__main__":
    main()
