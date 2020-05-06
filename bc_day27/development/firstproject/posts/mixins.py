from django.shortcuts import redirect

class CheckMember:
	def dispatch(self, request, *args, **kwargs):
		if request.user.groups.filter(name='admins').exists():
			return super().dispatch(request, *args, **kwargs)	
		else:
			return redirect('posts:access_denied')