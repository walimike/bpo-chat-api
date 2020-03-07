from django.urls import path

from .views import RegistrationAPIView

urlpatterns = [
    path('user/', RegistrationAPIView.as_view()),
]