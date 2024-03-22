from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import DocumentsModel
from .serializers import DocumentSerializer
from drf_yasg.utils import swagger_auto_schema

from django.core.cache import cache


class DocumentsView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        operation_summary='Get all documents',
    )
    def get(self, request):
        cached_documents = cache.get('documents')
        if cached_documents:
            return Response(cached_documents)
        documents = DocumentsModel.objects.all()
        serializer = DocumentSerializer(documents, many=True)

        cache.set('documents', serializer.data, timeout=60*60*24)

        return Response(serializer.data)


    @swagger_auto_schema(
        operation_summary='Create a new document',
        request_body=DocumentSerializer,
    )
    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('documents') # delete the cached list of documents
            print("cached deleted for all documents")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentsDetailView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        operation_summary='Get a document by id',
    )
    def get(self, request, pk):
        cached_document = cache.get(f'document-{pk}')
        if cached_document:
            return Response(cached_document)
        document = DocumentsModel.objects.get(pk=pk)
        serializer = DocumentSerializer(document)
        cache.set(f'document-{pk}', serializer.data, timeout=60*60*24)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Update a document by id',
        request_body=DocumentSerializer,
    )
    def put(self, request, pk):
        document = DocumentsModel.objects.get(pk=pk)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('documents') # delete the cached list of documents
            cache.delete(f'document-{pk}') # delete the cached single document
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Delete a document by id',
    )
    def delete(self, request, pk):
        document = DocumentsModel.objects.get(pk=pk)
        document.delete()
        cache.delete('documents')
        cache.delete(f'document-{pk}')
        return Response(status=status.HTTP_204_NO_CONTENT)