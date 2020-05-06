from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	title= models.CharField(max_length=100, null=True, blank=True)
	message = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title