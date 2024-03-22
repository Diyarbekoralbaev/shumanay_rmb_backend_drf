from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SHRMBHistoryModel, SHRMBAdmissionModel, SHRMBDoctorsModel, SHRMBDepartmentModel, SHRMBVacanciesModel
from .serializers import SHRMBHistorySerializer, SHRMBAdmissionSerializer, SHRMBDoctorsSerializer, \
    SHRMBDepartmentSerializer, SHRMBVacanciesSerializer
from drf_yasg.utils import swagger_auto_schema

from django.core.cache import cache


class SHRMBHistoryView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB History'],
        request_body=SHRMBHistorySerializer,
    )
    def post(self, request):
        serializer = SHRMBHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('history')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB History'],
    )
    def get(self, request):
        cached_data = cache.get('history')
        if cached_data:
            return Response(cached_data)
        histories = SHRMBHistoryModel.objects.all()
        serializer = SHRMBHistorySerializer(histories, many=True)
        cache.set('history', serializer.data, timeout=60 * 60 * 24)
        return Response(serializer.data)


class SHRMBHistoryDetailView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB History'],
    )
    def get(self, request, pk):
        try:
            cached_data = cache.get(f'history_{pk}')
            if cached_data:
                return Response(cached_data)
            history = SHRMBHistoryModel.objects.get(id=pk)
            serializer = SHRMBHistorySerializer(history)
            cache.set(f'history_{pk}', serializer.data, timeout=60 * 60 * 24)
            return Response(serializer.data)
        except SHRMBHistoryModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['SHRMB History'],
        request_body=SHRMBHistorySerializer,
    )
    def put(self, request, pk):
        history = SHRMBHistoryModel.objects.get(id=pk)
        serializer = SHRMBHistorySerializer(instance=history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('history')
            cache.delete(f'history_{pk}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB History'],
    )
    def delete(self, request, pk):
        try:
            history = SHRMBHistoryModel.objects.get(id=pk)
            history.delete()
            cache.delete('history')
            cache.delete(f'history_{pk}')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SHRMBHistoryModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SHRMBAdmissionView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB Admission'],
        request_body=SHRMBAdmissionSerializer,
    )
    def post(self, request):
        serializer = SHRMBAdmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('admission')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB Admission'],
    )
    def get(self, request):
        cached_data = cache.get('admission')
        if cached_data:
            return Response(cached_data)
        admissions = SHRMBAdmissionModel.objects.all()
        serializer = SHRMBAdmissionSerializer(admissions, many=True)
        cache.set('admission', serializer.data, timeout=60 * 60 * 24)
        return Response(serializer.data)


class SHRMBAdmissionDetailView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB Admission'],
    )
    def get(self, request, pk):
        try:
            cached_data = cache.get(f'admission_{pk}')
            if cached_data:
                return Response(cached_data)
            admission = SHRMBAdmissionModel.objects.get(id=pk)
            serializer = SHRMBAdmissionSerializer(admission)
            cache.set(f'admission_{pk}', serializer.data, timeout=60 * 60 * 24)
            return Response(serializer.data)
        except SHRMBAdmissionModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['SHRMB Admission'],
        request_body=SHRMBAdmissionSerializer,
    )
    def put(self, request, pk):
        admission = SHRMBAdmissionModel.objects.get(id=pk)
        serializer = SHRMBAdmissionSerializer(instance=admission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('admission')
            cache.delete(f'admission_{pk}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB Admission'],
    )
    def delete(self, request, pk):
        try:
            admission = SHRMBAdmissionModel.objects.get(id=pk)
            admission.delete()
            cache.delete('admission')
            cache.delete(f'admission_{pk}')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SHRMBAdmissionModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SHRMBDoctorsView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB Doctors'],
        request_body=SHRMBDoctorsSerializer,
    )
    def post(self, request):
        serializer = SHRMBDoctorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('doctors')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB Doctors'],
    )
    def get(self, request):
        cached_data = cache.get('doctors')
        if cached_data:
            return Response(cached_data)
        doctors = SHRMBDoctorsModel.objects.all()
        serializer = SHRMBDoctorsSerializer(doctors, many=True)
        cache.set('doctors', serializer.data, timeout=60 * 60 * 24)
        return Response(serializer.data)


class SHRMBDoctorsDetailView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB Doctors'],
    )
    def get(self, request, pk):
        try:
            cached_data = cache.get(f'doctors_{pk}')
            if cached_data:
                return Response(cached_data)
            doctor = SHRMBDoctorsModel.objects.get(id=pk)
            serializer = SHRMBDoctorsSerializer(doctor)
            cache.set(f'doctors_{pk}', serializer.data, timeout=60 * 60 * 24)
            return Response(serializer.data)
        except SHRMBDoctorsModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['SHRMB Doctors'],
        request_body=SHRMBDoctorsSerializer,
    )
    def put(self, request, pk):
        doctor = SHRMBDoctorsModel.objects.get(id=pk)
        serializer = SHRMBDoctorsSerializer(instance=doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('doctors')
            cache.delete(f'doctors_{pk}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB Doctors'],
    )
    def delete(self, request, pk):
        try:
            doctor = SHRMBDoctorsModel.objects.get(id=pk)
            doctor.delete()
            cache.delete('doctors')
            cache.delete(f'doctors_{pk}')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SHRMBDoctorsModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SHRMBDepartmentView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB Department'],
        request_body=SHRMBDepartmentSerializer,
    )
    def post(self, request):
        serializer = SHRMBDepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('department')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB Department'],
    )
    def get(self, request):
        cached_data = cache.get('department')
        if cached_data:
            return Response(cached_data)
        departments = SHRMBDepartmentModel.objects.all()
        serializer = SHRMBDepartmentSerializer(departments, many=True)
        cache.set('department', serializer.data, timeout=60 * 60 * 24)
        return Response(serializer.data)


class SHRMBDepartmentDetailView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB Department'],
    )
    def get(self, request, pk):
        try:
            cached_data = cache.get(f'department_{pk}')
            if cached_data:
                return Response(cached_data)
            department = SHRMBDepartmentModel.objects.get(id=pk)
            serializer = SHRMBDepartmentSerializer(department)
            cache.set(f'department_{pk}', serializer.data, timeout=60 * 60 * 24)
            return Response(serializer.data)
        except SHRMBDepartmentModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['SHRMB Department'],
        request_body=SHRMBDepartmentSerializer,
    )
    def put(self, request, pk):
        department = SHRMBDepartmentModel.objects.get(id=pk)
        serializer = SHRMBDepartmentSerializer(instance=department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('department')
            cache.delete(f'department_{pk}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB Department'],
    )
    def delete(self, request, pk):
        try:
            department = SHRMBDepartmentModel.objects.get(id=pk)
            department.delete()
            cache.delete('department')
            cache.delete(f'department_{pk}')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SHRMBDepartmentModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SHRMBVacanciesView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB Vacancies'],
        request_body=SHRMBVacanciesSerializer,
    )
    def post(self, request):
        serializer = SHRMBVacanciesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('vacancies')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB Vacancies'],
    )
    def get(self, request):
        cached_data = cache.get('vacancies')
        if cached_data:
            return Response(cached_data)
        vacancies = SHRMBVacanciesModel.objects.all()
        serializer = SHRMBVacanciesSerializer(vacancies, many=True)
        cache.set('vacancies', serializer.data, timeout=60 * 60 * 24)
        return Response(serializer.data)


class SHRMBVacanciesDetailView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @swagger_auto_schema(
        tags=['SHRMB Vacancies'],
    )
    def get(self, request, pk):
        try:
            cached_data = cache.get(f'vacancies_{pk}')
            if cached_data:
                return Response(cached_data)
            vacancy = SHRMBVacanciesModel.objects.get(id=pk)
            serializer = SHRMBVacanciesSerializer(vacancy)
            cache.set(f'vacancies_{pk}', serializer.data, timeout=60 * 60 * 24)
            return Response(serializer.data)
        except SHRMBVacanciesModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=['SHRMB Vacancies'],
        request_body=SHRMBVacanciesSerializer,
    )
    def put(self, request, pk):
        vacancy = SHRMBVacanciesModel.objects.get(id=pk)
        serializer = SHRMBVacanciesSerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('vacancies')
            cache.delete(f'vacancies_{pk}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['SHRMB Vacancies'],
    )
    def delete(self, request, pk):
        try:
            vacancy = SHRMBVacanciesModel.objects.get(id=pk)
            vacancy.delete()
            cache.delete('vacancies')
            cache.delete(f'vacancies_{pk}')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SHRMBVacanciesModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
