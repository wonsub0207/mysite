from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('write/', PostCreateView.as_view(), name='write'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]