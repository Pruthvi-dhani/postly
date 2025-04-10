from rest_framework import serializers


class UserLoginRequest(serializers.Serializer):
    """ request object that handles user login requests """
    username = serializers.CharField(max_length=50, allow_null=False, allow_blank=False)
    password = serializers.CharField(max_length=72, allow_null=False, allow_blank=False)
