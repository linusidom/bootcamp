import random
from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save

from products.utils import unique_slug_generator
# Create your models here.	


class Product(models.Model):
	title           = models.CharField(max_length=120)
	slug            = models.SlugField(blank=True, unique=True)
	description     = models.TextField()
	price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	image           = models.ImageField(upload_to='products', null=True, blank=True)
	featured        = models.BooleanField(default=False)
	active          = models.BooleanField(default=True)
	timestamp       = models.DateTimeField(auto_now_add=True)
	is_digital      = models.BooleanField(default=False) # User Library

	

	def __str__(self):
		return self.title

	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Product._meta.fields]


def pre_save_slug_field(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_slug_field, sender=Product)
