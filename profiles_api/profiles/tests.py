import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .api.serializers import ProfileSerializer
from .models import Profile


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            "username": "testuser",
            "email": "test@test.com",
            "password1": "somestrongpass",
            "password2": "somestrongpass",
        }
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    list_url = reverse("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(
            username="bobbys", password="somestorngshit"
        )
        self.token = Token.objects.create(user=self.user)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse("profile-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "bobbys")

    def test_profile_update_by_owner(self):
        response = self.client.put(
            reverse("profile-detail", kwargs={"pk": 1}),
            {"city": "bolly", "bio": "renaiseance"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_update_by_un_auth(self):
        random_user = User.objects.create_user(
            username="whatit", password="someshitpasshere"
        )
        self.client.force_authenticate(user=random_user)
        response = self.client.put(
            reverse("profile-detail", kwargs={"pk": 1}), {"bio": "hacked"}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
