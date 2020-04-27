from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post
from posts.forms import PostForm
# Create your views here.


class PostListView(ListView):
	model = Post

class PostDetailView(DetailView):
	model = Post

class PostCreateView(CreateView):
	model = Post
	form_class = PostForm

class PostUpdateView(UpdateView):
	model = Post
	form_class = PostForm

class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy('posts:post_list')

	
