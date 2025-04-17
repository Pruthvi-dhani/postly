from django.urls import path

from likes.views import PostLikesView, CommentLikesView

urlpatterns = [
    path("posts/<int:post_id>", PostLikesView.as_view()),
    path("comments/<int:comment_id>", CommentLikesView.as_view())
]
