from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from rest_framework import status

from authcustom.serializers import UserLoginRequest
from blogapp.custom_exceptions import CustomException, JWT_TOKEN_MISSING_MSG, JWT_TOKEN_MISSING_CODE
from blogapp.security_utils import is_correct_password, generate_refresh_token, validate_and_return_user_id_jwt_token, \
    generate_access_token
from user.models import User


# Create your views here.
class AuthenticationView(ViewSet):
    """
    api controller to handle user authentication
    """
    @action(detail=False, methods=["post"], url_path="login")
    def handle_user_login(self, request: Request) -> Response:
        cleaned_request = UserLoginRequest(data=request.data)
        if cleaned_request.is_valid():
            claimed_username = cleaned_request.data["username"]
            claimed_password = cleaned_request.data["password"]
            user_obj: User = User.objects.filter(username=claimed_username).first()
            if not user_obj:
                raise NotFound(detail="username doesn't exist")
            if not is_correct_password(db_hashed_pw=user_obj.password, entered_pw=claimed_password):
                raise AuthenticationFailed(detail="wrong password")
            resp = Response(status=status.HTTP_200_OK)
            return generate_refresh_token(user_id=user_obj.id, response=resp)
        else:
            raise ValidationError(detail="invalid request body")

    @action(detail=False, methods=["post"], url_path="refresh-token")
    def handle_refresh_token(self, request: Request) -> Response:
        refresh_token = request.COOKIES.get("refresh_token")
        if refresh_token:
            user_id = validate_and_return_user_id_jwt_token(refresh_token)
            return Response(generate_access_token(user_id), status=status.HTTP_200_OK)
        raise CustomException(JWT_TOKEN_MISSING_MSG, JWT_TOKEN_MISSING_CODE)
