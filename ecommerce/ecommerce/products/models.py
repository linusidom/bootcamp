from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	description = models.CharField(max_length=100, null=True, blank=True)
	price = models.DecimalField(max_digits=20, decimal_places=2, default=300)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title
