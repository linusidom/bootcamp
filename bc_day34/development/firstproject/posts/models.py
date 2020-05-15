from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from posts.utils import unique_or_not
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	author = models.CharField(max_length=100, null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return f'{self.id}. {self.title}'

	def get_absolute_url(self):
		return reverse('posts:post_detail', kwargs={'pk': self.pk})

# We want to add a slug to any new object
# @receiver(pre_save, sender=Post)
def pre_save_slug_field(sender, instance, *args, **kwargs):
	print('Sender',sender)
	print('Instance',instance)
	print('Args',args)
	print('Kwargs',kwargs)

	# If we don't have a slug field we want to create one
	if not instance.slug:
		# This is not a Slug
		# instance.slug = 'This is a Slug'

		# This_is_a_Slug
		# instance.slug = 'This_is_a_Slug'

		instance.slug = unique_or_not(instance)
pre_save.connect(pre_save_slug_field, sender=Post)










