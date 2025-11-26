from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '이름', 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'placeholder': '댓글을 입력하세요', 'rows': 3, 'class': 'form-control'}),
        }
