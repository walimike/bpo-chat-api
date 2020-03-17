from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class BaseTest(APITestCase):

    def setUp(self):

        self.valid_registration_data = {
            "username": "akram",
            "email": "akram@gmail.com",
            "password": "password123",
            "password2": "password123"
            }

        self.second_valid_registration_data = {
            "username": "mabel",
            "email": "mabel@gmail.com",
            "password": "password123",
            "password2": "password123"
            }

        self.invaid_user_name = {
            "username": "", 
            "email": "akram@gmail.com",
            "password": "password123",
            "password2": "password123"
            }

        self.invaid_email = {
            "username": "", 
            "email": "akramcom",
            "password": "password123",
            "password2": "password123"
            }

        self.non_matching_passwords = {
            "username": "akram",
            "email": "akram@gmail.com",
            "password": "password123",
            "password2": "password1234"
            }

        self.client = APIClient()

    def register_and_login(self):
        self.client.post('/api/v1/users/signup/',
                                    self.valid_registration_data,
                                    format='json')
        
        login_data = {
                "email": "akram@gmail.com",
                "password": "password123"
            }
        
        login_response = self.client.post('/api/v1/users/login/',
                                          login_data, format='json')
        return login_response

    def register_and_login_second_user(self):
        self.client.post('/api/v1/users/signup/',
                                    self.second_valid_registration_data,
                                    format='json')
        
        login_data = {
                "email": "mabel@gmail.com",
                "password": "password123"
            }
        
        login_response = self.client.post('/api/v1/users/login/',
                                          login_data, format='json')
        return login_response

    def access_token(self):
        response = self.register_and_login()
        return response.data['access']

    def second_user_access_token(self):
        response = self.register_and_login_second_user()
        return response.data['access']

    def create_a_chat_instance(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token())
        
        response = self.client.post('/api/v1/chats/',
                                    {"username":"akram"},
                                    format='json')
        return response

    def join_chat_instance(self):
        re = self.create_a_chat_instance()
        chat_uri = re.data['uri']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.second_user_access_token())
        
        response = self.client.patch(f"/api/v1/chats/{chat_uri}/",
                                    {"username":"mabel"},
                                    format='json')
        return response

    def send_chat_message(self):
        re = self.create_a_chat_instance()
        chat_uri = re.data['uri']
        
        response = self.client.post(f"/api/v1/chats/{chat_uri}/messages/",
                                    {"message":"hello world"},
                                    format='json')
        return response

    def get_chat_history(self):
        re = self.create_a_chat_instance()
        chat_uri = re.data['uri']
        
        re = self.client.get(f"/api/v1/chats/{chat_uri}/messages/",
                                    format='json')
        return re
