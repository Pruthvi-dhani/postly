from django.urls import path, include
from rest_framework.routers import DefaultRouter

from auth.views import AuthenticationView

router = DefaultRouter()
router.register(r"", AuthenticationView, basename="")

urlpatterns = [
    path("", include(router.urls))
]
