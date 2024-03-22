from django.db import models
from shared.models import BaseModel


class GalleryModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title
