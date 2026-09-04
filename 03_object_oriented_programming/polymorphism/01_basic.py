"""
Topic: Duck Typing & Polymorphism Basics
File: 01_basic.py
"""
from typing import Any

class ConsoleNotifier:
    def notify(self, message: str) -> None:
        print(f"[Console] {message}")


class EmailNotifier:
    def notify(self, message: str) -> None:
        print(f"[Email Dispatch] Sending: '{message}'")


class SlackNotifier:
    def notify(self, message: str) -> None:
        print(f"[Slack Webhook] Sending: '{message}'")


# Polymorphic dispatcher accepting ANY object with a notify(message) method
def send_system_alert(notifier: Any, message: str) -> None:
    notifier.notify(message)


if __name__ == "__main__":
    notifiers = [ConsoleNotifier(), EmailNotifier(), SlackNotifier()]

    for n in notifiers:
        send_system_alert(n, "System maintenance scheduled for 00:00 UTC")
