from rest_framework import serializers


class CreateCommentRequest(serializers.Serializer):
    """
    request object to create a comment
    """
    comment: str = serializers.CharField(allow_null=False, allow_blank=False, max_length=512)
    post_id: int = serializers.IntegerField(allow_null=False)
    parent_comment_id: int = serializers.IntegerField(allow_null=True)


class EditCommentRequest(serializers.Serializer):
    """
    request to edit a comment
    """
    comment: str = serializers.CharField(allow_null=False, allow_blank=False, max_length=512)


class CreateCommentResponse(serializers.Serializer):
    """
    request object to create a comment
    """
    comment: str = serializers.CharField()
    post_id: int = serializers.IntegerField()
    parent_comment_id: int = serializers.IntegerField()
    id: int = serializers.IntegerField()
