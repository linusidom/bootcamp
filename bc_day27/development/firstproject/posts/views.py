from django.shortcuts import render
from django.views.generic import TemplateView

from posts.models import Post
from comments.models import Comment
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.decorators import login_required
from posts.decorators import check_member


from django.contrib.auth.mixins import LoginRequiredMixin
from posts.mixins import CheckMember
# Create your views here.

'''
Method 1 - Function Based Views Permissions to View Page
Block Anyone but admin
Send others groups to access Denied
'''
# @login_required
# @check_member(allowed='admins')
# def dashboard(request):
# 	context = {}

# 	context['posts'] = Post.objects.all().count()
# 	context['comments'] = Comment.objects.all().count()
# 	context['users'] = User.objects.all()

# 	return render(request, 'posts/dashboard.html', context)

# def access_denied(request):
# 	return render(request, 'posts/access_denied.html')



'''
Method 2 - Class Based Views Permissions to View Page
Block Anyone but admin
Send others groups to access Denied
'''

class Dashboard(LoginRequiredMixin, CheckMember, TemplateView):
	template_name = 'posts/dashboard.html'

	def get_context_data(self):
		context = super().get_context_data()
		context['posts'] = Post.objects.all().count()
		context['comments'] = Comment.objects.all().count()
		context['users'] = User.objects.all()	
		return context

class AccessDenied(TemplateView):
	template_name = 'posts/access_denied.html'


'''
Method 3 - Restrict access in the Function/Class itself
Block Anyone but admin
Send others groups to access Denied
'''
@login_required
@check_member(allowed='admins')
def dashboard(request):
	context = {}

	context['posts'] = Post.objects.all().count()
	context['comments'] = Comment.objects.all().count()
	if request.user.groups.filter(name='customers').exists():
		context['users'] = User.objects.all()
	context['users_in_template'] = User.objects.all()
	return render(request, 'posts/dashboard.html', context)

def access_denied(request):
	return render(request, 'posts/access_denied.html')





