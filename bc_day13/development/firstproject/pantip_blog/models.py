from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=100, null=True)
	message = models.TextField(null=True)

	def __str__(self):
		return self.title