from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import NewsModel
from .serializers import NewsSerializer
from drf_yasg.utils import swagger_auto_schema

from django.core.cache import cache


class NewsView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        operation_summary='Get all news',
    )
    def get(self, request):
        cached_data = cache.get('news')
        if cached_data:
            return Response(cached_data)
        news = NewsModel.objects.all()
        serializer = NewsSerializer(news, many=True)
        cache.set('news', serializer.data, timeout=60 * 60 * 24)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Create a new news',
        request_body=NewsSerializer,
    )
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('news')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        operation_summary='Get a news by id',
    )
    def get(self, request, pk):
        cached_data = cache.get(f'news_{pk}')
        if cached_data:
            return Response(cached_data)
        news = NewsModel.objects.get(pk=pk)
        serializer = NewsSerializer(news)
        cache.set(f'news_{pk}', serializer.data, timeout=60 * 60 * 24)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Update a news by id',
        request_body=NewsSerializer,
    )
    def put(self, request, pk):
        news = NewsModel.objects.get(pk=pk)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f'news_{pk}')
            cache.delete('news')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Patch a news by id',
        request_body=NewsSerializer,
    )
    def patch(self, request, pk):
        news = NewsModel.objects.get(pk=pk)
        serializer = NewsSerializer(news, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f'news_{pk}')
            cache.delete('news')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Delete a news by id',
    )
    def delete(self, request, pk):
        news = NewsModel.objects.get(pk=pk)
        news.delete()
        cache.delete(f'news_{pk}')
        cache.delete('news')
        return Response(status=status.HTTP_204_NO_CONTENT)
