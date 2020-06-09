from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=120, null=True, blank=True)
	author = models.CharField(max_length=120, null=True, blank=True)

	def __str__(self):
		if self.title:
			return self.title
		return ""

	def get_absolute_url(self):
		return reverse('books:book_detail', kwargs={'pk':self.pk})
