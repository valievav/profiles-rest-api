from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    """

    def create_user(self, email, name, password=None):
        """
        Create new user profile
        """
        if not email:
            raise ValueError('Please provide an email address')

        email = self.normalize_email(email)  # lowercasing domain part only (first part can be case sensitive)
        user = self.model(email=email, name=name)

        user.set_password(password)  # encrypting and storing as a hash (function is part of the AbstractBaseUser)
        user.save(using=self._db)  # to support multiple db

        return user

    def create_superuser(self, email, name, password):
        """
        Create new superuser profile
        """
        user = self.create_user(email, name, password)

        user.is_superuser = True  # automatically created by PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database models for users
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Return user full name
        """
        return self.name

    def get_short_name(self):
        """
        Return user short name
        """
        return self.name

    def __str__(self):
        """
        Return string representation of user
        """
        return self.email


class ProfileFeedItem(models.Model):
    """
    Profile status update
    """
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return model as a string
        """
        return self.status_text
