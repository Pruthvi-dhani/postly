from rest_framework import serializers


class CreatePostRequest(serializers.Serializer):
    """
    request object to create a user post
    """
    title = serializers.CharField(allow_null=False, allow_blank=False, max_length=128)
    content = serializers.CharField(allow_null=False, allow_blank=False, max_length=1024)


class CreatePostResponse(serializers.Serializer):
    """
    response object to be sent after creating a post
    """
    title = serializers.CharField()
    content = serializers.CharField()
    id = serializers.IntegerField()
