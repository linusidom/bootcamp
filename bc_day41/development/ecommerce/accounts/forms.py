from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

	def clean_username(self, *args, **kwargs):
		# cleaned_data = super(SignupForm, self).clean_username(*args, **kwargs)
		username = self.cleaned_data.get('username')
		print('Username From Form', username)
		qs = User.objects.filter(username=username).exists()
		if qs:
			raise forms.ValidationError('Username is already Taken')
		return username

	def clean_email(self, *args, **kwargs):
		# cleaned_data = super(SignupForm, self).clean_email(*args, **kwargs)
		email = self.cleaned_data.get('email')
		print('email From Form', email)
		qs = User.objects.filter(email=email).exists()
		if qs:
			raise forms.ValidationError('Email is already Taken')
		return email

	def clean(self, *args, **kwargs):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError('Passwords Must Match')
		return password

class GuestForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Email'}))
