from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.views.generic import ListView, CreateView 
from django.urls import reverse_lazy 

from .form import PostForm

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')