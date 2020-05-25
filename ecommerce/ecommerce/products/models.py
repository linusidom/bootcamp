from django.db import models
from django.db.models.signals import pre_save
from products.utils import unique_slug_gen
# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	description = models.CharField(max_length=100, null=True, blank=True)
	price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(unique=True, blank=True, null=True)
	def __str__(self):
		return self.title

def pre_save_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_gen(instance)

pre_save.connect(pre_save_slug, sender=Product)
