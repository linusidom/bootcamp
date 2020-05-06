from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

# Create your models here.
class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.SET_NULL, null=True)
	message = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.post.title