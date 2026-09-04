"""
Basic Mocking with unittest.mock.MagicMock.
"""

from unittest.mock import MagicMock


class WeatherService:
    def get_temperature(self, city: str) -> float:
        # In production this calls remote weather API
        raise RuntimeError("Real HTTP network call executed!")


def check_jacket_needed(service: WeatherService, city: str) -> bool:
    temp = service.get_temperature(city)
    return temp < 15.0


def test_check_jacket_needed() -> None:
    # Instantiate dummy MagicMock replacing WeatherService
    mock_service = MagicMock(spec=WeatherService)
    # Configure return value for get_temperature
    mock_service.get_temperature.return_value = 10.0

    result = check_jacket_needed(mock_service, "London")

    assert result is True
    # Verify mock call interaction
    mock_service.get_temperature.assert_called_once_with("London")
    print("Mocking test passed successfully!")


if __name__ == "__main__":
    test_check_jacket_needed()
