from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.api.serializers import PostSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostRetrieveAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostCreateAPIView(CreateAPIView):
	serializer_class = PostSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class PostUpdateAPIView(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [IsAuthenticated]

	def perform_update(self, serializer):
		user = User.objects.get(username=self.request.user)
		post = Post.objects.get(pk=self.kwargs['pk'])
		print(user.id, post.user.id)
		if user.id == post.user.id:
			instance = serializer.save()

class PostDestroyAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	permission_classes = [IsAuthenticated]

	def perform_destroy(self, instance):
		user = User.objects.get(username=self.request.user)
		post = Post.objects.get(pk=self.kwargs['pk'])
		print(user.id, post.user.id)
		if user.id == post.user.id:
			instance.delete()




