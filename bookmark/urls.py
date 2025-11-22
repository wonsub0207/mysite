from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDeleteView

urlpatterns = [
    
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name='delete'),
]