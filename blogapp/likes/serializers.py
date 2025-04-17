from rest_framework import serializers


class PostLikesCreateRequest(serializers.Serializer):
    """
    request object to add user likes to posts
    """
    user_id = serializers.IntegerField(allow_null=False)
    post_id = serializers.IntegerField(allow_null=False)


class PostLikesCreateResponse(serializers.Serializer):
    """
    response object to add user likes to posts
    """
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    post_id = serializers.IntegerField()


class PostCommentsCreateResponse(serializers.Serializer):
    """
    response object to add user likes to comments
    """
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    comment_id = serializers.IntegerField()
