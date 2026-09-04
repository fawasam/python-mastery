"""
Mocking Exercises.
"""

from unittest.mock import MagicMock


class EmailSender:
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        raise NotImplementedError("Production email client")


def notify_user_welcome(sender: EmailSender, email: str) -> bool:
    return sender.send_email(email, "Welcome!", "Thanks for signing up.")


# Exercise 1 (Medium): Write a test function using MagicMock to test notify_user_welcome
def test_notify_user_welcome() -> None:
    raise NotImplementedError("Implement test_notify_user_welcome with MagicMock")
