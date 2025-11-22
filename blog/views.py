from django.views.generic import ListView, DetailView,CreateView
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