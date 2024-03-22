# urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('<pk>/', NewsDetailView.as_view(), name='news-detail'),
]