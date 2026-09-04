"""
Advanced Design Patterns: Observer & Adapter Patterns in Python.
"""

from typing import Protocol


# ==========================================
# 1. Observer Pattern
# ==========================================

class Observer(Protocol):
    def update(self, temperature: float) -> None:
        ...


class WeatherStation:
    """Subject publishing temperature changes to subscribed observers."""
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._temperature: float = 0.0

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def set_temperature(self, temp: float) -> None:
        self._temperature = temp
        self._notify_all()

    def _notify_all(self) -> None:
        for obs in self._observers:
            obs.update(self._temperature)


class PhoneDisplay:
    def update(self, temperature: float) -> None:
        print(f"[Phone Display] Temperature updated: {temperature}°C")


class WindowDisplay:
    def update(self, temperature: float) -> None:
        print(f"[Window Display] LED screen temp: {temperature}°C")


# ==========================================
# 2. Adapter Pattern
# ==========================================

class LegacyXMLLogger:
    """Legacy third-party class expecting XML formatted strings."""
    def log_xml(self, xml_data: str) -> None:
        print(f"Legacy XML Logged: {xml_data}")


class ModernJSONLogger(Protocol):
    """Target interface expected by modern codebase."""
    def log_json(self, message: str) -> None:
        ...


class LoggerAdapter:
    """Adapter wrapping LegacyXMLLogger to expose the ModernJSONLogger interface."""
    def __init__(self, legacy_logger: LegacyXMLLogger) -> None:
        self.legacy_logger = legacy_logger

    def log_json(self, message: str) -> None:
        # Convert JSON-like string payload into legacy XML representation
        xml_payload = f"<log><message>{message}</message></log>"
        self.legacy_logger.log_xml(xml_payload)


if __name__ == "__main__":
    # Observer
    station = WeatherStation()
    station.attach(PhoneDisplay())
    station.attach(WindowDisplay())
    station.set_temperature(24.5)
    
    # Adapter
    legacy = LegacyXMLLogger()
    adapter: ModernJSONLogger = LoggerAdapter(legacy)
    adapter.log_json("User login succeeded")
