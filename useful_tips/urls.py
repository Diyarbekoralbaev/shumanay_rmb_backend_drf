# urls.py
from django.urls import path
from .views import UsefulTipsView, UsefulTipsDetailView

urlpatterns = [
    path('', UsefulTipsView.as_view()),
    path('<int:pk>/', UsefulTipsDetailView.as_view()),
]
