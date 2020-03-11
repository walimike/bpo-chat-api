from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.apps.authentication.models import User


class Authentication(APITestCase):

    def test_for_new_user(self):
        data =  {"username": "akram",
                "email": "akram@gmail.com",
                "password": "password123",
                "password2": "password123"}

        response = self.client.post('/api/v1/users/signup/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_for_missing_username(self):
        """
        Method for testing if there is a missing username during registration.
        """
        data = {"username": "", 
                "email": "akram@gmail.com",
                "password": "password123",
                "password2": "password123"}
        response = self.client.post('/api/v1/users/signup/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This field may not be blank.", str(response.data))

    def test_for_missing_email(self):
        """
        Method for testing if there is a missing email during registration.
        """
        data = {"user": {"username": "mukasa", "email": "", "password":
                "akrammukasa"}}
        response = self.client.post('/api/v1/users/signup/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This field is required", str(response.data))

    def test_login(self):
        data =  {"username": "akram",
                "email": "akram@gmail.com",
                "password": "password123",
                "password2": "password123"}

        response = self.client.post('/api/v1/users/signup/', data, format='json')

        data = {"email": "akram@gmail.com", 
                "password": "password123"}
        response = self.client.post('/api/v1/users/login/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
