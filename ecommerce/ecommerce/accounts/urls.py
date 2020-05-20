from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
	path('user_login', views.user_login, name='user_login'),
	path('user_logout', views.user_logout, name='user_logout'),
	path('signup', views.signup, name='signup'),
	path('guest_login', views.guest_login, name='guest_login'),
	
]
