from django.shortcuts import redirect

def check_member(allowed):
	def decorator(func):
		def wrapper(request, *args, **kwargs):
			print(request.user.groups)
			if request.user.groups.filter(name=allowed).exists():
				return func(request)
			else:
				return redirect('posts:access_denied')
		return wrapper
	return decorator
