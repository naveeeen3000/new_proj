from django import forms
from blog.models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','text')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','text')
        
