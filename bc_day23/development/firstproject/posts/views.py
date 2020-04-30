from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from posts.forms import PostForm

# Create your views here.

class PostListView(ListView):
	model = Post

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post

	def get_queryset(self):
		return Post.objects.filter(user=self.request.user, pk=self.kwargs['pk'])

class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('posts:post_list')
	def get_queryset(self):
		return Post.objects.filter(user=self.request.user, pk=self.kwargs['pk'])












