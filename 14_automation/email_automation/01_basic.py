"""
Email Automation Basics: Building MIME Email Messages.
"""

from email.message import EmailMessage


def build_email_message(sender: str, recipient: str, subject: str, body_text: str) -> EmailMessage:
    """Construct an EmailMessage object ready for SMTP transmission."""
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body_text)
    return msg


if __name__ == "__main__":
    email = build_email_message(
        sender="alerts@company.com",
        recipient="admin@company.com",
        subject="Daily System Status Digest",
        body_text="All systems operating normally. 0 critical errors detected."
    )
    print("Generated Email Payload:")
    print(email.as_string())
