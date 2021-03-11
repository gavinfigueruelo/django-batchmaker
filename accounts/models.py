from django.db import models
from django.conf import settings
from django.comtrib.auth.models import AbstractUser
from . import TokenSerializer
# Create your models here.

class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'profiles/', null = True)

    def __str__(self):
        return self.user.username
