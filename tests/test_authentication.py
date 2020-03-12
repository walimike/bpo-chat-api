from rest_framework import status

from .test_base import BaseTest


class TestAuthentication(BaseTest):

    def test_for_new_user(self):
        response = self.client.post('/api/v1/users/signup/', self.valid_registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_for_missing_username(self):
        response = self.client.post('/api/v1/users/signup/', self.invaid_user_name, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This field may not be blank.", str(response.data))

    def test_for_missing_email(self):
        response = self.client.post('/api/v1/users/signup/', self.invaid_email, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Enter a valid email address", str(response.data))

    def test_for_non_matching_passwords(self):
        response = self.client.post('/api/v1/users/signup/', self.non_matching_passwords, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Passwords must much", str(response.data))

    def test_unique_user_email(self):
        self.client.post('/api/v1/users/signup/', self.valid_registration_data, format='json')
        re = self.client.post('/api/v1/users/signup/', self.valid_registration_data, format='json')
        self.assertEqual(re.status_code, status.HTTP_400_BAD_REQUEST)


    def test_login(self):
        response = self.register_and_login() 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hello_view(self):
        response = self.client.get('/api/v1/users/hello/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
