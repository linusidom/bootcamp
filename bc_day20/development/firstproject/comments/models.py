from django.db import models
from django.shortcuts import reverse
from posts.models import Post
# Create your models here.

class Comment(models.Model):
	# title = models.CharField(max_length=100, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.CharField(max_length=100, null=True, blank=True)
	message = models.TextField(null=True, blank=True)

	def __str__(self):
		# PK = Primary Key = ID = Identification
		return f'{self.pk} {self.author}'

	def get_absolute_url(self):
		return reverse('posts:post_detail', kwargs={'pk':self.post.pk})
