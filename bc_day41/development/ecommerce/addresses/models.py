from django.db import models
from billing.models import BillingProfile
# Create your models here.

ADD_TYPE = (
	('shipping','Shipping'),
	('billing','Billing')
	)

class Address(models.Model):
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True, blank=True)
	address_type = models.CharField(max_length=100, null=True, blank=True, choices=ADD_TYPE)
	address = models.CharField(max_length=100, null=True, blank=True)
	district = models.CharField(max_length=100, null=True, blank=True, default='Bangkok')
	province = models.CharField(max_length=100, null=True, blank=True, default='Bangkok')
	postal_code = models.CharField(max_length=100, null=True, blank=True, default='10260')
	country = models.CharField(max_length=100, null=True, blank=True, default='Thailand')

	def __str__(self):
		return f'{self.address}, {self.district} {self.province} {self.postal_code}, {self.country}'
