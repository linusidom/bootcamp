from django.db import models
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	author = models.CharField(max_length=100, null=True, blank=True)
	message = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('firstapp:blog_list')