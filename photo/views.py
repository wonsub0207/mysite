from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Photo
from .forms import CommentForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = context.get('comment_form') or CommentForm()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = self.object
            comment.save()
            return redirect('photo_detail', pk=self.object.pk)
        context = self.get_context_data(comment_form=form)
        return self.render_to_response(context)

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo_list')
    template_name = 'photo/photo_confirm_delete.html'
