"""
Common Mistakes in API Authentication.
"""


# MISTAKE 1: Hardcoding Secret Keys inside source code
def mistake_hardcoded_secret() -> None:
    # DANGER: Storing SECRET_KEY = "my_secret_123" in git repository allows attackers to forge tokens!
    # ALWAYS load secrets from environment variables (os.environ or .env)!
    pass


if __name__ == "__main__":
    print("Always load authentication JWT secrets and API tokens from secure environment variables!")
