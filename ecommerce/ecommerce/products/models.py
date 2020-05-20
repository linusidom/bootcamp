from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from products.utils import unique_slug_gen
# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
	image = models.ImageField(upload_to='products')
	timestamp = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True, null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('products:product_detail', kwargs={'slug':self.slug})

def pre_save_slug_field(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_gen(instance)

pre_save.connect(pre_save_slug_field, sender=Product)