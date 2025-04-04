from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

from .serializers import CreateUserRequest
from .models import User


# Create your views here.
class UserDetailsView(APIView):
    """
    controller to handle user creation, view details, update details and deletion
    """
    def get(self, request: Request):
        pass

    def post(self, request: Request):
        cleaned_request = CreateUserRequest(data=request.data)
        if cleaned_request.is_valid():
            cleaned_data = cleaned_request.data
            cleaned_data["password"] = "abc"
            User.objects.create(**cleaned_data)
            return Response({"detail": "user created"}, status=status.HTTP_200_OK)
        else:
            raise ValidationError(detail="something wrong with post body")
