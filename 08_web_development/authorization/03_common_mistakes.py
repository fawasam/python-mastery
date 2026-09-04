"""
Common Mistakes in Authorization (BOLA / IDOR Vulnerabilities).
"""


# MISTAKE 1: Relying on client-side parameters for resource access without backend ownership checks
def mistake_idor_vulnerability() -> None:
    # DANGER: Route GET /api/v1/orders/{order_id} that fetches order solely by order_id
    # WITHOUT checking if current_user.id == order.user_id allows any authenticated user
    # to iterate order_id=1, 2, 3... and steal all customer records!
    pass


if __name__ == "__main__":
    print("Always verify resource ownership on every backend query (BOLA protection)!")
