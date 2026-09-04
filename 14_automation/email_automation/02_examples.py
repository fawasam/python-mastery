"""
Advanced Email Automation: HTML Body and Attachments.
"""

from email.message import EmailMessage


def build_html_email_with_attachment(
    sender: str,
    recipient: str,
    subject: str,
    html_content: str,
    file_bytes: bytes,
    filename: str
) -> EmailMessage:
    """Build multi-part HTML email with attached document payload."""
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    
    # Add plain text fallback and HTML body
    msg.set_content("Please view this message in an HTML-compatible email client.")
    msg.add_alternative(html_content, subtype="html")
    
    # Attach binary file
    msg.add_attachment(file_bytes, maintype="application", subtype="octet-stream", filename=filename)
    
    return msg


if __name__ == "__main__":
    email = build_html_email_with_attachment(
        sender="billing@saas.com",
        recipient="user@example.com",
        subject="Your Invoice #1092",
        html_content="<h1>Invoice Attached</h1><p>Thank you for your payment.</p>",
        file_bytes=b"%PDF-1.4 sample pdf content",
        filename="invoice_1092.pdf"
    )
    print("Multi-part HTML Email constructed successfully.")
