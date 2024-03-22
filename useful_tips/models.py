from django.db import models

from shared.models import BaseModel


class UsefulTipsModel(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = 'Useful Tip'
        verbose_name_plural = 'Useful Tips'

    def __str__(self):
        return self.title
