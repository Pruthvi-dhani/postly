from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

from blogapp.authentication_utils import check_token_authentication
from user.serializers import CreateUserRequest, UserDetailsResponse
from user.models import User
from blogapp.security_utils import encode_password


# Create your views here.
class UserDetailsView(APIView):
    """
    controller to handle user creation, view details, update details and deletion
    """
    @method_decorator(check_token_authentication)
    def get(self, request: Request, customer_id: int, user_id: int):
        user_obj = User.objects.get(pk=user_id)
        user_resp = UserDetailsResponse(user_obj)
        return Response(user_resp.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        cleaned_request = CreateUserRequest(data=request.data)
        if cleaned_request.is_valid():
            cleaned_data = cleaned_request.data
            cleaned_data["password"] = encode_password(cleaned_data["password"])
            user_obj = User.objects.create(**cleaned_data)
            user_resp = UserDetailsResponse(user_obj)
            return Response(user_resp.data, status=status.HTTP_200_OK)
        else:
            raise ValidationError(detail="something wrong with post body")
