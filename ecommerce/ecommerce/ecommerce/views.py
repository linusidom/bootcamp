from django.shortcuts import render
from accounts.forms import LoginForm, SignupForm

def index_view(request):
	context = {
		'loginForm': LoginForm,
		'signupForm': SignupForm,
	}
	return render(request, 'index.html', context)

def loggedin_view(request):
	return render(request, 'loggedin.html')