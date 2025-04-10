from functools import wraps

from rest_framework.request import Request

from blogapp.custom_exceptions import CustomException, JWT_TOKEN_MISSING_MSG, JWT_TOKEN_MISSING_CODE
from blogapp.security_utils import validate_and_return_user_id_jwt_token


def check_token_authentication(view_func):
    """
    decorator that checks for validity of jwt before the view function is called
    use this decorator before calling other functional decorators
    """
    @wraps(view_func)
    def _wrapped_view(request: Request, *args, **kwargs):
        access_token = request.headers.get("Access-Token")
        if access_token:
            customer_id = validate_and_return_user_id_jwt_token(access_token)
        else:
            raise CustomException(JWT_TOKEN_MISSING_MSG, JWT_TOKEN_MISSING_CODE)
        return view_func(request=request, customer_id=customer_id, *args, **kwargs)

    return _wrapped_view
