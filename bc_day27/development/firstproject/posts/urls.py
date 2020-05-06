from django.urls import path, include
from posts import views

app_name = 'posts'

urlpatterns = [

	# Method 1 Function Based Views 
 	path('', views.dashboard, name='dashboard'),
	path('access_denied', views.access_denied, name='access_denied'),

	# Method 1 Class Based Views 
 	# path('', views.Dashboard.as_view(), name='dashboard'),
	# path('access_denied', views.AccessDenied.as_view(), name='access_denied'),



]