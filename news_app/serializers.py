# serializers.py
from rest_framework import serializers
from .models import NewsModel


class NewsSerializer(serializers.ModelSerializer):

    def validate_image(self, value):
        if value.size > 1024 * 1024*10:
            raise serializers.ValidationError('Image size should be less than 10MB')
        ex = value.name.split('.')[-1]
        if ex not in ['jpg', 'jpeg', 'png']:
            raise serializers.ValidationError('Image format should be jpg, jpeg or png')
        return value

    class Meta:
        model = NewsModel
        fields = ['id', 'title', 'subtitle', 'description', 'image', 'created_at', 'updated_at', 'status']