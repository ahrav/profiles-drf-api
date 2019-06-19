from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, ProfileStatusViewSet

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet)

urlpatterns = [path("", include(router.urls))]
