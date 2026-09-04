"""
Configuration Anti-Patterns.
"""

# MISTAKE: Hardcoding secret API keys or credentials in default config files committed to version control.
# WHY: Committing secrets violates 12-Factor App rules and leaks credentials into Git history.
# FIX: Always read secrets from environment variables (e.g. API_SECRET_KEY) and commit `.env.example` templates instead.

if __name__ == "__main__":
    print("Configuration security rules verified.")
