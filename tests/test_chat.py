from rest_framework import status

from .test_base import BaseTest


class TestChat(BaseTest):

    def test_create_chat_instance(self):
        response = self.create_a_chat_instance()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_join_chat_instance(self):
        response = self.join_chat_instance()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_send_message_to_chat_instance(self):
        response = self.send_chat_message()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_messages_from_chat_instance(self):
        response = self.get_chat_history()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
