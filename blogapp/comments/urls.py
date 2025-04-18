from django.urls import path

from .views import CommentsCrudView, CommentsPostView

urlpatterns = [
    path("", CommentsCrudView.as_view()),
    path("<int:comment_id>", CommentsCrudView.as_view()),
    path("get-post-comments", CommentsPostView.as_view())
]