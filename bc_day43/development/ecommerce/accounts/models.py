from django.db import models

# Create your models here.

class GuestEmail(models.Model):
	email = models.EmailField(null=True, blank=True)

	def __str__(self):
		return self.email