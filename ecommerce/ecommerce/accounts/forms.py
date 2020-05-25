from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username', 'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':'form-control'}))

	def clean_username(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.data.get('password')
		print(username, password)
		qs = authenticate(username=username, password=password)
		if not qs:
			raise forms.ValidationError('Invalid Login')
		return username

class GuestForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email', 'class':'form-control'}))

class SignupForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username', 'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email', 'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':'form-control'}))

	def clean_username(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError('Invalid Login')
		return username

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('Email in Use, try Forgot Password')
		return email

	def clean(self, *args, **kwargs):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError('Passwords Must Match')
		return password