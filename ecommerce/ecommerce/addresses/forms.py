from django import forms
from addresses.models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		exclude = ['billing_profile', 'user', 'address_type']