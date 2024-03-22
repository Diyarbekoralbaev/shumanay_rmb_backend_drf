from .models import SHRMBHistoryModel, SHRMBAdmissionModel, SHRMBDoctorsModel, SHRMBDepartmentModel, SHRMBVacanciesModel
from rest_framework import serializers


class BaseSHRMBSerializer(serializers.ModelSerializer):
    def validate_photo(self, value):
        if value.size > 1024 * 1024 * 10:
            raise serializers.ValidationError('The file size is too large. It must be less than 10 MB.')
        ext = value.name.split('.')[-1].lower()
        if ext not in ['jpg', 'jpeg', 'png']:
            raise serializers.ValidationError('The file format is not supported. It must be jpg, jpeg or png.')
        return value


class SHRMBHistorySerializer(BaseSHRMBSerializer):
    class Meta:
        model = SHRMBHistoryModel
        fields = ['id', 'title', 'description', 'photo', 'created_at', 'updated_at', 'status']


class SHRMBAdmissionSerializer(BaseSHRMBSerializer):
    class Meta:
        model = SHRMBAdmissionModel
        fields = ['id', 'full_name', 'photo', 'info', 'created_at', 'updated_at', 'status']


class SHRMBDoctorsSerializer(BaseSHRMBSerializer):
    class Meta:
        model = SHRMBDoctorsModel
        fields = ['id', 'full_name', 'photo', 'info', 'created_at', 'updated_at', 'status']


class SHRMBDepartmentSerializer(BaseSHRMBSerializer):
    class Meta:
        model = SHRMBDepartmentModel
        fields = ['id', 'title', 'description', 'photo', 'created_at', 'updated_at', 'status']


class SHRMBVacanciesSerializer(BaseSHRMBSerializer):
    class Meta:
        model = SHRMBVacanciesModel
        fields = ['id', 'title', 'description', 'photo', 'created_at', 'updated_at', 'status']
