from django.shortcuts import render
from django.views.generic import (ListView, DetailView,
								CreateView, UpdateView, DeleteView)
# Create your views here.
from firstapp.models import Blog
from django.urls import reverse_lazy

# def Blog_List_View():
# 	pass

class BlogListView(ListView):
	# BlogListView is missing a QuerySet

	# Define BlogListView.model
	model = Blog

	# BlogListView.queryset
	# override BlogListView.get_queryset().

class BlogDetailView(DetailView):
	# BlogDetailView is missing a QuerySet

	# Define BlogDetailView.model
	model = Blog
	# BlogDetailView.queryset

	# override BlogDetailView.get_queryset().

	# Generic detail view BlogDetailView must be called with either
	# object pk - Number
	# or a slug - String
	# in the URLconf.


class BlogCreateView(CreateView):
	# BlogCreateView is missing a QuerySet. 
	# Define BlogCreateView.model, 
	model = Blog

	# Using ModelFormMixin (base class of BlogCreateView) 
	# without the 'fields' attribute is prohibited.
	fields = ['title','author','message']

	# No URL to redirect to.  Either provide a url or 
	# define a get_absolute_url method on the Model.
	success_url = reverse_lazy('firstapp:index')


	# BlogCreateView.queryset, or 
	# override BlogCreateView.get_queryset().

class BlogUpdateView(UpdateView):
	# BlogUpdateView is missing a QuerySet. 
	
	# Define BlogUpdateView.model,
	model = Blog


	# BlogUpdateView.queryset, or 
	# override BlogUpdateView.get_queryset().

	# Generic detail view BlogUpdateView must be called with 
	# either an object pk  - Number
	# or a slug - String
	# in the URLconf.

	# Using ModelFormMixin (base class of BlogUpdateView) 
	# without the 'fields' attribute is prohibited.
	fields = ['title','author','message']

	# No URL to redirect to.  Either provide a url or 
	# define a get_absolute_url method on the Model.
	success_url = reverse_lazy('firstapp:index')	

class BlogDeleteView(DeleteView):
	model = Blog
	success_url = reverse_lazy('firstapp:index')	





