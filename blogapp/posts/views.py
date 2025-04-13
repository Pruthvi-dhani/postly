from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotAuthenticated

from posts.serializers import CreatePostRequest, CreatePostResponse
from posts.models import Posts

from blogapp.authentication_utils import check_token_authentication


# Create your views here.
class UserPostView(APIView):
    """
    controller to handle user posts
    """
    @method_decorator(check_token_authentication)
    def post(self, request: Request, customer_id: int):
        cleaned_request = CreatePostRequest(data=request.data)
        if cleaned_request.is_valid():
            post_obj = Posts.objects.create(**(cleaned_request.data | {"user_id": customer_id}))
            post_resp = CreatePostResponse(post_obj)
            return Response(post_resp.data, status=status.HTTP_200_OK)
        else:
            raise ValidationError("data input is wrong")

    @method_decorator(check_token_authentication)
    def get(self, request: Request, customer_id: int, post_id: int):
        post_obj = Posts.objects.get(pk=post_id, is_deleted=False)
        post_resp = CreatePostResponse(post_obj)
        return Response(post_resp.data, status=status.HTTP_200_OK)

    @method_decorator(check_token_authentication)
    def delete(self, request: Request, customer_id: int, post_id: int):
        post_obj: Posts = Posts.objects.get(pk=post_id, is_deleted=False)
        if customer_id != post_obj.user.id:
            raise NotAuthenticated("user not authenticated for this task")
        post_obj.is_deleted = True
        post_obj.save()
        return Response(None, status=status.HTTP_200_OK)

    @method_decorator(check_token_authentication)
    def put(self, request: Request, customer_id: int, post_id: int):
        post_obj: Posts = Posts.objects.get(pk=post_id, is_deleted=False)
        cleaned_request = CreatePostRequest(data=request.data)
        if cleaned_request.is_valid():
            cleaned_request = cleaned_request.data
            if customer_id != post_obj.user.id:
                raise NotAuthenticated("user not authenticated for this task")
            post_obj.title = cleaned_request["title"]
            post_obj.content = cleaned_request["content"]
            post_obj.save()
            put_resp = CreatePostResponse(post_obj)
            return Response(put_resp.data, status=status.HTTP_200_OK)
        raise ValidationError("data input is wrong")
