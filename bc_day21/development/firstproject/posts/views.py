from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from posts.models import Post
from posts.forms import PostForm
# Create your views here.

# class PostListView(ListView):
# 	model = Post

def post_list(request):
	posts = Post.objects.all()
	# print('Post QuerySet', posts)
	context = {
		'post_list': posts,
		'Another_Variable': 'This is a test'
	}
	# print('Context Dictionary' ,context)

	# render_method = render(request, 'posts/post_list.html', context)
	# reverse_method = reverse('posts:post_list')
	# redirect_method = redirect('posts:post_list')
	# reverse_lazy_method = reverse_lazy('posts:post_list')
	# print('\nRender Method\n',render_method, type(render_method))
	# print('\nReverse Method\n',reverse_method, type(reverse_method))
	# print('\nRedirect Method\n',redirect_method, type(redirect_method))
	# print('\nReverse_lazy Method\n',reverse_lazy_method, type(reverse_lazy_method))

	# With Function based views if we want to
	# return an actual web template we should 
	# use the Render method

	return render(request, 'posts/post_list.html', context)

# class PostDetailView(DetailView):
# 	model = Post

def post_detail(request, pk):
	posts = Post.objects.get(pk=pk)
	print('Post', posts)
	context = {
		'post': posts,
		'Another_Variable': 'This is a test'
	}
	print(context)
	return render(request, 'posts/post_detail.html', context)


# class PostCreateView(CreateView):
# 	model = Post
# 	form_class = PostForm


def post_create(request):
	# print(request.method) # GET and POST
	# print(request.POST)
	if request.method == 'POST':
		form = PostForm(request.POST)
		# print('\nForm Before Save\n', form)
		# print('Form Saved', form.save(commit=False))
		post = form.save(commit=False)
		post.save()
		print('\nPrint Form after Save\n', post)
		return redirect(post)
	else:
		context = {
			'form': PostForm()
		}
		return render(request, 'posts/post_form.html', context)

# class PostUpdateView(UpdateView):
# 	model = Post
# 	form_class = PostForm

def post_update(request, pk):
	# print(request.method) # GET and POST
	post = Post.objects.get(pk=pk)
	# print(request.POST)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		# print('\nForm Before Save\n', form)

		# print('Form Saved', form.save(commit=False))
		post = form.save(commit=False)
		post.save()
		print('\nPrint Form after Save\n', post)
		return redirect(post)

	else:
		context = {
			'form': PostForm(instance=post)
		}
		return render(request, 'posts/post_form.html', context)

# class PostDeleteView(DeleteView):
# 	model = Post
# 	success_url = reverse_lazy('posts:post_list')

def post_delete(request, pk):
	post = Post.objects.get(pk=pk)
	# print('Post', posts)
	if request.method == 'POST':
		post.delete()
		return redirect('posts:post_list')
	else:
		context = {
			'post': post,
			'Another_Variable': 'This is a test'
		}

		return render(request, 'posts/post_confirm_delete.html', context)
