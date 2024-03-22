from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import GalleryModel
from .serializers import GallerySerializer
from drf_yasg.utils import swagger_auto_schema

from django.core.cache import cache


class GalleryView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        operation_summary='Get all gallery',
    )
    def get(self, request):
        cached_data = cache.get('gallery')
        if cached_data:
            return Response(cached_data)
        gallery = GalleryModel.objects.all()
        serializer = GallerySerializer(gallery, many=True)
        cache.set('gallery', serializer.data, timeout=60 * 60 * 24)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Create a new gallery',
        request_body=GallerySerializer,
    )
    def post(self, request):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('gallery')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GalleryDetailView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        operation_summary='Get a gallery by id',
    )
    def get(self, request, pk):
        cached_data = cache.get(f'gallery_{pk}')
        if cached_data:
            return Response(cached_data)
        gallery = GalleryModel.objects.get(pk=pk)
        serializer = GallerySerializer(gallery)
        cache.set(f'gallery_{pk}', serializer.data, timeout=60 * 60 * 24)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Update a gallery by id',
        request_body=GallerySerializer,
    )
    def put(self, request, pk):
        gallery = GalleryModel.objects.get(pk=pk)
        serializer = GallerySerializer(gallery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f'gallery_{pk}')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Patch a gallery by id',
        request_body=GallerySerializer,
    )
    def patch(self, request, pk):
        gallery = GalleryModel.objects.get(pk=pk)
        serializer = GallerySerializer(gallery, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            cache.delete('gallery')
            cache.delete(f'gallery_{pk}')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Delete a gallery by id',
    )
    def delete(self, request, pk):
        gallery = GalleryModel.objects.get(pk=pk)
        gallery.delete()
        cache.delete(f'gallery_{pk}')
        cache.delete('gallery')
        return Response(status=status.HTTP_204_NO_CONTENT)