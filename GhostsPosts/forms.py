from django import forms
from django.forms import ModelForm
from .models import Post, Boast

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','content']

class BoastForm(ModelForm):
    class Meta:
        model = Boast
        fields = ['title','author','content']