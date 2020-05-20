from django import forms
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class GuestForm(forms.Form):
	email = forms.CharField(
    label = "",
    widget=forms.TextInput(attrs={'class': 'form-control',
                                  'type': 'email',
                                  'placeholder': 'Email address',
                                  'required': 'true'}))


class LoginForm(forms.Form):
	username = forms.CharField(
    label="", max_length=30, 
    widget=forms.TextInput(attrs={'class': 'form-control',
                            'required': 'true',
                            'placeholder': 'Login'}))

	password = forms.CharField(
    label="",
    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                      'required': 'true',
                                      'placeholder':'Password'}))

class SignupForm(forms.Form):
	username = forms.CharField(
	label = "",
    max_length=30, 
    widget=forms.TextInput(attrs={'class': 'form-control',
                            'required': 'true',
                            'placeholder': 'Username'}))
	email = forms.CharField(
    label = "",
    widget=forms.TextInput(attrs={'class': 'form-control',
                                  'type': 'email',
                                  'placeholder': 'Email address',
                                  'required': 'true'}))
	password = forms.CharField(
	label = "",
	widget=forms.PasswordInput(attrs={'class': 'form-control',
	                                      'required': 'true',
	                                      'placeholder':'Enter Password'}))
	password2 = forms.CharField(
	label = "",
	widget=forms.PasswordInput(attrs={'class': 'form-control',
	                                      'type': 'password',
	                                      'required': 'true',
	                                      'placeholder':'Confirm Password'}))

	def clean_username(self):
		# cleaned_data = super(SignupForm, self).clean()
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username).exists()
		if qs:
			raise forms.ValidationError('Username already exists')
		print(username)
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email).exists()
		if qs:
			raise forms.ValidationError('Email already exists')
		print(email)
		return email


	def clean(self):
		# cleaned_data = super(SignupForm, self).clean()
		# cleaned_data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password and password2 and password != password2:
			raise forms.ValidationError('Passwords must match')
		print(password)
		return password