import logging

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

from blogapp.authentication_utils import check_token_authentication
from likes.models import PostLikes, CommentLikes
from likes.serializers import PostCommentsCreateResponse, PostLikesCreateResponse
# Create your views here.


class PostLikesView(APIView):
    """
    add and del likes on posts
    """
    @method_decorator(check_token_authentication)
    # @action(detail=False, methods=["post"], url_path=r"posts/(?P<post_id>\d+)")
    def post(self, request: Request, customer_id: int, post_id: int) -> Response:
        try:
            data_obj = PostLikes.objects.create(user_id=customer_id, post_id=post_id)
        except IntegrityError as e:
            logging.info("encountered exception adding like to post: " + str(e))
            raise ValidationError(detail="user already likes post")
        resp = PostLikesCreateResponse(data_obj)
        return Response(resp.data, status=status.HTTP_200_OK)

    @method_decorator(check_token_authentication)
    # @action(detail=False, methods=["delete"], url_path=r"posts/(?P<post_id>\d+)")
    def delete(self, request: Request, customer_id: int, post_id: int) -> Response:
        try:
            data_obj = PostLikes.objects.get(user_id=customer_id, post_id=post_id, is_deleted=False)
            data_obj.delete()
        except IntegrityError as e:
            logging.info("encountered exception adding like to post: " + str(e))
            raise ValidationError(detail="user already likes post")
        return Response({}, status=status.HTTP_200_OK)


class CommentLikesView(APIView):
    """
    add and del likes on comments
    """
    @method_decorator(check_token_authentication)
    # @action(detail=False, methods=["post"], url_path=r"comments/(?P<comment_id>\d+)")
    def post(self, request: Request, customer_id: int, comment_id: int) -> Response:
        try:
            data_obj = CommentLikes.objects.create(user_id=customer_id, comment_id=comment_id)
        except IntegrityError as e:
            logging.info("encountered exception adding like to comment: " + str(e))
            raise ValidationError(detail="user already likes comment")
        resp = PostCommentsCreateResponse(data_obj)
        return Response(resp.data, status=status.HTTP_200_OK)

    @method_decorator(check_token_authentication)
    # @action(detail=False, methods=["delete"], url_path=r"comments/(?P<comment_id>\d+)")
    def delete(self, request: Request, customer_id: int, comment_id: int) -> Response:
        try:
            data_obj = CommentLikes.objects.get(user_id=customer_id, comment_id=comment_id, is_deleted=False)
            data_obj.delete()
        except IntegrityError as e:
            logging.info("encountered exception adding like to comment: " + str(e))
            raise ValidationError(detail="user already likes comment")
        return Response({}, status=status.HTTP_200_OK)
