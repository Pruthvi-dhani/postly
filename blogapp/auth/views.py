from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed

from auth.serializers import UserLoginRequest
from blogapp.security_utils import is_correct_password, generate_refresh_token
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
            resp = Response()
            return generate_refresh_token(user_id=user_obj.id, response=resp)
        else:
            raise ValidationError(detail="invalid request body")

    @action(detail=False, methods=["post"], url_path="refresh-token")
    def handle_refresh_token(self, request: Request) -> Response:
        pass
