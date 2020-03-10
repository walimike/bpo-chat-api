from django.urls import path

from .views import RegistrationAPIView, HelloView

urlpatterns = [
    path('user/', RegistrationAPIView.as_view()),
    path('hello/', HelloView.as_view()),
]