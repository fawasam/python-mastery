"""
Solutions for Custom Exception Exercises.
"""


class ConfigError(Exception):
    pass


class MissingConfigKeyError(ConfigError):
    def __init__(self, key: str) -> None:
        super().__init__(f"Configuration key '{key}' is missing.")
        self.key = key


class InvalidConfigValueError(ConfigError):
    def __init__(self, key: str, value: object) -> None:
        super().__init__(f"Invalid value '{value}' for configuration key '{key}'.")
        self.key = key
        self.value = value


def load_setting(config: dict[str, object], key: str) -> object:
    if key not in config:
        raise MissingConfigKeyError(key)
    val = config[key]
    if val is None:
        raise InvalidConfigValueError(key, val)
    return val


if __name__ == "__main__":
    cfg = {"port": 8080, "host": None}

    try:
        load_setting(cfg, "db_name")
    except MissingConfigKeyError as e:
        print(f"Caught Missing Key Error: {e}")

    try:
        load_setting(cfg, "host")
    except InvalidConfigValueError as e:
        print(f"Caught Invalid Value Error: {e}")
