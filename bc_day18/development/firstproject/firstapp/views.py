from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from firstapp.models import Blog
from firstapp.forms import BlogForm
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(ListView):
	# BlogListView is missing a QuerySet. 
	# Define BlogListView.model, 
	model = Blog

	# gets the queryset (Blog.objects.all())
	# gets the template (firstapp/blog_list.html)
	# , gets the context_data (blog_list)


	# BlogListView.queryset, 
	# override BlogListView.get_queryset().

class BlogCreateView(CreateView):
	model = Blog

	# No queryset for CreateView
	# gets the template (firstapp/blog_form.html)
	# , gets the context_data (form)

	# Using ModelFormMixin (base class of BlogCreateView) 
	# without the 'fields' attribute is prohibited.

	# Unknown field(s) () specified for Blog
	# fields = ['title', 'author', 'message']
	form_class = BlogForm

	# No URL to redirect to.  Either provide a url or 
	# define a get_absolute_url method on the Model.
	# success_url = reverse_lazy('firstapp:index')

	def get_context_data(self, *args, **kwargs):
		context = super(BlogCreateView, self).get_context_data(*args, **kwargs)
		context['page_function'] = 'Create Entry'
		return context

class BlogUpdateView(UpdateView):
	model = Blog

	# get queryset based on PK (Blog.objects.filter(pk=pk))
	# gets the template (firstapp/blog_form.html)
	# , gets the context_data (form)
	# Fills in the form data with the data from the database



	# Pulls data from the database based on PK
	# PK comes from URL request
	# Looks for blog_form.html

	# Passes in the following fields to make the form

	# Form context_object_name is 'form'

	fields = ['title', 'author', 'message']

	# No URL to redirect to.  Either provide a url or 
	# define a get_absolute_url method on the Model.

	def get_context_data(self, *args, **kwargs):
		context = super(BlogUpdateView, self).get_context_data(*args, **kwargs)
		context['page_function'] = 'Update Entry'
		return context

class BlogDeleteView(DeleteView):
	model = Blog

	# gets the queryset (Blog.objects.filter(pk=pk))
	# gets the template (firstapp/blog_confirm_delete.html)
	# , gets the context_data (blog)
	success_url = reverse_lazy('firstapp:index')

	def get_context_data(self, *args, **kwargs):
		context = super(BlogDeleteView, self).get_context_data(*args, **kwargs)
		context['page_function'] = 'Delete Entry'
		return context















