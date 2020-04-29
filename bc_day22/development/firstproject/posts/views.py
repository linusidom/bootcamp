from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PostListView(ListView):
	model = Post

	# def get_queryset(self):
	# 	return Post.objects.filter(user=self.request.user)

class PostDetailView(DetailView):
	model = Post

	# def get_queryset(self):
	# 	return Post.objects.filter(user=self.request.user, pk=self.kwargs['pk'])

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm

	def form_valid(self, form):
		print(self.request.user, type(self.request.user), dir(self.request), type(self.request.user.username))
		form.instance.user = self.request.user
		form.instance.author = self.request.user.username
		form.save()
		return super(PostCreateView, self).form_valid(form)	

class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	form_class = PostForm
	
	def get_queryset(self):
		return Post.objects.filter(user=self.request.user, pk=self.kwargs['pk'])

class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = Post

	def get_queryset(self):
		return Post.objects.filter(user=self.request.user, pk=self.kwargs['pk'])

	success_url = reverse_lazy('posts:post_list')