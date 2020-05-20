from django.db import models
from billing.models import BillingProfile
from django.contrib.auth import get_user_model

User = get_user_model()


ADD_TYPE = (
	('shipping','Shipping'),
	('billing','Billing'),
	)

class Address(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	billing_profile = models.ForeignKey(BillingProfile,on_delete=models.SET_NULL, null=True, blank=True)
	address_type = models.CharField(max_length=100, null=True, blank=True, choices=ADD_TYPE)
	address_line1 = models.CharField(max_length=100, null=True, blank=True)
	address_line2 = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=100, null=True, blank=True)
	postal_code = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, default='Thailand')

	def __str__(self):
		return str(self.billing_profile.id)

	def get_address(self):
		return f'''{self.address_line1 or ""} {self.address_line2 or ""}
		{self.city or ""} {self.state or ""} {self.postal_code or ""}
		{self.country or ""}'''