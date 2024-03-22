from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)