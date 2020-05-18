from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

# Create your models here.
class BillingProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	email = models.EmailField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=True)
	update = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.user.username

def post_save_user_created(sender, instance, created, *args, **kwargs):
	if created:
		BillingProfile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_created, sender=User)