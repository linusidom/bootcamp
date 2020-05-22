from django import forms
from django.contrib.auth import login, logout, authenticate, get_user_model

User = get_user_model()

class GuestForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))



class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))

	def clean_username(self, *args, **kwargs):
		cleaned_data = super(LoginForm, self).clean(*args, **kwargs)
		username = cleaned_data.get('username')
		password = self.data.get('password')
		# password = cleaned_data.get('password')
		print(username, password)
		user = authenticate(username=username, password=password)
		print('authenticated', user)
		if not user:
			raise forms.ValidationError('Invalid Login')
		return username

class SignupForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))

	def clean_username(self, *args, **kwargs):
		cleaned_data = super(SignupForm, self).clean(*args, **kwargs)
		username = cleaned_data.get('username')
		qs = User.objects.filter(username=username).exists()
		if qs:
			raise forms.ValidationError('Username is Taken')
		return username

	def clean(self, *args, **kwargs):
		cleaned_data = super(SignupForm, self).clean(*args, **kwargs)
		password2 = cleaned_data.get('password2')
		password = cleaned_data.get('password')
		if password != password2:
			raise forms.ValidationError('Passwords Must Match!')
		return cleaned_data
