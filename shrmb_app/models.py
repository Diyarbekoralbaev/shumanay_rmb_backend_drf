from django.db import models
from shared.models import BaseModel


class SHRMBHistoryModel(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'SHRMB History'
        verbose_name_plural = 'SHRMB Histories'

    def __str__(self):
        return self.title


class SHRMBAdmissionModel(BaseModel):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'SHRMB Admission'
        verbose_name_plural = 'SHRMB Admissions'

    def __str__(self):
        return self.full_name


class SHRMBDoctorsModel(BaseModel):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'SHRMB Doctor'
        verbose_name_plural = 'SHRMB Doctors'

    def __str__(self):
        return self.full_name


class SHRMBDepartmentModel(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = 'SHRMB Department'
        verbose_name_plural = 'SHRMB Departments'

    def __str__(self):
        return self.title


class SHRMBVacanciesModel(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = 'SHRMB Vacancy'
        verbose_name_plural = 'SHRMB Vacancies'

    def __str__(self):
        return self.title

