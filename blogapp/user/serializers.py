from rest_framework import serializers


class CreateUserRequest(serializers.Serializer):
    """
    request object for creating user
    """
    username = serializers.CharField(max_length=50, allow_null=False, allow_blank=False)
    email = serializers.CharField(max_length=256, allow_null=False, allow_blank=False)
    about = serializers.CharField(max_length=1024)
    password = serializers.CharField(max_length=72, allow_null=False, allow_blank=False, min_length=15)


class UserDetailsResponse(serializers.Serializer):
    """
    response object for user domain model
    """
    id = serializers.IntegerField()
    email = serializers.CharField(max_length=256, allow_null=False, allow_blank=False)
    about = serializers.CharField(max_length=1024)
