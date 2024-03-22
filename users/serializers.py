from rest_framework import serializers
from .models import UserModel

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password', 'is_staff', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

# class SettingsSerializer(serializers.Serializer):
#     authjwt_secret_key = serializers.CharField(default='47ef36f32028d591a0dc4653bcdac33de4da10cc4e96d83637759374346ca92a')