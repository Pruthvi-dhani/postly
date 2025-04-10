class CustomException(Exception):
    """
    class to handle custom app exceptions
    """
    def __init__(self, message="Something went wrong", code=100):
        self.message = message
        self.code = code
        super().__init__(message)


JWT_TOKEN_EXPIRED_MSG, JWT_TOKEN_EXPIRED_CODE = "jwt token expired", 101
JWT_TOKEN_INVALID_MSG, JWT_TOKEN_INVALID_CODE = "jwt token invalid", 102
JWT_TOKEN_ID_NOT_PRESENT_MSG, JWT_TOKEN_ID_NOT_PRESENT_CODE = "id not present in jwt token", 103
JWT_TOKEN_MISSING_MSG, JWT_TOKEN_MISSING_CODE = "jwt token missing", 104
