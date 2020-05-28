from django.db import models
from billing.models import BillingProfile

# Create your models here.

ADD_TYPE = (('shipping','Shipping'),('billing','Billing'))

class Address(models.Model):
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True, blank=True)
	address_type = models.CharField(max_length=100, null=True, blank=True, choices=ADD_TYPE)
	address = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return str(self.address)

	def get_address(self):
		return self.address
