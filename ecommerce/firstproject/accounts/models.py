from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyAbstractUser(AbstractUser):
	
	def __str__(self):
		return str(self.username)