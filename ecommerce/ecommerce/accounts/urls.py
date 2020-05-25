from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('user_guest', views.user_guest, name='user_guest'),
]
