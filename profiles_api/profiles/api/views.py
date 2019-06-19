from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerProfileOrReadOnly, IsOwnerOrReadOnly
from ..models import Profile, ProfileStatus
from .serializers import ProfileSerializer, ProfileStatusSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_class = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_class = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
