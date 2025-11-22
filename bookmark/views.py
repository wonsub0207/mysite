from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy 
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] 
    success_url = reverse_lazy('list') 
    template_name_suffix = '_create'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    template_name = 'bookmark/bookmark_confirm_delete.html'