from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    password2 = serializers.CharField(
        style = {'input_style':'password'},
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def save(self):
        user = User(
            email = self.validated_data["email"],
            username = self.validated_data["username"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError(
                {"password": "Passwords must much"}
            )

        user.set_password(password)
        user.save()
        return user