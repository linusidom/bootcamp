from django.shortcuts import render
from  django.views.generic import ListView, DetailView
from firstapp.models import Blog

# Create your views here.

class BlogListView(ListView):
	# BlogListView is missing a QuerySet
	
	'''
	Method 1 - Just Define the Model
	'''
	# Define BlogListView.model, 
	# model = Blog
	
	# Pulls Data From the Database

	# Returns blog_list or object_list (list Element)
	# context_object_name = 'my_list'


	# Requires blog_list.html
	# template_name = 'firstapp/index.html'

	'''
	Method 2 - Queryset
	'''
	# BlogListView.queryset, or 
	# queryset = Blog.objects.filter(pk=1)
	
	# for query in queryset:
	# 	print(query.title)
	# print('Type of QuerySet on all Response', type(queryset))
	# BlogListView requires either a 'template_name' attribute or a get_queryset() method that returns a QuerySet.
	
	# All, Filter Returns queryset
	# Get returns the Object itself 
	
	# Returns blog_list or object_list (list Element)
	# context_object_name = 'my_list'


	# Requires blog_list.html
	# template_name = 'firstapp/index.html'


	'''
	Method 3
	'''
	# override BlogListView.get_queryset().
	def get_queryset(self):
		queryset = Blog.objects.all()
		return queryset

	# Returns blog_list or object_list (list Element)
	# context_object_name = 'my_list'


	# Requires blog_list.html
	# template_name = 'firstapp/index.html'

	def get_context_data(self):
		context = super(BlogListView, self).get_context_data()
		context['comments'] = ['Comment 1', 'Comment 2']
		return context

class BlogDetailView(DetailView):
	# model = Blog

	'''
	Method 2 - Queryset
	'''
	# BlogListView.queryset, or 
	queryset = Blog.objects.all()

	# Calls get_objects and passes the pk
	def get_object(self, *args, **kwargs):
		# Can change PK number here however you see fit
		data = Blog.objects.get(pk=1)
		return data


	# Need to have **kwargs at the end
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comments'] = ['Comment 1', 'Comment 2']
		return context
	




