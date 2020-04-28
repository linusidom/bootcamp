from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	author = models.CharField(max_length=100, null=True, blank=True)
	message = models.TextField(null=True, blank=True)

	def __str__(self):
		return f'{self.id}. {self.title}'

	def get_absolute_url(self):
		return reverse('posts:post_detail', kwargs={'pk':self.pk})
