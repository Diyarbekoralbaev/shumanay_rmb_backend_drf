# serializers.py
from rest_framework import serializers
from .models import GalleryModel


class BaseGallerySerializer(serializers.ModelSerializer):
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 10:
            raise serializers.ValidationError('Image size is too large')
        ex = value.name.split('.')[-1]
        if ex not in ['jpg', 'jpeg', 'png']:
            raise serializers.ValidationError('Image format is not supported')
        return value


class GallerySerializer(BaseGallerySerializer):
    class Meta:
        model = GalleryModel
        fields = ['id', 'title', 'description', 'image', 'created_at', 'updated_at', 'status']