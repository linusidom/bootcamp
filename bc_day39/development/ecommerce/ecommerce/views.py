from django.shortcuts import render
from accounts.forms import LoginForm, GuestForm

def index_view(request):
	context = {
		'loginForm': LoginForm,
		'guestForm': GuestForm
	}
	return render(request, 'index.html', context)