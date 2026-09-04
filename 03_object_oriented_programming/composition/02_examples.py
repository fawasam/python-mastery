"""
Topic: Flexible Component Dependency Injection via Composition
File: 02_examples.py
"""

class SMTPTransporter:
    def send(self, recipient: str, body: str) -> None:
        print(f"[SMTP] Email sent to {recipient}: {body}")


class MockTransporter:
    def send(self, recipient: str, body: str) -> None:
        print(f"[MOCK] Logged payload for {recipient}")


class NotificationService:
    def __init__(self, transporter: Any) -> None:
        # Dependency Injection via Composition
        self.transporter = transporter

    def notify_user(self, user_email: str, msg: str) -> None:
        self.transporter.send(user_email, msg)


if __name__ == "__main__":
    from typing import Any

    prod_service = NotificationService(SMTPTransporter())
    test_service = NotificationService(MockTransporter())

    prod_service.notify_user("user@prod.com", "Password Reset")
    test_service.notify_user("test@dev.com", "Test Notification")
