from django.db import models

# Create your models here.
class Person(models.Model):
	firstName = models.CharField(max_length=100, null=True)
	lastName = models.CharField(max_length=100, null=True)

	def __str__(self):
		return f'Hello {self.firstName} {self.lastName}'
