from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from firstapp.models import Blog
from firstapp.forms import BlogForm
# Create your views here.

class BlogListView(ListView):
	model = Blog

	# Delivers / looks for
	# looks for template firstapp/blog_list.html
	# Delivers list blog_list/object_list = Blog.objects.all()

# Get Users to input Data
class BlogCreateView(CreateView):
	model = Blog
	form_class = BlogForm
	# fields = ['title', 'author', 'message']

	# Delivers /looks for
	# looks for templates firstapp/blog_form.html
	# Delivers list form = BlogForm()

class BlogDetailView(DetailView):
	model = Blog

	# Delivers / looks for
	# looks for template firstapp/blog_detail.html
	# Delivers list blog/object = Blog.objects.get(pk=pk)

class BlogUpdateView(UpdateView):
	model = Blog
	form_class = BlogForm
	# fields = ['title', 'author', 'message']

	# Delivers /looks for
	# looks for templates firstapp/blog_form.html
	# Delivers list form = BlogForm()

class BlogDeleteView(DeleteView):
	model = Blog

	# Delivers /looks for
	# looks for templates firstapp/blog_confirm_delete.html
	# Delivers list blog/object = Blog.objects.get(pk=pk)
	success_url = reverse_lazy('firstapp:blog_list')
