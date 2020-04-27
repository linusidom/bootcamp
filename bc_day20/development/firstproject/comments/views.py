from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post
from comments.models import Comment
from comments.forms import CommentForm
# Create your views here.


class CommentListView(ListView):
	model = Comment

class CommentDetailView(DetailView):
	model = Comment

class CommentCreateView(CreateView):
	model = Comment
	form_class = CommentForm

	def form_valid(self, form):
		# Get the POST ID from the URL
		post = Post.objects.get(pk=self.kwargs['pk'])

		# DO NOT SAVE THE FORM, but COPY the contents
		comment = form.save(commit=False)

		# UPDATE THE DATA OF THE FORM WITH THE POST ID
		comment.post = post
		return super(CommentCreateView, self).form_valid(form)

class CommentUpdateView(UpdateView):
	model = Comment
	form_class = CommentForm

class CommentDeleteView(DeleteView):
	model = Comment
	def get_success_url(self):
		comment = Comment.objects.get(pk=self.kwargs['pk'])
		return reverse('posts:post_detail', kwargs={'pk':comment.post.id})
	# success_url = reverse_lazy('comments:comment_list')

	
