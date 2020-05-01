from rest_framework import generics
from posts.models import Post
from posts.api.models import PostSerializer

class PostListAPIView(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostRetrieveAPIView(generics.RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer