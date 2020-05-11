from rest_framework.generics import ListAPIView, RetrieveAPIView
from posts.models import Post
from posts.api.serializers import PostSerializer

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
