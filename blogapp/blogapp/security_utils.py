import bcrypt
from datetime import timedelta
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from rest_framework.response import Response

from blogapp.custom_exceptions import CustomException, JWT_TOKEN_EXPIRED_MSG, JWT_TOKEN_EXPIRED_CODE, \
    JWT_TOKEN_INVALID_MSG, JWT_TOKEN_INVALID_CODE, JWT_TOKEN_ID_NOT_PRESENT_MSG, JWT_TOKEN_ID_NOT_PRESENT_CODE
from blogapp.utils import now
from blogapp.config import app_config


def encode_password(password: str) -> str:
    """ encodes the given password to a hashed repr suitable for storage """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def is_correct_password(db_hashed_pw: str, entered_pw: str) -> bool:
    """ checks if the entered user password is correct """
    return bcrypt.checkpw(entered_pw.encode("utf-8"), db_hashed_pw.encode("utf-8"))


def generate_refresh_token(user_id: int, response: Response) -> Response:
    """
    generates refresh token after successful user login
    """
    expiry_time = now() + timedelta(minutes=app_config.get_value("REFRESH_TOKEN_EXPIRY_MINS"))
    payload = {
        "user_id": user_id,
        "exp": expiry_time.timestamp()
    }
    encoded_jwt = jwt.encode(payload, app_config.get_value("JWT_SECRET_KEY"), algorithm="HS256")
    # refresh token is a http only cookie
    response.set_cookie(key="refresh_token", value=encoded_jwt, path="/", domain="", samesite="Strict", httponly=True)
    return response


def generate_access_token(user_id: int) -> dict:
    """
    generates a short-lived access token for user authentication
    """
    expiry_time = now() + timedelta(minutes=app_config.get_value("ACCESS_TOKEN_EXPIRY_MINS"))
    payload = {
        "user_id": user_id,
        "exp": expiry_time.timestamp()
    }
    encoded_jwt = jwt.encode(payload, app_config.get_value("JWT_SECRET_KEY"), algorithm="HS256")
    return {"access_token": encoded_jwt}


def validate_and_return_user_id_jwt_token(token: str) -> int:
    """
    validates the signature and exp of the given jwt token
    """
    # throws exception if token is invalid or expired
    try:
        payload = jwt.decode(token, app_config.get_value("JWT_SECRET_KEY"), algorithms=["HS256"])
    except ExpiredSignatureError:
        raise CustomException(JWT_TOKEN_EXPIRED_MSG, JWT_TOKEN_EXPIRED_CODE)
    except InvalidTokenError:
        raise CustomException(JWT_TOKEN_INVALID_MSG, JWT_TOKEN_INVALID_CODE)
    if "user_id" not in payload:
        raise CustomException(JWT_TOKEN_ID_NOT_PRESENT_MSG, JWT_TOKEN_ID_NOT_PRESENT_CODE)
    return payload["user_id"]
