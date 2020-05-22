from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from accounts.forms import LoginForm, SignupForm, GuestForm
from accounts.models import GuestEmail
User = get_user_model()

# Create your views here.

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			print(username, password)
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				return redirect('index')
	else:
		form = LoginForm()
	return render(request, 'accounts/user_login.html', {'form':form})

def user_logout(request):
	logout(request)
	return redirect('index')

def user_signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			print('User Pass', username, password)
			user = User.objects.create_user(username=username, email=email, password=password)
			return redirect('accounts:user_login')
	else:
		form = SignupForm()
	return render(request, 'accounts/user_signup.html', {'form':form})

def user_guest(request):
	if request.method == 'POST':
		form = GuestForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			user_guest = GuestEmail.objects.create(email=email)
			request.session['guest_email_id'] = user_guest.id
			return redirect('carts:checkout')
	else:
		form = GuestForm()
	return render(request, 'carts/checkout.html', {'form':form})
