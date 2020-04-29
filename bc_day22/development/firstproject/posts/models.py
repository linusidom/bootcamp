from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	title = models.CharField(max_length=100, null=True, blank=True)
	author = models.CharField(max_length=100, null=True, blank=True)
	message = models.TextField(null=True, blank=True)

	def __str__(self):
		return f'{self.id}. {self.title}'

	def get_absolute_url(self):
		return reverse('posts:post_detail', kwargs={'pk':self.pk})
