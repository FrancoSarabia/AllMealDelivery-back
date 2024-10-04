from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from .profile import Profile

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, profile, is_active, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            profile = profile,
            is_active = is_active
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, profile, password=None, **extra_fields):
        return self._create_user(username, email, profile, password, True, **extra_fields)

    def create_superuser(self, username, email, profile, password=None, **extra_fields):
        return self._create_user(username, email, profile, password, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    _id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    username = models.CharField(max_length = 255, unique = True, default='')
    email = models.EmailField(unique=True, default='')
    password = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email