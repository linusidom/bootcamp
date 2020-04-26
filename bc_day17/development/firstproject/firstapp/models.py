from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	author = models.CharField(max_length=100, null=True, blank=True)
	message= models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title

	# null = True/False
	 # - Database will either require (True) before saving or not (False)

	# Blank = True/False
	 # - Webpage Form will either Require this (True) before submitting or not (False)