from django.urls import path
from .views import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoDeleteView

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('upload/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]