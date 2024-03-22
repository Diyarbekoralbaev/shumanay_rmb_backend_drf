from django.urls import path
from .views import *

urlpatterns = [
    path('history/', SHRMBHistoryView.as_view(), name='history'),
    path('history/<pk>/', SHRMBHistoryDetailView.as_view(), name='history-detail'),

    path('admission/', SHRMBAdmissionView.as_view(), name='admission'),
    path('admission/<pk>/', SHRMBAdmissionDetailView.as_view(), name='admission-detail'),

    path('doctors/', SHRMBDoctorsView.as_view(), name='doctors'),
    path('doctors/<pk>/', SHRMBDoctorsDetailView.as_view(), name='doctors-detail'),

    path('departments/', SHRMBDepartmentView.as_view(), name='departments'),
    path('departments/<pk>/', SHRMBDepartmentDetailView.as_view(), name='departments-detail'),

    path('vacancies/', SHRMBVacanciesView.as_view(), name='vacancies'),
    path('vacancies/<pk>/', SHRMBVacanciesDetailView.as_view(), name='vacancies-detail'),
]
