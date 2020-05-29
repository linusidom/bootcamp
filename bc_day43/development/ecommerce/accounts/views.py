from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from accounts.forms import LoginForm, SignupForm, GuestForm
from accounts.models import GuestEmail
User = get_user_model()

# Create your views here.
def user_login(request):
	if request.method == 'POST':

		next_post = request.POST.get('next')

		print('Post Method', request.method, request.POST)

		form = LoginForm(request.POST)
		print('Form Data',form)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			print('Username Password', username, password)
			user = authenticate(request, username=username, password=password)
			print('Authenticated User', user)
			if user:
				login(request, user)
				
				# If a guest decides to login after registering as a guest
				# We can remove their guest email id from our session
				try:
					del request.session['guest_email_id']
					del request.session['guest_email']
				except:
					pass
				if next_post:
					return redirect(next_post)
				return redirect('index')
	else:
		print('Not Post Method', request.method)
		form = LoginForm()
	return render(request, 'accounts/user_login.html', {'form':form})

def user_logout(request):
	logout(request) # request.flush()
	return redirect('index')

def user_signup(request):
	if request.method == 'POST':
		print('Post Method', request.method, request.POST)
		form = SignupForm(request.POST)
		print('Form Data',form)
		if form.is_valid():
			username = form.data.get('username')
			email = form.data.get('email')
			password = form.data.get('password')
			print('Username Password', username, password)
			newuser = User.objects.create_user(username=username, email=email, password=password)
			print(newuser)
			if newuser:
				return redirect ('accounts:user_login')
	else:
		form = SignupForm()
	return render(request, 'accounts/user_signup.html', {'form':form})

def user_guest(request):
	if request.method == 'POST':

		next_post = request.POST.get('next')


		print('Post Method', request.method, request.POST)
		form = GuestForm(request.POST)
		print('Form Data',form)
		if form.is_valid():
			email = form.data.get('email')
			guestEmail = GuestEmail.objects.create(email=email)
			request.session['guest_email'] = guestEmail.email
			request.session['guest_email_id'] = guestEmail.id
			if next_post:
				return redirect(next_post)
			return redirect ('index')
	else:
		form = GuestForm()
	return render(request, 'accounts/user_signup.html', {'form':form})

