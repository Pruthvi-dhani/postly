from rest_framework import serializers


class CreateUserRequest(serializers.Serializer):
    """
    request object for creating user
    """
    username = serializers.CharField(max_length=50, allow_null=False, allow_blank=False)
    email = serializers.CharField(max_length=256, allow_null=False, allow_blank=False)
    about = serializers.CharField(max_length=1024)

