
from django.contrib.auth import get_user_model
from .models import (
    ChatSession, ChatSessionMember, ChatSessionMessage, deserialize_user
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated


class ChatSessionView(APIView):
    """Manage Chat sessions."""
    
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        User = get_user_model()
        all_chats = []
        user = request.user
        chat_sessions = ChatSessionMember.objects.filter(user=user).values()
        for chat_session in chat_sessions:
            id = chat_session["chat_session_id"]
            chat_instance =  ChatSession.objects.filter(id=id).values()
            print(User.objects.filter(id=chat_instance[0]['owner_id']).values())

            all_chats.append(chat_instance[0])

        return Response({"message":all_chats})

    def post(self, request, *args, **kwargs):
        
        """create a new chat session."""
        User = get_user_model()
        user = request.user
        username = request.data['username']
        other_user = User.objects.get(username=username)
        
        try:
            chat_session = ChatSession.objects.get(owner=user)
        except ChatSession.DoesNotExist:
            try:
                chat_session = ChatSession.objects.get(owner=other_user)
            except ChatSession.DoesNotExist:
                chat_session = ChatSession.objects.create(owner=user)
                chat_session.save()
        owner = chat_session.owner

        if owner != user:        
            chat_session.members.get_or_create(
                user=user, chat_session=chat_session
            )

        owner = deserialize_user(owner)
        members = [
            deserialize_user(chat_session.user) 
            for chat_session in chat_session.members.all()
        ]
        members.insert(0, owner)
        return Response ({
            'status': 'SUCCESS', 'members': members,
            'message': '%s joined that chat' % user.username,
            'uri': chat_session.uri,
            'user': deserialize_user(user)
        })

    def patch(self, request, *args, **kwargs):
        """Add a user to a chat session."""
        User = get_user_model()

        uri = kwargs['uri']
        user = User.objects.get(username=request.user.username)
        chat_session = ChatSession.objects.get(uri=uri)
        owner = chat_session.owner

        if owner != user:        
            chat_session.members.get_or_create(
                user=user, chat_session=chat_session
            )

        owner = deserialize_user(owner)
        members = [
            deserialize_user(chat_session.user) 
            for chat_session in chat_session.members.all()
        ]
        members.insert(0, owner)
        return Response ({
            'status': 'SUCCESS', 'members': members,
            'message': '%s joined that chat' % user.username,
            'user': deserialize_user(user)
        })


class ChatSessionMessageView(APIView):
    """Create/Get Chat session messages."""

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """return all messages in a chat session."""
        uri = kwargs['uri']

        chat_session = ChatSession.objects.get(uri=uri)
        messages = [chat_session_message.to_json() 
            for chat_session_message in chat_session.messages.all()]

        return Response({
            'id': chat_session.id,
            'uri': chat_session.uri,
            'messages': messages
        })

    def post(self, request, *args, **kwargs):
        """create a new message in a chat session."""
        uri = kwargs['uri']
        message = request.data['message']

        user = request.user
        chat_session = ChatSession.objects.get(uri=uri)

        ChatSessionMessage.objects.create(
            user=user, chat_session=chat_session, message=message
        )
        messages = [chat_session_message.to_json() 
            for chat_session_message in chat_session.messages.all()]

        return Response ({
            'status': 'SUCCESS',
            'uri': chat_session.uri,
            'messages': messages
        })
