from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from analytics.signals import object_viewed_signal
# Create your models here.

User = get_user_model()

class ObjectViewed(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
	c_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
	object_id = models.PositiveIntegerField(null=True, blank=True)
	content_object = GenericForeignKey('c_type', 'object_id')
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.content_object} viewed on {self.timestamp} by {self.user}'

def object_viewed_receiver(sender, instance, request, *args, **kwargs):
	print(sender)
	print(instance)
	print(request)
	print(request.user)
	c_type = ContentType.objects.get_for_model(sender)
	user = None
	if request.user.is_authenticated:
		user = User.objects.get(username=request.user)
	
	new_view_obj = ObjectViewed.objects.create(
		user = user,
		c_type = c_type,
		object_id = instance.id,
		)
object_viewed_signal.connect(object_viewed_receiver)