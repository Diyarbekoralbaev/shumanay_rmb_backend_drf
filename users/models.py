from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
from django.utils import timezone

class UserModel(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class OTPModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    expired_at = models.DateTimeField(auto_created=True, default=datetime.now() + timedelta(minutes=5), blank=True, null=True)

    def __str__(self):
        return self.otp

    def is_expired(self):
        return timezone.now() > self.expired_at

    def is_valid(self, otp):
        return self.otp == otp and not self.is_expired()

