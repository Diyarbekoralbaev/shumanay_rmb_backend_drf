from django.db import models
import uuid
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


STATUS_CHOICES = (
    ('active', _('Active')),
    ('draft', _('Draft')),
)


class BaseModel(models.Model):
    id = models.TextField(primary_key=True, default=str(uuid.uuid4()).replace('-', ''), editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
        return self

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
        self.save()
        return self


