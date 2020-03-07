from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import RegistrationSerializer

class RegistrationAPIView(CreateAPIView):
    """
    Allow any user (authenticated or not) to access this endpoint
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = self.request.data
        
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_data = {"token": Token.objects.get(user=user).key, "username": user.username}
        
        return Response(response_data, status=status.HTTP_201_CREATED)
