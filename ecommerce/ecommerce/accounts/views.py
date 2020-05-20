from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from accounts.models import GuestEmail
from accounts.forms import LoginForm, SignupForm, GuestForm
# Create your views here.

User = get_user_model()

def user_login(request):
	form = LoginForm(request.POST or None)
	context = {
		'form':form
	}
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(request, username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return redirect('products:product_list')
	return render(request, 'accounts/login.html', context)

def user_logout(request):
	logout(request)
	return redirect('accounts:user_login')

def signup(request):
	form = SignupForm(request.POST or None)
	context = {
		'form':form
	}
	if form.is_valid():
		username = form.data.get('username')
		password = form.data.get('password')
		email = form.data.get('email')
		user = User.objects.create(username=username, email=email, password=password)
		if user:
			login(request, user)
			return redirect('products:product_list')
	return render(request, 'accounts/signup.html', context)


def guest_login(request):
	next_get = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_to = next_get or next_post
	form = GuestForm(request.POST or None)
	context = {
		'form':form
	}
	if form.is_valid():
		email = form.data.get('email')
		guest_user = GuestEmail.objects.create(email=email)
		request.session['guest_email_id'] = guest_user.id
		return redirect(redirect_to)
	return render(request, 'accounts/signup.html', context)
