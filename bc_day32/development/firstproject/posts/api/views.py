from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from posts.models import Post
from posts.api.serializers import PostSerializer

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostUpdateAPIView(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class SearchAPIView(ListAPIView):
	def get_queryset(self):
		query = self.request.GET.get('searchResult')
		queryset = Post.objects.filter(title__icontains=query)
		return queryset
	serializer_class = PostSerializer