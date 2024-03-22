from django.urls import path
from .views import GalleryView, GalleryDetailView

urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),
    path('<pk>/', GalleryDetailView.as_view(), name='gallery-detail'),
]
