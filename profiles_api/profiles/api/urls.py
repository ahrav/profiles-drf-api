from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet, base_name="status")

urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="api-avatar-update"),
]
