from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView 


from .serializers import RegistrationSerializer
from .models import User

class RegistrationAPIView(ListCreateAPIView):
    """
    Allow any user (authenticated or not) to access this endpoint
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request):
        user = self.request.data
        
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        response_data = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
        
        return Response(response_data, status=status.HTTP_201_CREATED)
   
class HelloView(APIView):
    permission_classes = (AllowAny,)             

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)