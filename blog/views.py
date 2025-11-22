from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
 
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']  
    template_name = 'blog/post_create.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('list')
    template_name = 'blog/post_confirm_delete.html'