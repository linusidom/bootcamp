from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	weight = models.PositiveIntegerField()

	def __str__(self):
		
		return self.user.username