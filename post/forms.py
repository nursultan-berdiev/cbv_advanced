from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'date_posted')
        widgets = {'date_posted': forms.DateInput(attrs={'type': 'date'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {'date_posted': forms.DateInput(attrs={'type': 'date'})}