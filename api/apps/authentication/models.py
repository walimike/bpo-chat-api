from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.db import models


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, password=None):
        """Create and return a `User` with an email, username and password."""

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser):

    username = models.CharField( max_length=255, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()
