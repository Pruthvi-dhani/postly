from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authcustom.views import AuthenticationView

router = DefaultRouter()
router.register(r"", AuthenticationView, basename="auth")

urlpatterns = [
    path("", include(router.urls))
]
