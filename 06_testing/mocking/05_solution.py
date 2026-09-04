"""
Solutions for Mocking Exercises.
"""

from unittest.mock import MagicMock


class EmailSender:
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        raise NotImplementedError("Production email client")


def notify_user_welcome(sender: EmailSender, email: str) -> bool:
    return sender.send_email(email, "Welcome!", "Thanks for signing up.")


def test_notify_user_welcome() -> None:
    mock_sender = MagicMock(spec=EmailSender)
    mock_sender.send_email.return_value = True

    result = notify_user_welcome(mock_sender, "user@example.com")

    assert result is True
    mock_sender.send_email.assert_called_once_with("user@example.com", "Welcome!", "Thanks for signing up.")
    print("Mocking exercise solution test passed.")


if __name__ == "__main__":
    test_notify_user_welcome()
