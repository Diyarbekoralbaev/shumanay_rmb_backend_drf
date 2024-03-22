from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UsefulTipsModel
from .serializers import UsefulTipsSerializer
from drf_yasg.utils import swagger_auto_schema


class UsefulTipsView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        operation_summary='Get all useful tips',
    )
    def get(self, request):
        useful_tips = UsefulTipsModel.objects.all()
        serializer = UsefulTipsSerializer(useful_tips, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Create a new useful tip',
        request_body=UsefulTipsSerializer,
    )
    def post(self, request):
        serializer = UsefulTipsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsefulTipsDetailView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        operation_summary='Get a useful tip by id',
    )
    def get(self, request, pk):
        useful_tip = UsefulTipsModel.objects.get(pk=pk)
        serializer = UsefulTipsSerializer(useful_tip)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Update a useful tip by id',
        request_body=UsefulTipsSerializer,
    )
    def put(self, request, pk):
        useful_tip = UsefulTipsModel.objects.get(pk=pk)
        serializer = UsefulTipsSerializer(useful_tip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Delete a useful tip by id',
    )
    def delete(self, request, pk):
        useful_tip = UsefulTipsModel.objects.get(pk=pk)
        useful_tip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)