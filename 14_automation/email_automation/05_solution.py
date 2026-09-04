"""
Solutions: Email Automation Exercises.
"""

from email.message import EmailMessage


def format_support_ticket_email(ticket_id: str, user_email: str, issue_text: str) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = "support@company.com"
    msg["To"] = user_email
    msg["Subject"] = f"Support Ticket #{ticket_id}"
    msg.set_content(f"We received your issue:\n\n{issue_text}\n\nOur team is reviewing it.")
    return msg


if __name__ == "__main__":
    email = format_support_ticket_email("TK-500", "user@example.com", "App crashes on login")
    print("Ticket Subject:", email["Subject"])
