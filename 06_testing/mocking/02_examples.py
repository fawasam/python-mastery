"""
Mocking Exceptions with side_effect.
"""

from unittest.mock import MagicMock, patch


class PaymentGateway:
    def charge(self, card_number: str, amount: float) -> bool:
        raise ConnectionError("Network unreachable")


def process_order_payment(gateway: PaymentGateway, card: str, amount: float) -> str:
    try:
        gateway.charge(card, amount)
        return "SUCCESS"
    except ConnectionError:
        return "PAYMENT_FAILED_RETRY"


def test_payment_failure_retry() -> None:
    mock_gateway = MagicMock()
    # Configure side_effect to raise an exception when charge is invoked
    mock_gateway.charge.side_effect = ConnectionError("Timeout")

    status = process_order_payment(mock_gateway, "4111-2222-3333-4444", 99.99)

    assert status == "PAYMENT_FAILED_RETRY"
    mock_gateway.charge.assert_called_once_with("4111-2222-3333-4444", 99.99)
    print("Side effect mock test passed successfully!")


if __name__ == "__main__":
    test_payment_failure_retry()
