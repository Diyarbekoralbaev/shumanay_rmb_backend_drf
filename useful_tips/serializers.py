from rest_framework import serializers
from .models import UsefulTipsModel


class BaseUsefulTipsSerializer(serializers.ModelSerializer):
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 10:
            raise serializers.ValidationError('The image size is too large. It must be less than 10 MB.')
        ext = value.name.split('.')[-1].lower()
        if ext not in ['jpg', 'jpeg', 'png']:
            raise serializers.ValidationError('The image format is not supported. It must be jpg, jpeg or png.')
        return value


class UsefulTipsSerializer(BaseUsefulTipsSerializer):
    class Meta:
        model = UsefulTipsModel
        fields = ['id', 'title', 'description', 'image', 'created_at', 'updated_at', 'status']