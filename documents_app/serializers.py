# serializers.py
from rest_framework import serializers
from .models import DocumentsModel


class BaseDocumentSerializer(serializers.ModelSerializer):
    def validate_file(self, value):
        if value.size > 1024 * 1024 * 10:
            raise serializers.ValidationError('The file size is too large. It must be less than 10 MB.')
        ext = value.name.split('.')[-1].lower()
        if ext not in ['pdf', 'doc', 'docx']:
            raise serializers.ValidationError('The file format is not supported. It must be pdf, doc or docx.')
        return value


class DocumentSerializer(BaseDocumentSerializer):
    class Meta:
        model = DocumentsModel
        fields = ['id', 'title', 'description', 'file', 'created_at', 'updated_at', 'status']
