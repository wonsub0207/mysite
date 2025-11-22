from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Photo

class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

class PhotoCreateView(CreateView):
    model = Photo
    fields = ['title', 'author', 'image', 'description']
    template_name = 'photo/photo_create.html'
   
    success_url = reverse_lazy('photo_list')

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo_list')
    template_name = 'photo/photo_confirm_delete.html'