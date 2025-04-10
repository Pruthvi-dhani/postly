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
        self._prop_map["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
        self._prop_map["ACCESS_TOKEN_EXPIRY_MINS"] = int(os.environ.get("ACCESS_TOKEN_EXPIRY_MINS"))
        self._prop_map["REFRESH_TOKEN_EXPIRY_MINS"] = int(os.environ.get("REFRESH_TOKEN_EXPIRY_MINS"))
        self._prop_map["DEBUG_MODE"] = bool(int(os.environ.get("DEBUG_MODE")))
        self._prop_map["DJANGO_SECRET_KEY"] = os.environ.get("DJANGO_SECRET_KEY")

    def get_value(self, key):
        return self._prop_map[key]


app_config = AppConfig()
