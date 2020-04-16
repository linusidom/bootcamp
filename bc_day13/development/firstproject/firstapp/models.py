from django.db import models

# Create your models here.
# Inheritance - Book is an object of type models.Model
class Book(models.Model):
	title = models.CharField(max_length=100, null=True)
	author = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.title

