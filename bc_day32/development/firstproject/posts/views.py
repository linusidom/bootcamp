from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post
from posts.forms import PostForm
# Create your views here.


class PostListView(ListView):
	model = Post

	def get_context_data(self):
		context = super(PostListView, self).get_context_data()
		context['form'] = PostForm
		return context

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


def search_view(request):
	query = request.GET.get('searchQuery')
	print('Query',query)
	queryset = Post.objects.filter(title__icontains= query)
	print(queryset)
	context = {
		'post_list':queryset
	}
	return render(request, 'posts/search_result.html', context)













