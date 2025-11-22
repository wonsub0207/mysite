from django.urls import path
from .views import PhotoListView, PhotoDetailView, PhotoCreateView

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('upload/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
]