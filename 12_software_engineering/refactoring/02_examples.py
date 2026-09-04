"""
Advanced Refactoring: Replacing Complex Conditionals with Polymorphism.
"""

from abc import ABC, abstractmethod


# --- BEFORE REFACTORING ---
class DirtyNotificationSender:
    """Code Smell: Switch Statement / Conditional complexity on type string."""
    def send(self, notification_type: str, user: str, message: str) -> None:
        if notification_type == "email":
            print(f"SMTP Email to {user}: {message}")
        elif notification_type == "sms":
            print(f"Twilio SMS to {user}: {message}")
        elif notification_type == "slack":
            print(f"Slack Webhook to {user}: {message}")
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")


# --- AFTER REFACTORING ---

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, user: str, message: str) -> None:
        pass


class EmailChannel(NotificationChannel):
    def send(self, user: str, message: str) -> None:
        print(f"SMTP Email to {user}: {message}")


class SMSChannel(NotificationChannel):
    def send(self, user: str, message: str) -> None:
        print(f"Twilio SMS to {user}: {message}")


class SlackChannel(NotificationChannel):
    def send(self, user: str, message: str) -> None:
        print(f"Slack Webhook to {user}: {message}")


class RefactoredNotificationSender:
    """Refactored: Uses polymorphism instead of nested conditional checks."""
    def __init__(self, channel: NotificationChannel) -> None:
        self.channel = channel

    def send(self, user: str, message: str) -> None:
        self.channel.send(user, message)


if __name__ == "__main__":
    sender = RefactoredNotificationSender(SlackChannel())
    sender.send("dev-team", "Deployment completed successfully!")
