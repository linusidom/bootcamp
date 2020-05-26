from django import forms
from addresses.models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		exclude = ['billing_profile', 'address_type']

		widgets = {
			'address': forms.TextInput(attrs={'placeholder':'Enter Address', 'class':'form-control'})
		}
		labels = {
			'address': ''
		}
