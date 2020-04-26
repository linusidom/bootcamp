from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from firstapp.models import Blog


"""
Function Based Views
- Offers More Flexibilty but have to code everything
"""
def list_view(request):
	posts = Blog.objects.all()
	context = {
		'blog_list': posts,
		'sample_variable': 'I am a extra variable from a function based view'
	}
	return render(request, 'firstapp/index.html', context)


def detail_view(request, pk):
	post = Blog.objects.get(pk=pk)
	context = {
		'blog': post,
	}
	return render(request, 'firstapp/blog_detail.html', context)

"""
Class Based Views
- Offers less flexibilty but more defaults so less coding
"""
class BlogListView(ListView):
	model = Blog

class BlogDetailView(DetailView):
	model = Blog












