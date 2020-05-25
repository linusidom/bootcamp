from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from accounts.forms import LoginForm, GuestForm, SignupForm
from accounts.models import GuestEmail

User = get_user_model()

# Create your views here.

def user_login(request):
	if request.method == 'POST':
		next_post = request.POST.get('next')
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.data.get('username')
			password = form.data.get('password')
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				try:
					del request.session['guest_email_id']
				except:
					pass
				if next_post:
					return redirect(next_post)
				else:
					return redirect('index')
	else:
		form = LoginForm()
	return render(request, 'accounts/user_login.html', {'form':form})

def user_logout(request):
	logout(request)
	return redirect('index')

def user_signup(request):
	if request.method == 'POST':
		next_post = request.POST.get('next')
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.data.get('username')
			email = form.data.get('email')
			password = form.data.get('password')
			user = User.objects.create_user(username=username, email=email, password=password)
			if next_post:
				return redirect(next_post)
			else:
				return redirect('index')
	else:	
		form = SignupForm()
	return render(request, 'accounts/user_signup.html', {'form':form})


def user_guest(request):
	if request.method == 'POST':
		next_post = request.POST.get('next')
		form = GuestForm(request.POST)
		if form.is_valid():
			email = form.data.get('email')
			guestEmail = GuestEmail.objects.create(email=email)
			request.session['guest_email_id'] = guestEmail.id
			return redirect(next_post)
	else:	
		form = GuestForm()
	return render(request, 'carts/checkout.html', {'form':form})
