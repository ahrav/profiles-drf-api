from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerProfileOrReadOnly, IsOwnerOrReadOnly
from ..models import Profile, ProfileStatus
from .serializers import (
    ProfileSerializer,
    ProfileStatusSerializer,
    ProfileAvatarSerializer,
)


class AvatarUpdateView(UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_class = [IsOwnerProfileOrReadOnly, IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ["city"]


class ProfileStatusViewSet(ModelViewSet):
    serializer_class = ProfileStatusSerializer
    permission_class = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get("username", None)
        if username:
            queryset = queryset.filter(user_profile_user_username=username)
        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
