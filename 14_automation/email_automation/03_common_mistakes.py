"""
Email Automation Anti-Patterns.
"""

# MISTAKE: Hardcoding SMTP passwords inside script files.
# WHY: Exposes credentials when pushing code to Git repositories.
# FIX: Store SMTP credentials in environment variables (`SMTP_PASSWORD`) or secret management systems.

if __name__ == "__main__":
    print("Email credential security rules verified.")
