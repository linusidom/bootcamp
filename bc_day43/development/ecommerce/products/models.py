from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10, default=300)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	image = models.ImageField(null=True, blank=True, upload_to='products')
	slug = models.SlugField(unique=True, null=True, blank=True)

	def __str__(self):
		return self.title