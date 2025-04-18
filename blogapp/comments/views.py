from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from django.utils.decorators import method_decorator
from django.db import models

from blogapp.authentication_utils import check_token_authentication
from comments.serializers import CreateCommentRequest, CreateCommentResponse, EditCommentRequest
from comments.models import Comments


# Create your views here.
class CommentsCrudView(APIView):
    """
    api controller that handles comments
    """
    @method_decorator(check_token_authentication)
    def post(self, request: Request, customer_id: int):
        cleaned_request = CreateCommentRequest(data=request.data)
        if cleaned_request.is_valid():
            cleaned_request = cleaned_request.data
            # does the parent comment exist under the same post
            post_id = cleaned_request["post_id"]
            parent_comment_id = cleaned_request["parent_comment_id"]
            if parent_comment_id:
                parent_comment = Comments.objects.get(pk=parent_comment_id, is_deleted=False, post_id=post_id)
            comment_obj = Comments.objects.create(**{
                "comment": cleaned_request["comment"],
                "parent_comment_id": parent_comment_id,
                "user_id": customer_id,
                "post_id": post_id
            })
            resp = CreateCommentResponse(comment_obj)
            return Response(resp.data, status=status.HTTP_202_ACCEPTED)
        raise ValidationError("request body is bad")

    @method_decorator(check_token_authentication)
    def get(self, request: Request, customer_id: int, comment_id: int):
        comment = Comments.objects.get(pk=comment_id, is_deleted=False)
        resp = CreateCommentResponse(comment)
        return Response(resp.data, status=status.HTTP_200_OK)

    @method_decorator(check_token_authentication)
    def delete(self, request: Request, customer_id: int, comment_id: int):
        comment = Comments.objects.get(pk=comment_id, is_deleted=False, user_id=customer_id)
        comment.is_deleted = True
        comment.save()
        return Response(None, status=status.HTTP_200_OK)

    @method_decorator(check_token_authentication)
    def put(self, request: Request, customer_id: int, comment_id: int):
        cleaned_request = EditCommentRequest(data=request.data)
        comment = Comments.objects.get(pk=comment_id, is_deleted=False, user_id=customer_id)
        if cleaned_request.is_valid():
            cleaned_request = cleaned_request.data
            comment.comment = cleaned_request["comment"]
            comment.save()
            resp = CreateCommentResponse(comment)
            return Response(resp.data, status=status.HTTP_200_OK)
        raise ValidationError("request is invalid")


class CommentsPostView(APIView):
    """
    api controller to get comments related to a post
    """
    @staticmethod
    def _get_comments_one_level_deep(post_id: int, parent_comment_id: int = None) -> list[dict]:
        """
        gets the next level of comments with the count of replies
        """
        replies_objs = Comments.objects.filter(
            post_id=post_id,
            is_deleted=False,
            parent_comment_id=parent_comment_id
        ).annotate(
            replies_count=models.Count("child_comments")
        )
        replies_lst = list()
        for replies_obj in replies_objs:
            replies_lst.append({
                "id": replies_obj.id,
                "comment": replies_obj.comment,
                "replies_count": replies_obj.replies_count
            })
        return replies_lst

    @method_decorator(check_token_authentication)
    def get(self, request: Request, customer_id: int):
        post_id = request.query_params.get("post_id")
        parent_comment_id = request.query_params.get("parent_comment_id")
        if post_id:
            post_id = int(post_id)
        if parent_comment_id:
            parent_comment_id = int(parent_comment_id)
        comments = self._get_comments_one_level_deep(post_id, parent_comment_id)
        return Response({"data": comments}, status=status.HTTP_200_OK)
