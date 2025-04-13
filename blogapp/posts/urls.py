from django.urls import path
from posts import views

urlpatterns = [
    path("", views.UserPostView.as_view()),
    path("<int:post_id>", views.UserPostView.as_view())
]
