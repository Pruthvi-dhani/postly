import os


class AppConfig:
    """
    handles application properties
    """
    def __init__(self):
        self._prop_map = dict()
        # define list of env vars here
        self._prop_map["DB_HOST"] = os.environ.get("DB_HOST")
        self._prop_map["DB_PORT"] = os.environ.get("DB_PORT")
        self._prop_map["DB_USER"] = os.environ.get("DB_USER")
        self._prop_map["DB_PASSWORD"] = os.environ.get("DB_PASSWORD")
        self._prop_map["APP_TIMEZONE"] = os.environ.get("APP_TIMEZONE")

    def get_value(self, key):
        return self._prop_map[key]


app_config = AppConfig()
